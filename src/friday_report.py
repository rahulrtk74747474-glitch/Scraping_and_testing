from __future__ import annotations

from pathlib import Path

import pandas as pd

from .report import trade_statistics
from .storage import DATA_DIR, REPORT_DIR


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    return pd.read_csv(path)


def write_friday_report(as_of: str, metrics: dict, open_rows: list[dict]) -> dict:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    trades = _read_csv(DATA_DIR / "trades.csv")
    stats = trade_statistics(trades)

    lines = [
        "# Rahul-606569 Friday 3:15 PM — Paper Backtest Report",
        "",
        f"**As of market date:** {as_of}",
        "",
        "## Portfolio",
        "",
        f"- External capital contributed: **₹{metrics['capital_contributed']:,.2f}**",
        f"- Estimated liquidation equity: **₹{metrics['equity']:,.2f}**",
        f"- Cash: **₹{metrics['cash']:,.2f}**",
        f"- Total profit/loss: **₹{metrics['total_profit']:,.2f} ({metrics['total_return_pct']:.2f}%)**",
        f"- Realized P&L: **₹{metrics['realized_pnl']:,.2f}**",
        f"- Unrealized P&L estimate: **₹{metrics['unrealized_pnl_est']:,.2f}**",
        f"- Open positions: **{metrics['open_positions']}**",
        f"- Max drawdown observed (return-based): **{metrics['max_drawdown_pct']:.2f}%**",
        f"- Max capital deployed: **₹{metrics['max_capital_deployed']:,.2f}**",
        "",
        "## Closed-trade statistics",
        "",
        f"- Closed trades: **{stats['closed_trades']}**",
        f"- Wins / losses: **{stats['wins']} / {stats['losses']}**",
        f"- Win rate: **{stats['win_rate_pct']:.2f}%**",
        f"- Max winning streak: **{stats['max_winning_streak']}**",
        f"- Max losing streak: **{stats['max_losing_streak']}**",
        f"- Average net P&L/trade: **₹{stats['avg_net_pnl']:,.2f}**",
        f"- Average net return/trade: **{stats['avg_return_pct']:.2f}%**",
        f"- Profit factor: **{stats['profit_factor'] if stats['profit_factor'] is not None else 'N/A'}**",
        f"- Max averaging amount added in a closed trade: **₹{stats['max_average_added']:,.2f}**",
        "",
        "## Open positions",
        "",
    ]

    if open_rows:
        df = pd.DataFrame(open_rows)
        keep = [
            "symbol", "entry_date", "entry_price", "weighted_avg_price", "qty",
            "latest_close", "capital_in_trade", "average_add_count",
            "average_added_notional", "unrealized_net_pnl_est", "return_pct_est",
        ]
        lines.append(df[keep].to_markdown(index=False))
    else:
        lines.append("_No open positions._")

    lines += [
        "",
        "## Strategy rules implemented",
        "",
        "- Scanner: https://chartink.com/screener/rahul-606569",
        "- Decision cycle: every Friday at **3:15 PM IST**.",
        "- New scanner stock: buy the largest whole-share quantity whose gross value is **not above ₹30,000**.",
        "- Existing position: on the next Friday, if price is **above the original entry price**, sell the full accumulated quantity.",
        "- If price is not above the original entry price, add the largest whole-share quantity whose value is within **10% of the initial invested notional**.",
        "- Held stocks are checked every Friday even if they are no longer present in the scanner.",
        "- A stock already held is not given another ₹30,000 entry; it follows the exit/10% averaging rule.",
        "- No fixed total account size was specified, so this branch uses capital-on-demand. Return is calculated against cumulative external capital actually contributed.",
        "- Zerodha equity-delivery charges are estimated by the existing project charge model.",
        "",
        "_Paper trading/backtest only; no real broker order is placed._",
        "",
    ]

    (REPORT_DIR / "latest.md").write_text("\n".join(lines), encoding="utf-8")
    return stats
