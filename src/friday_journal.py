from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
FIELDS = [
    "trade_id", "strategy", "symbol", "timeframe", "currency", "direction",
    "entry_time", "exit_time", "entry_signal", "entry_reason",
    "exit_signal", "exit_reason", "entry_price", "exit_price", "quantity",
    "entry_value", "exit_value", "stop", "target", "gross_pnl", "fees",
    "net_pnl", "return_pct", "result", "holding_period", "notes",
]


def _read(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _num(v, default=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return float(default)


def write_friday_journal() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    trades = _read(DATA / "trades.csv")
    signals = _read(DATA / "signals.csv")
    sig_map = {(r.get("date"), str(r.get("symbol", "")).upper()): r for r in signals}

    rows = []
    for t in trades:
        symbol = str(t.get("symbol", "")).upper()
        sig = sig_map.get((t.get("entry_date", ""), symbol), {})
        pnl = _num(t.get("net_pnl"))
        rows.append({
            "trade_id": f"FRIDAY606569-{symbol}-{t.get('entry_date','')}-{t.get('exit_date','')}",
            "strategy": "Rahul-606569 Friday 3:15 PM",
            "symbol": symbol,
            "timeframe": "Weekly Friday 15:15 decision cycle",
            "currency": "INR",
            "direction": "LONG",
            "entry_time": t.get("entry_date", ""),
            "exit_time": t.get("exit_date", ""),
            "entry_signal": "CHARTINK_RAHUL_606569",
            "entry_reason": (
                "Stock appeared in the Rahul-606569 Chartink scanner at the Friday decision cycle."
                + (f" Scanner name: {sig.get('name')}." if sig.get("name") else "")
            ),
            "exit_signal": "FRIDAY_PRICE_ABOVE_ORIGINAL_ENTRY",
            "exit_reason": "At a later Friday 3:15 PM check, price was above the original entry price, so all accumulated shares were sold.",
            "entry_price": t.get("entry_price", ""),
            "exit_price": t.get("exit_price", ""),
            "quantity": t.get("qty", ""),
            "entry_value": t.get("buy_turnover", ""),
            "exit_value": t.get("sell_turnover", ""),
            "stop": "Not used",
            "target": "First later Friday price above original entry price",
            "gross_pnl": t.get("gross_pnl", ""),
            "fees": t.get("total_charges", ""),
            "net_pnl": t.get("net_pnl", ""),
            "return_pct": t.get("return_pct", ""),
            "result": "PROFIT" if pnl > 0 else "LOSS" if pnl < 0 else "BREAKEVEN",
            "holding_period": f"{t.get('days_held','-')} day(s)",
            "notes": (
                f"Average-add count: {t.get('average_add_count','0')}; "
                f"average-added notional: ₹{_num(t.get('average_added_notional')):,.2f}; "
                f"max capital in trade: ₹{_num(t.get('max_capital_in_trade')):,.2f}."
            ),
        })

    with (DATA / "trade_journal.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows([{k: r.get(k, "") for k in FIELDS} for r in rows])

    total = sum(_num(r.get("net_pnl")) for r in rows)
    lines = [
        "# Rahul-606569 Friday 3:15 PM — Closed Trade Journal",
        "",
        f"- Closed trades: **{len(rows)}**",
        f"- Net realized P&L: **₹{total:,.2f}**",
        "",
    ]
    if not rows:
        lines += ["_No closed trades yet._", ""]
    else:
        lines += [
            "| Exit | Symbol | Result | Net P&L | Return |",
            "|---|---|---|---:|---:|",
        ]
        for r in reversed(rows):
            lines.append(
                f"| {r['exit_time']} | {r['symbol']} | {r['result']} | "
                f"₹{_num(r['net_pnl']):,.2f} | {_num(r['return_pct']):.4f}% |"
            )
        lines.append("")

    (REPORTS / "trade_journal.md").write_text("\n".join(lines), encoding="utf-8")
