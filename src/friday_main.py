from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

from .chartink import fetch_chartink_signals
from .friday_engine import FridayStrategyConfig, mark_to_market, normalise_state, process_friday
from .friday_journal import write_friday_journal
from .friday_report import write_friday_report
from .market_data import latest_daily_closes, latest_market_date
from .storage import DATA_DIR, append_csv, load_state, save_state

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config.yaml"


def load_config() -> dict:
    path = CONFIG_PATH if CONFIG_PATH.exists() else ROOT / "config.example.yaml"
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _env_true(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "y", "on"}


def main() -> None:
    config = load_config()
    tz = ZoneInfo(config.get("timezone", "Asia/Kolkata"))
    today = datetime.now(tz).date()
    market_date = latest_market_date()
    allow_latest = _env_true("FRIDAY_ALLOW_LATEST_MARKET_DATE")

    if not allow_latest:
        if today.weekday() != 4:
            print(f"Skipping: today {today} is not Friday.")
            return
        if market_date != today:
            print(f"Skipping: latest NSE market date is {market_date}, today is {today}.")
            return

    trade_date = market_date.isoformat()
    cfg = FridayStrategyConfig(
        per_stock_target=float(config.get("per_stock_target", 30000)),
        average_add_pct_of_initial=float(config.get("average_add_pct_of_initial", 0.10)),
    )
    state = normalise_state(load_state(float(config.get("starting_capital", 0))))

    if state.get("last_run_date") == trade_date:
        write_friday_journal()
        print(f"Already processed market date {trade_date}; no duplicate orders made.")
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
    symbols_for_prices.update(str(s["symbol"]).upper().strip() for s in signals)
    closes = latest_daily_closes(symbols_for_prices)

    for s in signals:
        symbol = str(s["symbol"]).upper().strip()
        price = float(s.get("close") or 0)
        if price > 0:
            closes[symbol] = {
                "date": market_date,
                "open": price,
                "high": price,
                "low": price,
                "close": price,
            }

    state, orders, closed_trades, skipped = process_friday(
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
        [
            "date", "symbol", "event", "side", "qty", "price", "turnover",
            "charges", "cash_flow", "capital_injected",
        ],
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
        DATA_DIR / "position_snapshots.csv",
        [{"date": trade_date, **row} for row in open_rows],
        [
            "date", "symbol", "entry_date", "entry_price", "weighted_avg_price",
            "qty", "latest_close", "latest_price_date", "capital_in_trade",
            "average_add_count", "average_added_notional",
            "unrealized_net_pnl_est", "return_pct_est",
        ],
    )
    append_csv(
        DATA_DIR / "daily_snapshots.csv",
        [{"date": trade_date, **metrics}],
        [
            "date", "cash", "equity", "capital_contributed", "total_profit",
            "total_return_pct", "realized_pnl", "unrealized_pnl_est",
            "open_positions", "max_drawdown_pct", "max_capital_deployed",
        ],
    )

    stats = write_friday_report(trade_date, metrics, open_rows)
    write_friday_journal()
    print(
        f"{trade_date}: scanner_stocks={len(signals)}, orders={len(orders)}, "
        f"open={metrics['open_positions']}, contributed={metrics['capital_contributed']:.2f}, "
        f"equity={metrics['equity']:.2f}, closed_trades={stats['closed_trades']}"
    )


if __name__ == "__main__":
    main()
