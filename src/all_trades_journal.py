from __future__ import annotations

import csv
import io
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "all_trades_journal.md"

BRANCHES = [
    ("Vertex Daily", "main"),
    ("Vertex 3:15", "vertex-315-paper"),
    ("Vertex 500 Daily", "vertex-500-paper"),
    ("Vertex 500 3:15", "vertex-500-315-paper"),
    ("Rahul-606569 Friday 3:15", "vertex-rahul-606569-friday-paper"),
    ("BTCUSDT 15m", "btcusdt-paper"),
    ("OB NIFTY 15m", "ob-nifty-15m-paper"),
    ("OB BANKNIFTY 15m", "ob-banknifty-15m-paper"),
    ("OB BTCUSDT 15m", "ob-btcusdt-15m-paper"),
    ("OB XAUUSDT 15m", "ob-xauusdt-15m-paper"),
    ("SMC NIFTY 15m", "smc-nifty-15m-paper"),
    ("SMC BANKNIFTY 15m", "smc-banknifty-15m-paper"),
    ("SMC BTCUSDT 4h", "smc-btcusdt-4h-paper"),
]


def _show(branch: str, path: str) -> str:
    p = subprocess.run(
        ["git", "show", f"origin/{branch}:{path}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    return p.stdout if p.returncode == 0 else ""


def _num(v) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def _money(v, cur: str) -> str:
    x = _num(v)
    return f"${x:,.4f}" if cur == "USD" else f"₹{x:,.2f}"


def main() -> None:
    rows: list[dict] = []
    for label, branch in BRANCHES:
        raw = _show(branch, "data/trade_journal.csv")
        if not raw.strip():
            continue
        for r in csv.DictReader(io.StringIO(raw)):
            r["source_branch"] = branch
            r["source_label"] = label
            rows.append(r)

    rows.sort(key=lambda r: (r.get("exit_time", ""), r.get("trade_id", "")), reverse=True)
    inr = sum(_num(r.get("net_pnl")) for r in rows if r.get("currency") == "INR")
    usd = sum(_num(r.get("net_pnl")) for r in rows if r.get("currency") == "USD")
    wins = sum(1 for r in rows if r.get("result") == "PROFIT")
    losses = sum(1 for r in rows if r.get("result") == "LOSS")

    lines = [
        "# All Strategies — Trade Journal",
        "",
        "_Aggregated automatically from each strategy branch. INR and USD results are kept separate._",
        "",
        "## Summary",
        "",
        f"- Closed trade records: **{len(rows)}**",
        f"- Profits / losses: **{wins} / {losses}**",
        f"- Net INR P&L: **₹{inr:,.2f}**",
        f"- Net USD P&L: **${usd:,.4f}**",
        "",
    ]
    if not rows:
        lines += ["_No journaled closed trades are available yet._", ""]
    else:
        lines += [
            "## All closed trades",
            "",
            "| Exit | Strategy | Symbol | Direction | Result | Net P&L | Return | Why closed |",
            "|---|---|---|---|---|---:|---:|---|",
        ]
        for r in rows:
            lines.append(
                f"| {r.get('exit_time','-')} | {r.get('source_label','-')} | {r.get('symbol','-')} | "
                f"{r.get('direction','-')} | {r.get('result','-')} | "
                f"{_money(r.get('net_pnl'), r.get('currency','INR'))} | {_num(r.get('return_pct')):.4f}% | "
                f"{r.get('exit_reason','-')} |"
            )
        lines += ["", "## Detailed journal", ""]
        for r in rows:
            cur = r.get("currency", "INR")
            lines += [
                f"### {r.get('source_label','-')} — {r.get('symbol','-')} — {r.get('result','-')}",
                "",
                f"- Trade ID: `{r.get('trade_id','-')}`",
                f"- Branch: `{r.get('source_branch','-')}`",
                f"- Entry: **{r.get('entry_time','-')}** at **{r.get('entry_price','-')}**",
                f"- Entry signal: **{r.get('entry_signal','-')}**",
                f"- Why taken: {r.get('entry_reason','-')}",
                f"- Stop: **{r.get('stop','-')}**",
                f"- Target: **{r.get('target','-')}**",
                f"- Exit: **{r.get('exit_time','-')}** at **{r.get('exit_price','-')}**",
                f"- Exit signal: **{r.get('exit_signal','-')}**",
                f"- Why closed/reduced: {r.get('exit_reason','-')}",
                f"- Quantity: **{r.get('quantity','-')}**",
                f"- Gross P&L: **{_money(r.get('gross_pnl'), cur) if r.get('gross_pnl') not in ('',None) else '-'}**",
                f"- Fees/charges: **{_money(r.get('fees'), cur) if r.get('fees') not in ('',None) else '-'}**",
                f"- Net P&L: **{_money(r.get('net_pnl'), cur)}**",
                f"- Profit/Loss percentage: **{_num(r.get('return_pct')):.4f}%**",
                f"- Holding period: **{r.get('holding_period','-')}**",
                f"- Notes: {r.get('notes','-')}",
                "",
            ]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
