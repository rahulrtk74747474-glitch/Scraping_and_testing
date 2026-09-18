from __future__ import annotations

import os
from datetime import datetime, timezone
from .btc_market import INTERVAL_MS, fetch_klines_from, fetch_recent_klines
from .btc_paper import DATA, append_csv, load_state, mark_equity, process_events, save_state, write_report
from .btc_strategy import StrategyParams, compute_events

WARMUP_BARS = 500

def main() -> None:
    starting_capital = float(os.getenv("BTC_STARTING_CAPITAL", "100"))
    fee_rate = float(os.getenv("BTC_FEE_RATE", "0.001"))
    state = load_state(starting_capital)
    last_processed = state.get("last_processed_close_time")

    if last_processed is None:
        bars = fetch_recent_klines(limit=1000)
    else:
        start_ms = max(0, int(last_processed) - WARMUP_BARS * INTERVAL_MS)
        bars = fetch_klines_from(start_ms)
        if len(bars) < 300:
            bars = fetch_recent_klines(limit=1000)

    if not bars:
        raise RuntimeError("No closed BTCUSDT 15m candles returned by Binance public market-data API.")

    newest = bars[-1]
    if last_processed is None:
        state["last_processed_close_time"] = newest.close_time
        save_state(state)
        append_csv(DATA / "btc_snapshots.csv", [{
            "close_time": newest.close_time,
            "utc": datetime.fromtimestamp(newest.close_time/1000, tz=timezone.utc).isoformat(),
            "price": newest.close, "balance": state["balance"], "equity": state["balance"],
            "unrealized_pnl": 0.0, "open_position": "", "note": "initialized_no_historical_replay",
        }], ["close_time","utc","price","balance","equity","unrealized_pnl","open_position","note"])
        write_report(state, newest.close, newest.close_time, fee_rate)
        print(f"Initialized BTCUSDT paper trader at {newest.close_time}; next new signal will be traded.")
        return

    if newest.close_time <= int(last_processed):
        print("No new completed 15m candle yet.")
        return

    events = compute_events(bars, StrategyParams())
    new_events = [e for e in events if int(e["close_time"]) > int(last_processed)]
    signal_rows = [e for e in new_events if e["event"] in {"sweep", "dist_confirmed", "outcome"}]
    orders, trades = process_events(state, new_events, fee_rate=fee_rate)

    state["last_processed_close_time"] = newest.close_time
    equity, unreal = mark_equity(state, newest.close, fee_rate)
    peak = max(float(state.get("equity_peak", state["starting_capital"])), equity)
    state["equity_peak"] = peak
    dd = (peak - equity) / peak * 100.0 if peak > 0 else 0.0
    state["max_drawdown_pct"] = max(float(state.get("max_drawdown_pct", 0.0)), dd)
    save_state(state)

    append_csv(DATA / "btc_signals.csv", signal_rows,
               ["close_time","event","cycle","side","dir","price","entry","stop","target","rr","result","exit","r"])
    append_csv(DATA / "btc_orders.csv", orders,
               ["close_time","cycle","event","side","price","qty","notional","fee","balance","stop","target"])
    append_csv(DATA / "btc_trades.csv", trades,
               ["cycle","dir","entry_time","exit_time","entry","exit","stop","target","qty","gross_pnl","fees","net_pnl","return_pct","result","r","balance_after"])
    append_csv(DATA / "btc_snapshots.csv", [{
        "close_time": newest.close_time,
        "utc": datetime.fromtimestamp(newest.close_time/1000, tz=timezone.utc).isoformat(),
        "price": newest.close, "balance": state["balance"], "equity": equity, "unrealized_pnl": unreal,
        "open_position": (state.get("open_position") or {}).get("dir", ""), "note": "",
    }], ["close_time","utc","price","balance","equity","unrealized_pnl","open_position","note"])
    write_report(state, newest.close, newest.close_time, fee_rate)
    print(f"BTCUSDT processed through {newest.close_time}: events={len(new_events)} orders={len(orders)} trades={len(trades)} equity=${equity:.4f}")

if __name__ == "__main__":
    main()
