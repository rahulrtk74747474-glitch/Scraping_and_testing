from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
STATE_PATH = DATA / "btc_state.json"

def initial_state(starting_capital: float = 100.0) -> dict:
    return {
        "version": 1, "symbol": "BTCUSDT", "timeframe": "15m",
        "starting_capital": float(starting_capital), "balance": float(starting_capital),
        "realized_pnl": 0.0, "open_position": None, "last_processed_close_time": None,
        "equity_peak": float(starting_capital), "max_drawdown_pct": 0.0,
        "closed_trades": 0, "wins": 0, "losses": 0,
    }

def load_state(starting_capital: float = 100.0) -> dict:
    DATA.mkdir(parents=True, exist_ok=True)
    if not STATE_PATH.exists():
        return initial_state(starting_capital)
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))

def save_state(state: dict) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")

def append_csv(path: Path, rows: Iterable[dict], fields: list[str]) -> None:
    rows = list(rows)
    if not rows:
        return
    DATA.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if not exists:
            w.writeheader()
        w.writerows(rows)

def process_events(state: dict, events: list[dict], fee_rate: float = 0.001) -> tuple[list[dict], list[dict]]:
    orders, trades = [], []
    last = state.get("last_processed_close_time")
    for e in sorted(events, key=lambda x: (int(x["close_time"]), 0 if x["event"] == "dist_confirmed" else 1)):
        if last is not None and int(e["close_time"]) <= int(last):
            continue
        if e["event"] == "dist_confirmed":
            if state.get("open_position") is not None:
                continue
            balance = float(state["balance"])
            if balance <= 0:
                continue
            entry = float(e["entry"])
            notional = balance / (1.0 + fee_rate)
            qty = notional / entry
            entry_fee = notional * fee_rate
            pos = {
                "cycle": int(e["cycle"]), "dir": e["dir"], "entry_time": int(e["close_time"]),
                "entry": entry, "stop": float(e["stop"]), "target": float(e["target"]),
                "qty": qty, "entry_notional": notional, "entry_fee": entry_fee,
                "balance_before": balance,
            }
            state["open_position"] = pos
            orders.append({
                "close_time": e["close_time"], "cycle": e["cycle"], "event": "ENTRY",
                "side": "BUY" if e["dir"] == "long" else "SELL_SHORT", "price": entry,
                "qty": qty, "notional": notional, "fee": entry_fee, "balance": balance,
                "stop": e["stop"], "target": e["target"],
            })
        elif e["event"] == "outcome":
            pos = state.get("open_position")
            if pos is None or int(pos.get("cycle", -1)) != int(e["cycle"]):
                continue
            exit_price = float(e["exit"])
            qty = float(pos["qty"])
            if pos["dir"] == "long":
                gross = qty * (exit_price - float(pos["entry"]))
                side = "SELL"
            else:
                gross = qty * (float(pos["entry"]) - exit_price)
                side = "BUY_TO_COVER"
            exit_notional = qty * exit_price
            exit_fee = exit_notional * fee_rate
            net = gross - float(pos["entry_fee"]) - exit_fee
            new_balance = float(pos["balance_before"]) + net
            state["balance"] = new_balance
            state["realized_pnl"] = float(state.get("realized_pnl", 0.0)) + net
            state["closed_trades"] = int(state.get("closed_trades", 0)) + 1
            if net > 0:
                state["wins"] = int(state.get("wins", 0)) + 1
            elif net < 0:
                state["losses"] = int(state.get("losses", 0)) + 1
            peak = max(float(state.get("equity_peak", state["starting_capital"])), new_balance)
            state["equity_peak"] = peak
            dd = (peak - new_balance) / peak * 100.0 if peak > 0 else 0.0
            state["max_drawdown_pct"] = max(float(state.get("max_drawdown_pct", 0.0)), dd)
            orders.append({
                "close_time": e["close_time"], "cycle": e["cycle"], "event": "EXIT",
                "side": side, "price": exit_price, "qty": qty, "notional": exit_notional,
                "fee": exit_fee, "balance": new_balance, "stop": pos["stop"], "target": pos["target"],
            })
            trades.append({
                "cycle": e["cycle"], "dir": pos["dir"], "entry_time": pos["entry_time"],
                "exit_time": e["close_time"], "entry": pos["entry"], "exit": exit_price,
                "stop": pos["stop"], "target": pos["target"], "qty": qty,
                "gross_pnl": gross, "fees": float(pos["entry_fee"]) + exit_fee,
                "net_pnl": net, "return_pct": net / float(pos["balance_before"]) * 100.0,
                "result": e["result"], "r": e["r"], "balance_after": new_balance,
            })
            state["open_position"] = None
    return orders, trades

def mark_equity(state: dict, last_price: float, fee_rate: float = 0.001) -> tuple[float, float]:
    bal = float(state["balance"])
    pos = state.get("open_position")
    if not pos:
        return bal, 0.0
    qty = float(pos["qty"])
    gross = qty * (last_price - float(pos["entry"])) if pos["dir"] == "long" else qty * (float(pos["entry"]) - last_price)
    est_exit_fee = qty * last_price * fee_rate
    unreal = gross - float(pos["entry_fee"]) - est_exit_fee
    return float(pos["balance_before"]) + unreal, unreal

def write_report(state: dict, last_price: float, last_close_time: int, fee_rate: float = 0.001) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    equity, unreal = mark_equity(state, last_price, fee_rate)
    start = float(state["starting_capital"])
    total = equity - start
    n = int(state.get("closed_trades", 0))
    wins = int(state.get("wins", 0))
    losses = int(state.get("losses", 0))
    win_rate = (wins / n * 100.0) if n else 0.0
    pos = state.get("open_position")
    lines = [
        "# BTCUSDT 15m Paper Trader — Latest Report", "",
        f"- Starting demo money: **${start:.2f}**",
        f"- Current equity: **${equity:.4f}**",
        f"- Closed balance: **${float(state['balance']):.4f}**",
        f"- Total P&L: **${total:.4f} ({(total/start*100 if start else 0):.2f}%)**",
        f"- Realized P&L: **${float(state.get('realized_pnl',0)):.4f}**",
        f"- Unrealized P&L estimate: **${unreal:.4f}**",
        f"- Closed trades: **{n}** | Wins: **{wins}** | Losses: **{losses}** | Win rate: **{win_rate:.2f}%**",
        f"- Max drawdown: **{float(state.get('max_drawdown_pct',0)):.2f}%**",
        f"- Last BTCUSDT close: **${last_price:,.2f}**",
        f"- Last processed candle close time (ms): `{last_close_time}`", "",
        "## Open position", "",
    ]
    if pos:
        lines += [
            f"- Direction: **{pos['dir'].upper()}**",
            f"- Entry: **${float(pos['entry']):,.2f}**",
            f"- Stop: **${float(pos['stop']):,.2f}**",
            f"- Target: **${float(pos['target']):,.2f}**",
            f"- Quantity: **{float(pos['qty']):.8f} BTC**",
        ]
    else:
        lines.append("_No open position. Waiting for the next confirmed distribution signal._")
    lines += [
        "", "## Execution assumptions", "",
        "- Paper trading only: no real Binance order is sent.",
        "- Uses the indicator's default 15-minute confirmed-bar logic.",
        "- Long on distribution UP; 1x paper short on distribution DOWN.",
        "- Uses the full virtual account as 1x notional for each trade.",
        f"- Trading fee assumption: **{fee_rate*100:.3f}% per side**; slippage is currently 0.",
        "- Target/stop outcomes follow the indicator model; ambiguous same-candle target+stop is treated conservatively as a stop.", ""
    ]
    (REPORTS / "btc_latest.md").write_text("\n".join(lines), encoding="utf-8")
