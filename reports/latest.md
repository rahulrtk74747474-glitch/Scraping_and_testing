# Vertex 500 Paper Trader — Latest Report

**As of:** 2026-09-29

## Portfolio

- Equity (estimated liquidation value): **₹99,960.36**
- Cash: **₹80,999.10**
- Total profit/loss: **₹-39.64 (-0.04%)**
- Realized P&L: **₹33.37**
- Unrealized P&L estimate: **₹-73.01**
- Open positions: **2**
- Max drawdown observed: **0.07%**
- Max capital deployed: **₹19,034.27**

## Closed-trade statistics

- Closed trades: **1**
- Wins / losses: **1 / 0**
- Win rate: **100.00%**
- Max winning streak: **1**
- Max losing streak: **0**
- Average net P&L/trade: **₹33.37**
- Average net return/trade: **0.42%**
- Profit factor: **N/A**
- Max averaging amount added in a closed trade: **₹0.00**

## Open positions

| symbol    | entry_date   |   entry_price |   weighted_avg_price |   qty |   latest_close |   capital_in_trade |   average_add_count |   average_added_notional |   unrealized_net_pnl_est |   return_pct_est |
|:----------|:-------------|--------------:|---------------------:|------:|---------------:|-------------------:|--------------------:|-------------------------:|-------------------------:|-----------------:|
| ICICIBANK | 2026-09-29   |       1292.2  |              1292.2  |     7 |        1292.2  |            9056.15 |                   0 |                        0 |                   -35.48 |          -0.3918 |
| SBFC      | 2026-09-29   |         84.46 |                84.46 |   118 |          84.46 |            9978.12 |                   0 |                        0 |                   -37.53 |          -0.3761 |

## Notes

- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.
- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.
- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.
- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.
