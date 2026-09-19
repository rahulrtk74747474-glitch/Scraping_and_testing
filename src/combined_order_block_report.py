from __future__ import annotations

import csv
import io
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "order_block_combined_latest.md"

STRATEGIES = [
    {"name": "NIFTY", "branch": "ob-nifty-15m-paper", "slug": "ob_nifty"},
    {"name": "BANKNIFTY", "branch": "ob-banknifty-15m-paper", "slug": "ob_banknifty"},
    {"name": "BTCUSDT", "branch": "ob-btcusdt-15m-paper", "slug": "ob_btcusdt"},
    {"name": "XAUUSDT", "branch": "ob-xauusdt-15m-paper", "slug": "ob_xauusdt"},
]

def git_show(branch: str, path: str) -> str | None:
    p = subprocess.run(
        ["git", "show", f"origin/{branch}:{path}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    return p.stdout if p.returncode == 0 else None

def read_json(branch: str, path: str) -> dict:
    raw = git_show(branch, path)
    return json.loads(raw) if raw else {}

def read_csv_last(branch: str, path: str) -> dict:
    raw = git_show(branch, path)
    if not raw or not raw.strip():
        return {}
    rows = list(csv.DictReader(io.StringIO(raw)))
    return rows[-1] if rows else {}

def fnum(v, default=0.0):
    try:
        return float(v)
    except Exception:
        return float(default)

def fint(v, default=0):
    try:
        return int(float(v))
    except Exception:
        return int(default)

def fmt_inr(v) -> str:
    return f"₹{fnum(v):,.2f}"

def fmt_pct(v) -> str:
    return f"{fnum(v):.2f}%"

def fmt_time(ms) -> str:
    if ms in (None, "", 0, "0"):
        return "-"
    try:
        return datetime.fromtimestamp(int(float(ms)) / 1000, tz=timezone.utc).isoformat()
    except Exception:
        return str(ms)

def status_from_state(state: dict) -> str:
    return "LONG" if state.get("position") else "FLAT"

def latest_equity(state: dict, snap: dict) -> float:
    if snap:
        return fnum(snap.get("equity_inr"), state.get("cash_inr", state.get("starting_capital_inr", 0)))
    return fnum(state.get("cash_inr", state.get("starting_capital_inr", 0)))

def strategy_data(s: dict) -> dict:
    slug = s["slug"]
    branch = s["branch"]
    state = read_json(branch, f"data/{slug}_state.json")
    snap = read_csv_last(branch, f"data/{slug}_snapshots.csv")
    order = read_csv_last(branch, f"data/{slug}_orders.csv")
    trade = read_csv_last(branch, f"data/{slug}_trades.csv")
    signal = read_csv_last(branch, f"data/{slug}_signals.csv")
    start = fnum(state.get("starting_capital_inr", 100000))
    equity = latest_equity(state, snap)
    return {
        **s,
        "state": state,
        "snap": snap,
        "order": order,
        "trade": trade,
        "signal": signal,
        "start": start,
        "equity": equity,
        "pnl": equity - start,
        "return_pct": ((equity / start) - 1) * 100 if start else 0.0,
    }

def render_detail(d: dict) -> list[str]:
    state, snap, order, trade, signal = d["state"], d["snap"], d["order"], d["trade"], d["signal"]
    pos = state.get("position")
    lines = [
        f"## {d['name']}",
        "",
        f"- Status: **{status_from_state(state)}**",
        f"- Starting capital: **{fmt_inr(d['start'])}**",
        f"- Current equity: **{fmt_inr(d['equity'])}**",
        f"- Total P&L: **{fmt_inr(d['pnl'])} ({fmt_pct(d['return_pct'])})**",
        f"- Cash: **{fmt_inr(state.get('cash_inr', 0))}**",
        f"- Realized P&L: **{fmt_inr(state.get('realized_pnl_inr', 0))}**",
        f"- Unrealized P&L: **{fmt_inr(snap.get('unrealized_pnl_inr', 0) if snap else 0)}**",
        f"- Closed trades: **{fint(state.get('closed_trades', 0))}** | Wins: **{fint(state.get('wins', 0))}** | Losses: **{fint(state.get('losses', 0))}**",
        f"- Max drawdown: **{fmt_pct(state.get('max_drawdown_pct', 0))}**",
        f"- Last processed candle: `{fmt_time(state.get('last_processed_close_time'))}`",
        "",
        "### Open position",
        "",
    ]
    if pos:
        lines += [
            f"- Entry time: `{fmt_time(pos.get('entry_time'))}`",
            f"- Entry price (quote): **{fnum(pos.get('entry_price_quote')):,.6f}**",
            f"- Entry price (INR): **{fmt_inr(pos.get('entry_price_inr'))}**",
            f"- Quantity: **{fnum(pos.get('qty')):.10f}**",
            f"- Entry capital: **{fmt_inr(pos.get('entry_cost_inr'))}**",
        ]
    else:
        lines.append("_No open position._")

    lines += ["", "### Latest signal / order / closed trade", ""]
    if signal:
        lines += [
            f"- Latest signal: **{signal.get('signal', '-')}**",
            f"- Signal confirmation: `{fmt_time(signal.get('confirmed_close_time'))}`",
            f"- Order-block high / avg / low: **{fnum(signal.get('ob_high')):,.6f} / {fnum(signal.get('ob_avg')):,.6f} / {fnum(signal.get('ob_low')):,.6f}**",
        ]
    else:
        lines.append("- Latest signal: **None recorded yet**")

    if order:
        lines += [
            f"- Latest executed order: **{order.get('side', '-')}** on **{order.get('signal', '-')}**",
            f"- Order time: `{fmt_time(order.get('close_time'))}`",
            f"- Order value: **{fmt_inr(order.get('gross_notional_inr'))}**",
            f"- Order price (INR): **{fmt_inr(order.get('price_inr'))}**",
        ]
    else:
        lines.append("- Latest executed order: **None yet**")

    if trade:
        lines += [
            f"- Latest closed trade P&L: **{fmt_inr(trade.get('net_pnl_inr'))} ({fmt_pct(trade.get('return_pct'))})**",
            f"- Closed trade exit time: `{fmt_time(trade.get('exit_time'))}`",
        ]
    else:
        lines.append("- Latest closed trade: **None yet**")

    lines += [
        "",
        f"[Open {d['name']} branch report](https://github.com/rahulrtk74747474-glitch/Scraping_and_testing/blob/{d['branch']}/reports/{d['slug']}_latest.md)",
        "",
    ]
    return lines

def main() -> None:
    data = [strategy_data(s) for s in STRATEGIES]
    total_start = sum(d["start"] for d in data)
    total_equity = sum(d["equity"] for d in data)
    total_pnl = total_equity - total_start
    total_ret = ((total_equity / total_start) - 1) * 100 if total_start else 0.0
    now = datetime.now(timezone.utc)

    lines = [
        "# Combined Order Block 15m Paper-Trading Report",
        "",
        f"_Automatically refreshed after any NIFTY / BANKNIFTY / BTCUSDT / XAUUSDT strategy workflow completes. Generated {now.isoformat()}._",
        "",
        "## Combined summary",
        "",
        f"- Total starting paper capital: **{fmt_inr(total_start)}**",
        f"- Combined current equity: **{fmt_inr(total_equity)}**",
        f"- Combined P&L: **{fmt_inr(total_pnl)} ({fmt_pct(total_ret)})**",
        "",
        "| Strategy | Status | Starting | Equity | P&L | Return | Closed trades | Last signal |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for d in data:
        sig = d["signal"].get("signal", "-") if d["signal"] else "-"
        lines.append(
            f"| {d['name']} | {status_from_state(d['state'])} | {fmt_inr(d['start'])} | {fmt_inr(d['equity'])} | "
            f"{fmt_inr(d['pnl'])} | {fmt_pct(d['return_pct'])} | {fint(d['state'].get('closed_trades',0))} | {sig} |"
        )

    lines += [
        "",
        "---",
        "",
    ]
    for d in data:
        lines += render_detail(d)
        lines += ["---", ""]

    lines += [
        "Paper trading only. No real broker or exchange orders are placed by these four Order Block systems.",
        "",
    ]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
