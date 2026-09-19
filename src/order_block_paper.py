from __future__ import annotations

import csv
import json
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

import requests
import yfinance as yf
from .trade_journal import write_trade_journal

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "order_block_config.json"
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
INTERVAL_MS = 15 * 60 * 1000

@dataclass(frozen=True)
class Bar:
    open_time: int
    open: float
    high: float
    low: float
    close: float
    close_time: int

def load_config() -> dict:
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    required = {"slug", "display_symbol", "source", "ticker", "quote_currency", "starting_capital_inr"}
    missing = sorted(required - set(cfg))
    if missing:
        raise RuntimeError(f"Missing config keys: {missing}")
    cfg.setdefault("periods", 5)
    cfg.setdefault("threshold_pct", 0.0)
    cfg.setdefault("use_wicks", False)
    cfg.setdefault("fee_rate", 0.0)
    cfg.setdefault("source_note", "")
    return cfg

def _closed_only(bars: list[Bar]) -> list[Bar]:
    now_ms = int(time.time() * 1000)
    return [b for b in bars if b.close_time < now_ms]

def fetch_binance_15m(symbol: str, limit: int = 1000) -> list[Bar]:
    url = "https://data-api.binance.vision/api/v3/klines"
    r = requests.get(url, params={"symbol": symbol, "interval": "15m", "limit": min(max(limit, 10), 1000)}, timeout=25)
    r.raise_for_status()
    bars = [
        Bar(int(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4]), int(x[6]))
        for x in r.json()
    ]
    return _closed_only(bars)

def fetch_yahoo_15m(ticker: str) -> list[Bar]:
    df = yf.download(
        ticker,
        period="10d",
        interval="15m",
        auto_adjust=False,
        prepost=False,
        progress=False,
        threads=False,
    )
    if df is None or df.empty:
        raise RuntimeError(f"No 15m data returned by Yahoo Finance for {ticker}.")
    if getattr(df.columns, "nlevels", 1) > 1:
        df.columns = [c[0] for c in df.columns]
    needed = {"Open", "High", "Low", "Close"}
    if not needed.issubset(df.columns):
        raise RuntimeError(f"Yahoo data for {ticker} is missing OHLC columns: {list(df.columns)}")
    bars: list[Bar] = []
    for ts, row in df.dropna(subset=["Open", "High", "Low", "Close"]).iterrows():
        pyts = ts.to_pydatetime()
        if pyts.tzinfo is None:
            pyts = pyts.replace(tzinfo=timezone.utc)
        else:
            pyts = pyts.astimezone(timezone.utc)
        open_ms = int(pyts.timestamp() * 1000)
        bars.append(Bar(
            open_ms,
            float(row["Open"]),
            float(row["High"]),
            float(row["Low"]),
            float(row["Close"]),
            open_ms + INTERVAL_MS - 1,
        ))
    bars.sort(key=lambda b: b.open_time)
    return _closed_only(bars)

def fetch_usdinr() -> float:
    df = yf.download("INR=X", period="5d", interval="15m", auto_adjust=False, progress=False, threads=False)
    if df is None or df.empty:
        df = yf.download("INR=X", period="1mo", interval="1d", auto_adjust=False, progress=False, threads=False)
    if df is None or df.empty:
        raise RuntimeError("Unable to fetch USD/INR conversion rate from Yahoo Finance.")
    if getattr(df.columns, "nlevels", 1) > 1:
        df.columns = [c[0] for c in df.columns]
    close = df["Close"].dropna()
    if close.empty:
        raise RuntimeError("USD/INR data has no usable close.")
    return float(close.iloc[-1])

def fetch_bars(cfg: dict) -> list[Bar]:
    if cfg["source"] == "binance_spot":
        return fetch_binance_15m(cfg["ticker"])
    if cfg["source"] == "yahoo":
        return fetch_yahoo_15m(cfg["ticker"])
    raise RuntimeError(f"Unsupported source: {cfg['source']}")

def px_inr(price: float, cfg: dict, usdinr: float) -> float:
    q = str(cfg["quote_currency"]).upper()
    if q == "INR":
        return float(price)
    if q in {"USD", "USDT"}:
        return float(price) * float(usdinr)
    raise RuntimeError(f"Unsupported quote currency: {q}")

def detect_signal(bars: list[Bar], i: int, periods: int = 5, threshold_pct: float = 0.0, use_wicks: bool = False) -> Optional[dict]:
    # Pine evaluates OB_bull/OB_bear on the next live bar using only [1..periods]
    # plus the OB candle at [periods+1]. When we run just after a 15m close,
    # bars[i] is Pine's [1], so the OB candle is i-periods and the five
    # qualifying candles are i-periods+1 .. i. This avoids an extra-bar delay.
    if i < periods:
        return None
    ob = bars[i - periods]
    last_follow = bars[i]
    absmove = abs(ob.close - last_follow.close) / ob.close * 100.0 if ob.close else 0.0
    if absmove < threshold_pct:
        return None
    following = bars[i - periods + 1:i + 1]
    bull = ob.close < ob.open and len(following) == periods and all(b.close > b.open for b in following)
    bear = ob.close > ob.open and len(following) == periods and all(b.close < b.open for b in following)
    if bull:
        high = ob.high if use_wicks else ob.open
        low = ob.low
        return {
            "signal": "BULLISH_OB",
            "confirmed_close_time": bars[i].close_time,
            "confirmed_price": bars[i].close,
            "ob_open_time": ob.open_time,
            "ob_high": high,
            "ob_low": low,
            "ob_avg": (high + low) / 2.0,
            "move_pct": absmove,
        }
    if bear:
        high = ob.high
        low = ob.low if use_wicks else ob.open
        return {
            "signal": "BEARISH_OB",
            "confirmed_close_time": bars[i].close_time,
            "confirmed_price": bars[i].close,
            "ob_open_time": ob.open_time,
            "ob_high": high,
            "ob_low": low,
            "ob_avg": (high + low) / 2.0,
            "move_pct": absmove,
        }
    return None

def append_csv(path: Path, rows: Iterable[dict], fields: list[str]) -> None:
    rows = list(rows)
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if not exists:
            w.writeheader()
        w.writerows(rows)

def initial_state(cfg: dict) -> dict:
    start = float(cfg["starting_capital_inr"])
    return {
        "version": 1,
        "strategy": "Order Block Finder v4 logic",
        "symbol": cfg["display_symbol"],
        "timeframe": "15m",
        "starting_capital_inr": start,
        "cash_inr": start,
        "realized_pnl_inr": 0.0,
        "position": None,
        "last_processed_close_time": None,
        "last_signal": None,
        "equity_peak_inr": start,
        "max_drawdown_pct": 0.0,
        "closed_trades": 0,
        "wins": 0,
        "losses": 0,
    }

def paths(cfg: dict) -> dict:
    slug = cfg["slug"]
    return {
        "state": DATA / f"{slug}_state.json",
        "signals": DATA / f"{slug}_signals.csv",
        "orders": DATA / f"{slug}_orders.csv",
        "trades": DATA / f"{slug}_trades.csv",
        "snapshots": DATA / f"{slug}_snapshots.csv",
        "report": REPORTS / f"{slug}_latest.md",
    }

def load_state(cfg: dict, p: dict) -> dict:
    if not p["state"].exists():
        return initial_state(cfg)
    return json.loads(p["state"].read_text(encoding="utf-8"))

def save_state(state: dict, p: dict) -> None:
    p["state"].parent.mkdir(parents=True, exist_ok=True)
    p["state"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")

def mark_equity(state: dict, last_price_inr: float) -> tuple[float, float]:
    pos = state.get("position")
    if not pos:
        return float(state["cash_inr"]), 0.0
    market_value = float(pos["qty"]) * last_price_inr
    unreal = market_value - float(pos["entry_cost_inr"])
    return market_value, unreal

def process_signal(state: dict, sig: dict, bar: Bar, cfg: dict, usdinr: float) -> tuple[list[dict], list[dict]]:
    orders: list[dict] = []
    trades: list[dict] = []
    fee_rate = float(cfg.get("fee_rate", 0.0))
    price_quote = float(bar.close)
    price_inr = px_inr(price_quote, cfg, usdinr)

    if sig["signal"] == "BULLISH_OB" and state.get("position") is None:
        cash = float(state["cash_inr"])
        if cash > 0 and price_inr > 0:
            notional = cash / (1.0 + fee_rate)
            fee = notional * fee_rate
            qty = notional / price_inr
            state["position"] = {
                "entry_time": int(bar.close_time),
                "entry_price_quote": price_quote,
                "entry_price_inr": price_inr,
                "entry_cost_inr": notional,
                "entry_fee_inr": fee,
                "qty": qty,
                "ob_open_time": int(sig["ob_open_time"]),
                "ob_high": float(sig["ob_high"]),
                "ob_low": float(sig["ob_low"]),
                "ob_avg": float(sig["ob_avg"]),
            }
            state["cash_inr"] = 0.0
            orders.append({
                "close_time": bar.close_time,
                "signal": sig["signal"],
                "side": "BUY",
                "price_quote": price_quote,
                "price_inr": price_inr,
                "qty": qty,
                "gross_notional_inr": notional,
                "fee_inr": fee,
                "cash_after_inr": 0.0,
            })

    elif sig["signal"] == "BEARISH_OB" and state.get("position") is not None:
        pos = state["position"]
        qty = float(pos["qty"])
        gross_proceeds = qty * price_inr
        exit_fee = gross_proceeds * fee_rate
        proceeds = gross_proceeds - exit_fee
        entry_total = float(pos["entry_cost_inr"]) + float(pos.get("entry_fee_inr", 0.0))
        net = proceeds - entry_total
        state["cash_inr"] = proceeds
        state["realized_pnl_inr"] = float(state.get("realized_pnl_inr", 0.0)) + net
        state["closed_trades"] = int(state.get("closed_trades", 0)) + 1
        if net > 0:
            state["wins"] = int(state.get("wins", 0)) + 1
        elif net < 0:
            state["losses"] = int(state.get("losses", 0)) + 1
        orders.append({
            "close_time": bar.close_time,
            "signal": sig["signal"],
            "side": "SELL",
            "price_quote": price_quote,
            "price_inr": price_inr,
            "qty": qty,
            "gross_notional_inr": gross_proceeds,
            "fee_inr": exit_fee,
            "cash_after_inr": proceeds,
        })
        trades.append({
            "entry_time": pos["entry_time"],
            "exit_time": bar.close_time,
            "entry_price_quote": pos["entry_price_quote"],
            "exit_price_quote": price_quote,
            "entry_price_inr": pos["entry_price_inr"],
            "exit_price_inr": price_inr,
            "qty": qty,
            "entry_total_inr": entry_total,
            "exit_proceeds_inr": proceeds,
            "net_pnl_inr": net,
            "return_pct": (net / entry_total * 100.0) if entry_total else 0.0,
            "entry_ob_open_time": pos.get("ob_open_time"),
            "exit_ob_open_time": sig.get("ob_open_time"),
        })
        state["position"] = None
    state["last_signal"] = sig
    return orders, trades

def update_drawdown(state: dict, equity: float) -> None:
    peak = max(float(state.get("equity_peak_inr", state["starting_capital_inr"])), equity)
    state["equity_peak_inr"] = peak
    dd = (peak - equity) / peak * 100.0 if peak else 0.0
    state["max_drawdown_pct"] = max(float(state.get("max_drawdown_pct", 0.0)), dd)

def fmt_time(ms: Optional[int]) -> str:
    if not ms:
        return "-"
    return datetime.fromtimestamp(int(ms) / 1000, tz=timezone.utc).isoformat()

def write_report(state: dict, cfg: dict, p: dict, last_bar: Bar, usdinr: float) -> None:
    last_inr = px_inr(last_bar.close, cfg, usdinr)
    equity, unreal = mark_equity(state, last_inr)
    start = float(state["starting_capital_inr"])
    n = int(state.get("closed_trades", 0))
    wins = int(state.get("wins", 0))
    win_rate = wins / n * 100.0 if n else 0.0
    pos = state.get("position")
    last_sig = state.get("last_signal")
    lines = [
        f"# {cfg['display_symbol']} 15m Order-Block Paper Trader — Latest",
        "",
        f"- Starting demo money: **₹{start:,.2f}**",
        f"- Current equity: **₹{equity:,.2f}**",
        f"- Cash: **₹{float(state['cash_inr']):,.2f}**",
        f"- Total P&L: **₹{equity - start:,.2f} ({((equity / start) - 1) * 100 if start else 0:.2f}%)**",
        f"- Realized P&L: **₹{float(state.get('realized_pnl_inr', 0)):,.2f}**",
        f"- Unrealized P&L: **₹{unreal:,.2f}**",
        f"- Closed trades: **{n}** | Wins: **{wins}** | Losses: **{int(state.get('losses', 0))}** | Win rate: **{win_rate:.2f}%**",
        f"- Max drawdown: **{float(state.get('max_drawdown_pct', 0)):.2f}%**",
        f"- Latest source close: **{last_bar.close:,.6f} {cfg['quote_currency']}**",
        f"- USD/INR used this run: **{usdinr:.4f}**" if str(cfg["quote_currency"]).upper() != "INR" else "- Quote currency: **INR**",
        f"- Last processed candle: `{fmt_time(state.get('last_processed_close_time'))}`",
        "",
        "## Position",
        "",
    ]
    if pos:
        lines += [
            "- Status: **LONG / fully invested**",
            f"- Entry time: `{fmt_time(pos['entry_time'])}`",
            f"- Entry price: **{float(pos['entry_price_quote']):,.6f} {cfg['quote_currency']}**",
            f"- Quantity (synthetic units): **{float(pos['qty']):.10f}**",
        ]
    else:
        lines.append("_Flat. Waiting for the next confirmed bullish order block._")
    lines += ["", "## Latest detected order block", ""]
    if last_sig:
        lines += [
            f"- Signal: **{last_sig['signal']}**",
            f"- Confirmation time: `{fmt_time(last_sig['confirmed_close_time'])}`",
            f"- Original OB candle open time: `{fmt_time(last_sig['ob_open_time'])}`",
            f"- OB high / avg / low: **{last_sig['ob_high']:.6f} / {last_sig['ob_avg']:.6f} / {last_sig['ob_low']:.6f}**",
            f"- Move used by indicator: **{last_sig['move_pct']:.4f}%**",
        ]
    else:
        lines.append("_No confirmed order block has been recorded since initialization._")
    lines += [
        "",
        "## Rules mirrored from the supplied Pine indicator",
        "",
        "- Timeframe: **15 minutes**.",
        f"- Relevant periods: **{int(cfg['periods'])}**.",
        f"- Minimum percent move threshold: **{float(cfg['threshold_pct']):.2f}%**.",
        f"- Use whole wick range: **{'Yes' if cfg['use_wicks'] else 'No'}**.",
        "- Bullish OB: last down candle before the required sequence of up candles.",
        "- Bearish OB: last up candle before the required sequence of down candles.",
        "- Buy only when the bullish OB is confirmed; use the full available paper account.",
        "- Sell the entire long position when a bearish OB is confirmed.",
        "- No short position is opened while flat.",
        "- Signals are executed at the confirmation candle close, not backdated to the visually offset OB candle.",
        f"- Fee assumption: **{float(cfg.get('fee_rate', 0)) * 100:.4f}% per side**; slippage: **0**.",
        "",
        "## Data source",
        "",
        f"- Source: **{cfg['source']} / {cfg['ticker']}**.",
    ]
    if cfg.get("source_note"):
        lines.append(f"- Note: {cfg['source_note']}")
    lines += ["", "_Paper trading/research only; no real order is sent._", ""]
    p["report"].parent.mkdir(parents=True, exist_ok=True)
    p["report"].write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    cfg = load_config()
    p = paths(cfg)
    bars = fetch_bars(cfg)
    if len(bars) < int(cfg["periods"]) + 2:
        raise RuntimeError(f"Not enough closed 15m bars for {cfg['display_symbol']}.")
    usdinr = 1.0 if str(cfg["quote_currency"]).upper() == "INR" else fetch_usdinr()
    state = load_state(cfg, p)
    newest = bars[-1]
    last_processed = state.get("last_processed_close_time")

    if last_processed is None:
        state["last_processed_close_time"] = newest.close_time
        equity, unreal = mark_equity(state, px_inr(newest.close, cfg, usdinr))
        update_drawdown(state, equity)
        save_state(state, p)
        append_csv(p["snapshots"], [{
            "close_time": newest.close_time,
            "utc": fmt_time(newest.close_time),
            "price_quote": newest.close,
            "price_inr": px_inr(newest.close, cfg, usdinr),
            "cash_inr": state["cash_inr"],
            "equity_inr": equity,
            "unrealized_pnl_inr": unreal,
            "position": "",
            "note": "initialized_no_historical_replay",
        }], ["close_time", "utc", "price_quote", "price_inr", "cash_inr", "equity_inr", "unrealized_pnl_inr", "position", "note"])
        write_report(state, cfg, p, newest, usdinr)
        write_trade_journal("order_block", cfg)
        print(f"Initialized {cfg['display_symbol']} at latest completed 15m candle; no historical trade replay.")
        return

    if newest.close_time <= int(last_processed):
        write_trade_journal("order_block", cfg)
        print(f"No new completed 15m candle for {cfg['display_symbol']}.")
        return

    signals = []
    orders = []
    trades = []
    start_idx = 0
    for idx, bar in enumerate(bars):
        if bar.close_time > int(last_processed):
            start_idx = idx
            break
    for i in range(start_idx, len(bars)):
        sig = detect_signal(
            bars,
            i,
            periods=int(cfg["periods"]),
            threshold_pct=float(cfg["threshold_pct"]),
            use_wicks=bool(cfg["use_wicks"]),
        )
        if sig:
            signals.append(sig)
            o, t = process_signal(state, sig, bars[i], cfg, usdinr)
            orders.extend(o)
            trades.extend(t)

    state["last_processed_close_time"] = newest.close_time
    last_inr = px_inr(newest.close, cfg, usdinr)
    equity, unreal = mark_equity(state, last_inr)
    update_drawdown(state, equity)
    save_state(state, p)

    append_csv(p["signals"], signals, [
        "signal", "confirmed_close_time", "confirmed_price", "ob_open_time", "ob_high", "ob_low", "ob_avg", "move_pct"
    ])
    append_csv(p["orders"], orders, [
        "close_time", "signal", "side", "price_quote", "price_inr", "qty", "gross_notional_inr", "fee_inr", "cash_after_inr"
    ])
    append_csv(p["trades"], trades, [
        "entry_time", "exit_time", "entry_price_quote", "exit_price_quote", "entry_price_inr", "exit_price_inr", "qty",
        "entry_total_inr", "exit_proceeds_inr", "net_pnl_inr", "return_pct", "entry_ob_open_time", "exit_ob_open_time"
    ])
    append_csv(p["snapshots"], [{
        "close_time": newest.close_time,
        "utc": fmt_time(newest.close_time),
        "price_quote": newest.close,
        "price_inr": last_inr,
        "cash_inr": state["cash_inr"],
        "equity_inr": equity,
        "unrealized_pnl_inr": unreal,
        "position": "LONG" if state.get("position") else "",
        "note": "",
    }], ["close_time", "utc", "price_quote", "price_inr", "cash_inr", "equity_inr", "unrealized_pnl_inr", "position", "note"])
    write_report(state, cfg, p, newest, usdinr)
    write_trade_journal("order_block", cfg)
    print(f"{cfg['display_symbol']} processed through {fmt_time(newest.close_time)}; signals={len(signals)} orders={len(orders)} trades={len(trades)} equity=₹{equity:.2f}")

if __name__ == "__main__":
    main()
