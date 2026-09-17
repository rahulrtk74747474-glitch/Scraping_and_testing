from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date

from .charges import equity_delivery_charges


@dataclass(frozen=True)
class StrategyConfig:
    starting_capital: float = 100000.0
    per_stock_target: float = 10000.0
    average_add_pct_of_initial: float = 0.10


def _days_held(entry_date: str, exit_date: str) -> int:
    return max((date.fromisoformat(exit_date) - date.fromisoformat(entry_date)).days, 0)


def target_initial_allocation(signal_count: int, cfg: StrategyConfig) -> float:
    if signal_count <= 0:
        return 0.0
    if signal_count <= 10:
        return cfg.per_stock_target
    return cfg.starting_capital / signal_count


def _max_affordable_qty(price: float, cash: float, requested_notional: float) -> int:
    if price <= 0 or cash <= 0 or requested_notional <= 0:
        return 0
    qty = int(math.floor(min(requested_notional, cash) / price))
    while qty > 0:
        turnover = qty * price
        charges = equity_delivery_charges(turnover, "buy")
        if turnover + charges.total <= cash + 1e-9:
            return qty
        qty -= 1
    return 0


def _buy_lot(symbol: str, price: float, requested_notional: float, cash: float, trade_date: str, event_type: str):
    qty = _max_affordable_qty(price, cash, requested_notional)
    if qty <= 0:
        return None, cash
    turnover = round(qty * price, 2)
    charges = equity_delivery_charges(turnover, "buy")
    cash_out = round(turnover + charges.total, 2)
    row = {"date": trade_date, "symbol": symbol, "event": event_type, "side": "BUY", "qty": qty, "price": round(price, 4), "turnover": turnover, "charges": charges.total, "cash_flow": -cash_out}
    return row, round(cash - cash_out, 2)


def _sell_all(position: dict, price: float, trade_date: str):
    qty = int(position["qty"])
    turnover = round(qty * price, 2)
    charges = equity_delivery_charges(turnover, "sell", include_dp=True)
    net_proceeds = round(turnover - charges.total, 2)
    total_buy_cost = float(position["total_buy_cost"])
    net_pnl = round(net_proceeds - total_buy_cost, 2)
    gross_pnl = round(turnover - float(position["total_buy_turnover"]), 2)
    trade = {"symbol": position["symbol"], "entry_date": position["entry_date"], "exit_date": trade_date, "entry_price": position["entry_price"], "exit_price": round(price, 4), "qty": qty, "buy_turnover": round(float(position["total_buy_turnover"]), 2), "sell_turnover": turnover, "buy_charges": round(float(position["total_buy_charges"]), 2), "sell_charges": charges.total, "total_charges": round(float(position["total_buy_charges"]) + charges.total, 2), "gross_pnl": gross_pnl, "net_pnl": net_pnl, "return_pct": round((net_pnl / total_buy_cost) * 100, 4) if total_buy_cost else 0.0, "days_held": _days_held(position["entry_date"], trade_date), "average_add_count": int(position["average_add_count"]), "average_added_notional": round(float(position["average_added_notional"]), 2), "max_capital_in_trade": round(total_buy_cost, 2)}
    order = {"date": trade_date, "symbol": position["symbol"], "event": "EXIT", "side": "SELL", "qty": qty, "price": round(price, 4), "turnover": turnover, "charges": charges.total, "cash_flow": net_proceeds}
    return order, net_proceeds, trade


def process_day(state: dict, signals: list[dict], closes: dict[str, dict], trade_date: str, cfg: StrategyConfig):
    if state.get("last_run_date") == trade_date:
        return state, [], [], []
    orders, closed_trades, skipped = [], [], []

    for symbol in list(state.get("positions", {}).keys()):
        position = state["positions"][symbol]
        bar = closes.get(symbol)
        if not bar or bar.get("date").isoformat() != trade_date:
            skipped.append({"date": trade_date, "symbol": symbol, "reason": "no_current_daily_close"})
            continue
        close = float(bar["close"])
        if trade_date > position["entry_date"] and close > float(position["entry_price"]):
            order, proceeds, trade = _sell_all(position, close, trade_date)
            state["cash"] = round(float(state["cash"]) + proceeds, 2)
            state["realized_pnl"] = round(float(state.get("realized_pnl", 0.0)) + trade["net_pnl"], 2)
            orders.append(order); closed_trades.append(trade); del state["positions"][symbol]
            continue
        if trade_date > position["entry_date"]:
            requested = float(position["initial_invested_notional"]) * cfg.average_add_pct_of_initial
            order, new_cash = _buy_lot(symbol, close, requested, float(state["cash"]), trade_date, "AVERAGE_ADD")
            if order:
                new_qty = int(position["qty"]) + int(order["qty"])
                position["qty"] = new_qty
                position["total_buy_turnover"] = round(float(position["total_buy_turnover"]) + order["turnover"], 2)
                position["total_buy_charges"] = round(float(position["total_buy_charges"]) + order["charges"], 2)
                position["total_buy_cost"] = round(float(position["total_buy_cost"]) - order["cash_flow"], 2)
                position["average_add_count"] = int(position["average_add_count"]) + 1
                position["average_added_notional"] = round(float(position["average_added_notional"]) + order["turnover"], 2)
                position["weighted_avg_price"] = round(float(position["total_buy_turnover"]) / new_qty, 4)
                state["cash"] = new_cash; orders.append(order)
            else:
                skipped.append({"date": trade_date, "symbol": symbol, "reason": "insufficient_cash_for_average"})

    fresh, seen = [], set()
    for sig in signals:
        symbol = str(sig.get("symbol", "")).upper().strip()
        if symbol and symbol not in seen and symbol not in state.get("positions", {}) and float(sig.get("close") or 0) > 0:
            seen.add(symbol); fresh.append(sig)

    target = target_initial_allocation(len(fresh), cfg)
    effective_target = min(target, float(state["cash"]) / len(fresh)) if fresh and target > 0 else 0.0
    for sig in fresh:
        symbol, price = sig["symbol"], float(sig["close"])
        order, new_cash = _buy_lot(symbol, price, effective_target, float(state["cash"]), trade_date, "ENTRY")
        if not order:
            skipped.append({"date": trade_date, "symbol": symbol, "reason": "insufficient_cash_for_entry"}); continue
        initial_notional = float(order["turnover"]); total_buy_cost = -float(order["cash_flow"])
        state["positions"][symbol] = {"symbol": symbol, "name": sig.get("name") or symbol, "entry_date": trade_date, "entry_price": round(price, 4), "weighted_avg_price": round(price, 4), "qty": int(order["qty"]), "initial_invested_notional": round(initial_notional, 2), "total_buy_turnover": round(initial_notional, 2), "total_buy_charges": round(float(order["charges"]), 2), "total_buy_cost": round(total_buy_cost, 2), "average_add_count": 0, "average_added_notional": 0.0}
        state["cash"] = new_cash; orders.append(order)

    deployed = sum(float(p["total_buy_cost"]) for p in state["positions"].values())
    state["max_capital_deployed"] = round(max(float(state.get("max_capital_deployed", 0.0)), deployed), 2)
    state["last_run_date"] = trade_date
    return state, orders, closed_trades, skipped


def mark_to_market(state: dict, closes: dict[str, dict]):
    open_rows, liquidation_value = [], 0.0
    for symbol, position in state.get("positions", {}).items():
        bar = closes.get(symbol)
        if not bar:
            price, price_date = float(position["weighted_avg_price"]), None
        else:
            price, price_date = float(bar["close"]), bar["date"].isoformat()
        turnover = int(position["qty"]) * price
        sell_charges = equity_delivery_charges(turnover, "sell", include_dp=True)
        net_liquidation = turnover - sell_charges.total; liquidation_value += net_liquidation
        net_unrealized = net_liquidation - float(position["total_buy_cost"])
        open_rows.append({"symbol": symbol, "entry_date": position["entry_date"], "entry_price": position["entry_price"], "weighted_avg_price": position["weighted_avg_price"], "qty": position["qty"], "latest_close": round(price, 4), "latest_price_date": price_date, "capital_in_trade": round(float(position["total_buy_cost"]), 2), "average_add_count": position["average_add_count"], "average_added_notional": round(float(position["average_added_notional"]), 2), "unrealized_net_pnl_est": round(net_unrealized, 2), "return_pct_est": round((net_unrealized / float(position["total_buy_cost"])) * 100, 4) if float(position["total_buy_cost"]) else 0.0})

    equity = round(float(state["cash"]) + liquidation_value, 2); starting = float(state["starting_capital"]); total_profit = round(equity - starting, 2)
    peak = max(float(state.get("equity_peak", starting)), equity); state["equity_peak"] = round(peak, 2)
    dd = ((peak - equity) / peak * 100) if peak > 0 else 0.0; state["max_drawdown_pct"] = round(max(float(state.get("max_drawdown_pct", 0.0)), dd), 4)
    metrics = {"cash": round(float(state["cash"]), 2), "equity": equity, "total_profit": total_profit, "total_return_pct": round(total_profit / starting * 100, 4) if starting else 0.0, "realized_pnl": round(float(state.get("realized_pnl", 0.0)), 2), "unrealized_pnl_est": round(sum(float(r["unrealized_net_pnl_est"]) for r in open_rows), 2), "open_positions": len(open_rows), "max_drawdown_pct": state["max_drawdown_pct"], "max_capital_deployed": round(float(state.get("max_capital_deployed", 0.0)), 2)}
    return open_rows, metrics
