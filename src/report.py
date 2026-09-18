from __future__ import annotations

from pathlib import Path
import pandas as pd
from .storage import DATA_DIR, REPORT_DIR


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    return pd.read_csv(path)


def trade_statistics(trades: pd.DataFrame) -> dict:
    if trades.empty:
        return {"closed_trades": 0, "wins": 0, "losses": 0, "win_rate_pct": 0.0, "max_winning_streak": 0, "max_losing_streak": 0, "avg_net_pnl": 0.0, "avg_return_pct": 0.0, "profit_factor": None, "max_average_added": 0.0}
    pnl = pd.to_numeric(trades["net_pnl"], errors="coerce").fillna(0.0); wins = pnl > 0; losses = pnl < 0
    max_win = max_loss = cur_win = cur_loss = 0
    for value in pnl:
        if value > 0: cur_win += 1; cur_loss = 0; max_win = max(max_win, cur_win)
        elif value < 0: cur_loss += 1; cur_win = 0; max_loss = max(max_loss, cur_loss)
        else: cur_win = cur_loss = 0
    gross_win = float(pnl[pnl > 0].sum()); gross_loss = abs(float(pnl[pnl < 0].sum()))
    return {"closed_trades": int(len(trades)), "wins": int(wins.sum()), "losses": int(losses.sum()), "win_rate_pct": round(float(wins.mean()) * 100, 2), "max_winning_streak": max_win, "max_losing_streak": max_loss, "avg_net_pnl": round(float(pnl.mean()), 2), "avg_return_pct": round(float(pd.to_numeric(trades["return_pct"], errors="coerce").fillna(0.0).mean()), 4), "profit_factor": round(gross_win / gross_loss, 4) if gross_loss > 0 else None, "max_average_added": round(float(pd.to_numeric(trades["average_added_notional"], errors="coerce").fillna(0.0).max()), 2)}


def write_markdown_report(as_of: str, metrics: dict, open_rows: list[dict]) -> dict:
    REPORT_DIR.mkdir(parents=True, exist_ok=True); trades = _read_csv(DATA_DIR / "trades.csv"); stats = trade_statistics(trades)
    lines = ["# Vertex 500 Paper Trader — Latest Report", "", f"**As of:** {as_of}", "", "## Portfolio", "", f"- Equity (estimated liquidation value): **₹{metrics['equity']:,.2f}**", f"- Cash: **₹{metrics['cash']:,.2f}**", f"- Total profit/loss: **₹{metrics['total_profit']:,.2f} ({metrics['total_return_pct']:.2f}%)**", f"- Realized P&L: **₹{metrics['realized_pnl']:,.2f}**", f"- Unrealized P&L estimate: **₹{metrics['unrealized_pnl_est']:,.2f}**", f"- Open positions: **{metrics['open_positions']}**", f"- Max drawdown observed: **{metrics['max_drawdown_pct']:.2f}%**", f"- Max capital deployed: **₹{metrics['max_capital_deployed']:,.2f}**", "", "## Closed-trade statistics", "", f"- Closed trades: **{stats['closed_trades']}**", f"- Wins / losses: **{stats['wins']} / {stats['losses']}**", f"- Win rate: **{stats['win_rate_pct']:.2f}%**", f"- Max winning streak: **{stats['max_winning_streak']}**", f"- Max losing streak: **{stats['max_losing_streak']}**", f"- Average net P&L/trade: **₹{stats['avg_net_pnl']:,.2f}**", f"- Average net return/trade: **{stats['avg_return_pct']:.2f}%**", f"- Profit factor: **{stats['profit_factor'] if stats['profit_factor'] is not None else 'N/A'}**", f"- Max averaging amount added in a closed trade: **₹{stats['max_average_added']:,.2f}**", "", "## Open positions", ""]
    if open_rows:
        df = pd.DataFrame(open_rows); keep = ["symbol", "entry_date", "entry_price", "weighted_avg_price", "qty", "latest_close", "capital_in_trade", "average_add_count", "average_added_notional", "unrealized_net_pnl_est", "return_pct_est"]; lines.append(df[keep].to_markdown(index=False))
    else: lines.append("_No open positions._")
    lines += ["", "## Notes", "", "- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.", "- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.", "- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.", "- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.", ""]
    (REPORT_DIR / "latest.md").write_text("\n".join(lines), encoding="utf-8"); return stats
