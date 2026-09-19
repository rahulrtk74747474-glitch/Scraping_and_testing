from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import yaml
from .chartink import fetch_chartink_signals
from .engine import StrategyConfig, mark_to_market, process_day
from .market_data import latest_daily_closes, latest_market_date
from .report import write_markdown_report
from .storage import DATA_DIR, append_csv, load_state, save_state
from .trade_journal import write_trade_journal

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config.yaml"


def load_config() -> dict:
    path = CONFIG_PATH if CONFIG_PATH.exists() else ROOT / "config.example.yaml"
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def main() -> None:
    config = load_config()
    tz = ZoneInfo(config.get("timezone", "Asia/Kolkata"))
    today = datetime.now(tz).date()
    market_date = latest_market_date()

    if config.get("skip_if_market_not_open_today", True) and market_date != today:
        print(f"Skipping: latest NSE market date is {market_date}, today is {today}.")
        return

    trade_date = market_date.isoformat()
    cfg = StrategyConfig(
        starting_capital=float(config.get("starting_capital", 100000)),
        per_stock_target=float(config.get("per_stock_target", 10000)),
        average_add_pct_of_initial=float(config.get("average_add_pct_of_initial", 0.10)),
    )
    state = load_state(cfg.starting_capital)

    # Prevent duplicate signals/orders/averaging when a manual workflow is re-run on the same market day.
    if state.get("last_run_date") == trade_date:
        write_trade_journal("vertex")
        print(f"Already processed market date {trade_date}; no changes made.")
        return

    signals = fetch_chartink_signals()
    signal_rows = [
        {
            "date": trade_date,
            "symbol": s["symbol"],
            "name": s["name"],
            "chartink_close": s["close"],
            "change_pct": s.get("change_pct"),
            "volume": s.get("volume"),
        }
        for s in signals
    ]

    symbols_for_prices = set(state.get("positions", {}).keys())
    symbols_for_prices.update(s["symbol"] for s in signals)
    closes = latest_daily_closes(symbols_for_prices)

    # Chartink itself supplies the signal-day close, so use it if Yahoo has not published the symbol yet.
    for s in signals:
        if s["symbol"] not in closes and float(s.get("close") or 0) > 0:
            closes[s["symbol"]] = {
                "date": market_date,
                "open": s["close"],
                "high": s["close"],
                "low": s["close"],
                "close": s["close"],
            }

    state, orders, closed_trades, skipped = process_day(
        state, signals, closes, trade_date, cfg
    )
    open_rows, metrics = mark_to_market(state, closes)
    save_state(state)

    append_csv(
        DATA_DIR / "signals.csv",
        signal_rows,
        ["date", "symbol", "name", "chartink_close", "change_pct", "volume"],
    )
    append_csv(
        DATA_DIR / "orders.csv",
        orders,
        ["date", "symbol", "event", "side", "qty", "price", "turnover", "charges", "cash_flow"],
    )
    append_csv(
        DATA_DIR / "trades.csv",
        closed_trades,
        [
            "symbol", "entry_date", "exit_date", "entry_price", "exit_price", "qty",
            "buy_turnover", "sell_turnover", "buy_charges", "sell_charges",
            "total_charges", "gross_pnl", "net_pnl", "return_pct", "days_held",
            "average_add_count", "average_added_notional", "max_capital_in_trade",
        ],
    )
    append_csv(DATA_DIR / "skipped.csv", skipped, ["date", "symbol", "reason"])
    append_csv(
        DATA_DIR / "daily_snapshots.csv",
        [{"date": trade_date, **metrics}],
        [
            "date", "cash", "equity", "total_profit", "total_return_pct",
            "realized_pnl", "unrealized_pnl_est", "open_positions",
            "max_drawdown_pct", "max_capital_deployed",
        ],
    )
    stats = write_markdown_report(trade_date, metrics, open_rows)
    write_trade_journal("vertex")
    print(
        f"{trade_date}: signals={len(signals)}, orders={len(orders)}, "
        f"open={metrics['open_positions']}, equity={metrics['equity']:.2f}, "
        f"closed_trades={stats['closed_trades']}"
    )


if __name__ == "__main__":
    main()
