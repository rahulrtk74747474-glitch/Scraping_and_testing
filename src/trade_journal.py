from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
JOURNAL_CSV = DATA / "trade_journal.csv"
JOURNAL_MD = REPORTS / "trade_journal.md"
IST = ZoneInfo("Asia/Kolkata")

FIELDS = [
    "trade_id", "strategy", "symbol", "timeframe", "currency", "direction",
    "entry_time", "exit_time", "entry_signal", "entry_reason",
    "exit_signal", "exit_reason", "entry_price", "exit_price", "quantity",
    "entry_value", "exit_value", "stop", "target", "gross_pnl", "fees",
    "net_pnl", "return_pct", "result", "holding_period", "notes",
]


def _read_csv(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _num(value, default: float = 0.0) -> float:
    try:
        if value in (None, ""):
            return float(default)
        return float(value)
    except (TypeError, ValueError):
        return float(default)


def _fmt_num(value, digits: int = 4) -> str:
    if value in (None, ""):
        return ""
    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)


def _fmt_ms(value) -> str:
    try:
        ms = int(float(value))
        return datetime.fromtimestamp(ms / 1000, tz=IST).strftime("%Y-%m-%d %H:%M:%S IST")
    except (TypeError, ValueError, OSError):
        return str(value or "-")


def _fmt_date(value) -> str:
    return str(value or "-")


def _holding_ms(entry, exit_) -> str:
    try:
        sec = max(0, (int(float(exit_)) - int(float(entry))) // 1000)
    except (TypeError, ValueError):
        return "-"
    days, rem = divmod(sec, 86400)
    hours, rem = divmod(rem, 3600)
    mins = rem // 60
    return f"{days}d {hours}h {mins}m"


def _result(pnl: float) -> str:
    if pnl > 1e-12:
        return "PROFIT"
    if pnl < -1e-12:
        return "LOSS"
    return "BREAKEVEN"


def _money(value, currency: str) -> str:
    if value in (None, ""):
        return "-"
    x = _num(value)
    if currency == "USD":
        return f"${x:,.4f}"
    return f"₹{x:,.2f}"


def _price(value, currency: str) -> str:
    if value in (None, ""):
        return "-"
    try:
        x = float(value)
    except (TypeError, ValueError):
        return str(value)
    if currency == "USD":
        return f"${x:,.4f}"
    return f"₹{x:,.4f}"


def _write(rows: list[dict], title: str) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    clean = [{k: row.get(k, "") for k in FIELDS} for row in rows]
    with JOURNAL_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(clean)

    pnls = [_num(r.get("net_pnl")) for r in clean]
    wins = sum(1 for x in pnls if x > 0)
    losses = sum(1 for x in pnls if x < 0)
    total = sum(pnls)
    avg_ret = (
        sum(_num(r.get("return_pct")) for r in clean) / len(clean)
        if clean else 0.0
    )
    currency = clean[-1].get("currency", "INR") if clean else "INR"

    lines = [
        f"# {title} — Closed Trade Journal",
        "",
        "_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._",
        "",
        "## Journal summary",
        "",
        f"- Closed trade records: **{len(clean)}**",
        f"- Profits / losses: **{wins} / {losses}**",
        f"- Net realized P&L in journal: **{_money(total, currency)}**",
        f"- Average return per closed trade: **{avg_ret:.4f}%**",
        "",
    ]
    if not clean:
        lines += [
            "## Trades",
            "",
            "_No closed trades have been recorded yet._",
            "",
        ]
    else:
        lines += [
            "## Quick history",
            "",
            "| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |",
            "|---:|---|---|---|---|---:|---:|---|",
        ]
        newest = list(reversed(clean))
        for i, r in enumerate(newest, 1):
            cur = r.get("currency", "INR")
            lines.append(
                f"| {i} | {r.get('exit_time','-')} | {r.get('symbol','-')} | "
                f"{r.get('direction','-')} | {r.get('result','-')} | "
                f"{_money(r.get('net_pnl'), cur)} | {_num(r.get('return_pct')):.4f}% | "
                f"{r.get('exit_reason','-')} |"
            )
        lines += ["", "## Full trade details", ""]
        for i, r in enumerate(newest, 1):
            cur = r.get("currency", "INR")
            lines += [
                f"### Trade {len(clean) - i + 1} — {r.get('result','-')} — {r.get('symbol','-')}",
                "",
                f"- Trade ID: `{r.get('trade_id','-')}`",
                f"- Strategy: **{r.get('strategy','-')}**",
                f"- Timeframe: **{r.get('timeframe','-')}**",
                f"- Direction: **{r.get('direction','-')}**",
                f"- Entry time: **{r.get('entry_time','-')}**",
                f"- Entry signal: **{r.get('entry_signal','-')}**",
                f"- Why entry was taken: {r.get('entry_reason','-')}",
                f"- Entry price: **{_price(r.get('entry_price'), cur)}**",
                f"- Quantity: **{r.get('quantity','-')}**",
                f"- Entry value/cost: **{_money(r.get('entry_value'), cur)}**",
                f"- Stop: **{r.get('stop','-')}**",
                f"- Target: **{r.get('target','-')}**",
                f"- Exit time: **{r.get('exit_time','-')}**",
                f"- Exit signal: **{r.get('exit_signal','-')}**",
                f"- Why position was closed/reduced: {r.get('exit_reason','-')}",
                f"- Exit price: **{_price(r.get('exit_price'), cur)}**",
                f"- Exit value/proceeds: **{_money(r.get('exit_value'), cur)}**",
                f"- Gross P&L: **{_money(r.get('gross_pnl'), cur)}**",
                f"- Fees/charges: **{_money(r.get('fees'), cur)}**",
                f"- Net P&L: **{_money(r.get('net_pnl'), cur)}**",
                f"- Profit/Loss percentage: **{_num(r.get('return_pct')):.4f}%**",
                f"- Holding period: **{r.get('holding_period','-')}**",
                f"- Notes: {r.get('notes','-')}",
                "",
            ]
    JOURNAL_MD.write_text("\n".join(lines), encoding="utf-8")


def write_vertex_journal() -> None:
    trades = _read_csv(DATA / "trades.csv")
    signals = _read_csv(DATA / "signals.csv")
    sig_map = {(r.get("date"), str(r.get("symbol", "")).upper()): r for r in signals}
    rows = []
    for t in trades:
        symbol = str(t.get("symbol", "")).upper()
        entry_date = t.get("entry_date", "")
        sig = sig_map.get((entry_date, symbol), {})
        pnl = _num(t.get("net_pnl"))
        reason_bits = [
            "Stock appeared in the configured Chartink/Vertex screener on the entry date.",
        ]
        if sig.get("name"):
            reason_bits.append(f"Scanner name: {sig.get('name')}.")
        if sig.get("change_pct") not in (None, ""):
            reason_bits.append(f"Scanner change: {sig.get('change_pct')}%.")
        rows.append({
            "trade_id": f"VERTEX-{symbol}-{entry_date}-{t.get('exit_date','')}",
            "strategy": "Vertex Chartink paper trader",
            "symbol": symbol,
            "timeframe": "Daily decision cycle",
            "currency": "INR",
            "direction": "LONG",
            "entry_time": _fmt_date(entry_date),
            "exit_time": _fmt_date(t.get("exit_date")),
            "entry_signal": "VERTEX_CHARTINK_SIGNAL",
            "entry_reason": " ".join(reason_bits),
            "exit_signal": "DAILY_CLOSE_ABOVE_ORIGINAL_ENTRY",
            "exit_reason": "A later completed daily close was above the original entry price, which is the configured Vertex exit rule.",
            "entry_price": _fmt_num(t.get("entry_price")),
            "exit_price": _fmt_num(t.get("exit_price")),
            "quantity": t.get("qty", ""),
            "entry_value": _fmt_num(t.get("buy_turnover"), 2),
            "exit_value": _fmt_num(t.get("sell_turnover"), 2),
            "stop": "Not used — no fixed stop is configured.",
            "target": "Rule-based target: first later daily close above original entry price.",
            "gross_pnl": _fmt_num(t.get("gross_pnl"), 2),
            "fees": _fmt_num(t.get("total_charges"), 2),
            "net_pnl": _fmt_num(pnl, 2),
            "return_pct": _fmt_num(t.get("return_pct"), 4),
            "result": _result(pnl),
            "holding_period": f"{t.get('days_held','-')} day(s)",
            "notes": (
                f"Average-add count: {t.get('average_add_count','0')}; "
                f"average-added notional: ₹{_num(t.get('average_added_notional')):,.2f}; "
                f"maximum capital in trade: ₹{_num(t.get('max_capital_in_trade')):,.2f}."
            ),
        })
    _write(rows, "Vertex")


def write_btc_journal() -> None:
    trades = _read_csv(DATA / "btc_trades.csv")
    rows = []
    for t in trades:
        d = str(t.get("dir", "")).lower()
        pnl = _num(t.get("net_pnl"))
        result = str(t.get("result", "")).upper() or _result(pnl)
        rows.append({
            "trade_id": f"BTCUSDT-{t.get('cycle','')}",
            "strategy": "BTCUSDT confirmed-distribution paper trader",
            "symbol": "BTCUSDT",
            "timeframe": "15m",
            "currency": "USD",
            "direction": d.upper(),
            "entry_time": _fmt_ms(t.get("entry_time")),
            "exit_time": _fmt_ms(t.get("exit_time")),
            "entry_signal": "DISTRIBUTION_UP_CONFIRMED" if d == "long" else "DISTRIBUTION_DOWN_CONFIRMED",
            "entry_reason": (
                "A confirmed distribution signal opened a LONG after the strategy's sweep/distribution conditions."
                if d == "long"
                else "A confirmed distribution signal opened a SHORT after the strategy's sweep/distribution conditions."
            ),
            "exit_signal": result,
            "exit_reason": "Configured profit target was hit." if result == "TARGET" else "Configured stop level was hit." if result == "STOP" else f"Strategy outcome: {result}.",
            "entry_price": _fmt_num(t.get("entry")),
            "exit_price": _fmt_num(t.get("exit")),
            "quantity": t.get("qty", ""),
            "entry_value": "",
            "exit_value": "",
            "stop": _fmt_num(t.get("stop")),
            "target": _fmt_num(t.get("target")),
            "gross_pnl": _fmt_num(t.get("gross_pnl"), 6),
            "fees": _fmt_num(t.get("fees"), 6),
            "net_pnl": _fmt_num(pnl, 6),
            "return_pct": _fmt_num(t.get("return_pct"), 4),
            "result": _result(pnl),
            "holding_period": _holding_ms(t.get("entry_time"), t.get("exit_time")),
            "notes": f"Outcome={result}; R multiple={t.get('r','-')}; balance after=${_num(t.get('balance_after')):,.4f}.",
        })
    _write(rows, "BTCUSDT 15m")


def write_order_block_journal(cfg: dict) -> None:
    slug = cfg["slug"]
    trades = _read_csv(DATA / f"{slug}_trades.csv")
    signals = _read_csv(DATA / f"{slug}_signals.csv")
    orders = _read_csv(DATA / f"{slug}_orders.csv")
    sig_map = {str(r.get("confirmed_close_time")): r for r in signals}
    order_map = {str(r.get("close_time")): r for r in orders}
    rows = []
    for i, t in enumerate(trades, 1):
        entry_t = str(t.get("entry_time", ""))
        exit_t = str(t.get("exit_time", ""))
        es = sig_map.get(entry_t, {})
        xs = sig_map.get(exit_t, {})
        eo = order_map.get(entry_t, {})
        xo = order_map.get(exit_t, {})
        pnl = _num(t.get("net_pnl_inr"))
        entry_gross = _num(t.get("entry_price_inr")) * _num(t.get("qty"))
        exit_gross = _num(t.get("exit_price_inr")) * _num(t.get("qty"))
        fees = _num(eo.get("fee_inr")) + _num(xo.get("fee_inr"))
        rows.append({
            "trade_id": f"{slug.upper()}-{i}-{entry_t}",
            "strategy": f"{cfg['display_symbol']} Order Block",
            "symbol": cfg["display_symbol"],
            "timeframe": "15m",
            "currency": "INR",
            "direction": "LONG",
            "entry_time": _fmt_ms(entry_t),
            "exit_time": _fmt_ms(exit_t),
            "entry_signal": "BULLISH_OB",
            "entry_reason": (
                f"Confirmed bullish order block: the identified OB candle was the last down candle before "
                f"{int(cfg.get('periods', 5))} required up candles; entry executed at the confirmation-candle close. "
                f"Detected move={es.get('move_pct','-')}%."
            ),
            "exit_signal": "BEARISH_OB",
            "exit_reason": (
                f"Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. "
                f"Detected move={xs.get('move_pct','-')}%."
            ),
            "entry_price": _fmt_num(t.get("entry_price_inr")),
            "exit_price": _fmt_num(t.get("exit_price_inr")),
            "quantity": t.get("qty", ""),
            "entry_value": _fmt_num(t.get("entry_total_inr"), 2),
            "exit_value": _fmt_num(t.get("exit_proceeds_inr"), 2),
            "stop": "Not used — this strategy exits on a confirmed bearish order block.",
            "target": "Not fixed — position remains open until a confirmed bearish order block.",
            "gross_pnl": _fmt_num(exit_gross - entry_gross, 2),
            "fees": _fmt_num(fees, 2),
            "net_pnl": _fmt_num(pnl, 2),
            "return_pct": _fmt_num(t.get("return_pct"), 4),
            "result": _result(pnl),
            "holding_period": _holding_ms(entry_t, exit_t),
            "notes": (
                f"Entry OB candle={_fmt_ms(t.get('entry_ob_open_time'))}; "
                f"exit OB candle={_fmt_ms(t.get('exit_ob_open_time'))}; "
                f"use_wicks={bool(cfg.get('use_wicks', False))}; threshold={cfg.get('threshold_pct',0)}%."
            ),
        })
    _write(rows, f"{cfg['display_symbol']} Order Block 15m")


def write_smc_journal(cfg: dict) -> None:
    slug = cfg["slug"]
    trades = _read_csv(DATA / f"{slug}_trades.csv")
    orders = _read_csv(DATA / f"{slug}_orders.csv")
    order_map = {str(r.get("close_time")): r for r in orders}
    rows = []
    for i, t in enumerate(trades, 1):
        entry_t = str(t.get("entry_time", ""))
        exit_t = str(t.get("exit_time", ""))
        xo = order_map.get(exit_t, {})
        pnl = _num(t.get("net_pnl_inr"))
        qty = _num(t.get("qty"))
        allocated = _num(t.get("allocated_cost_inr"))
        effective_entry = allocated / qty if qty else 0.0
        exit_price = _num(t.get("exit_price_inr"))
        sizing = xo.get("sizing_rule", "SMC sell sizing")
        frac = xo.get("fraction_pct", "")
        rows.append({
            "trade_id": f"{slug.upper()}-{i}-{exit_t}",
            "strategy": f"{cfg['display_symbol']} SMC Clean Wave major swings",
            "symbol": cfg["display_symbol"],
            "timeframe": cfg.get("timeframe", "15m"),
            "currency": "INR",
            "direction": "LONG",
            "entry_time": _fmt_ms(entry_t),
            "exit_time": _fmt_ms(exit_t),
            "entry_signal": "CONFIRMED_PIVOT_LOW_BUY",
            "entry_reason": "A confirmed major pivot low generated the BUY side of the SMC major-swing strategy. Position size follows the configured restore/50%/12.5% ladder rules.",
            "exit_signal": "CONFIRMED_PIVOT_HIGH_SELL",
            "exit_reason": f"A confirmed major pivot high generated a SELL. This realized slice used sizing rule {sizing}" + (f" at {frac}%." if frac not in (None, "") else "."),
            "entry_price": _fmt_num(effective_entry),
            "exit_price": _fmt_num(exit_price),
            "quantity": t.get("qty", ""),
            "entry_value": _fmt_num(allocated, 2),
            "exit_value": _fmt_num(t.get("exit_proceeds_inr"), 2),
            "stop": "Not used — this strategy reduces/exits on confirmed opposite major swings.",
            "target": "Not fixed — SELL decisions come from confirmed pivot-high signals.",
            "gross_pnl": "",
            "fees": _fmt_num(xo.get("fee_inr"), 2),
            "net_pnl": _fmt_num(pnl, 2),
            "return_pct": _fmt_num(t.get("return_pct"), 4),
            "result": _result(pnl),
            "holding_period": _holding_ms(entry_t, exit_t),
            "notes": (
                f"SMC uses scale-in/scale-out sizing. This row is a realized SELL slice; "
                f"exit ladder step={t.get('exit_ladder_step','-')}, fraction={t.get('fraction_pct','-')}%. "
                f"A position can remain partly open after this journal row."
            ),
        })
    _write(rows, f"{cfg['display_symbol']} SMC {cfg.get('timeframe','')}")


def write_trade_journal(kind: str, cfg: dict | None = None) -> None:
    kind = kind.lower().strip()
    if kind == "vertex":
        write_vertex_journal()
    elif kind == "btc":
        write_btc_journal()
    elif kind == "order_block":
        if cfg is None:
            raise ValueError("cfg is required for order_block journal")
        write_order_block_journal(cfg)
    elif kind == "smc":
        if cfg is None:
            raise ValueError("cfg is required for smc journal")
        write_smc_journal(cfg)
    else:
        raise ValueError(f"Unsupported journal kind: {kind}")
