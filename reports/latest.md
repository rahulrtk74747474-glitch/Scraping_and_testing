# Vertex 500 Paper Trader — Latest Report

**As of:** 2026-10-16

## Portfolio

- Equity (estimated liquidation value): **₹100,566.35**
- Cash: **₹75,577.10**
- Total profit/loss: **₹566.35 (0.57%)**
- Realized P&L: **₹1,550.00**
- Unrealized P&L estimate: **₹-983.65**
- Open positions: **2**
- Max drawdown observed: **0.80%**
- Max capital deployed: **₹35,539.37**

## Closed-trade statistics

- Closed trades: **9**
- Wins / losses: **9 / 0**
- Win rate: **100.00%**
- Max winning streak: **9**
- Max losing streak: **0**
- Average net P&L/trade: **₹172.22**
- Average net return/trade: **1.91%**
- Profit factor: **N/A**
- Max averaging amount added in a closed trade: **₹0.00**

## Open positions

| symbol     | entry_date   |   entry_price |   weighted_avg_price |   qty |   latest_close |   capital_in_trade |   average_add_count |   average_added_notional |   unrealized_net_pnl_est |   return_pct_est |
|:-----------|:-------------|--------------:|---------------------:|------:|---------------:|-------------------:|--------------------:|-------------------------:|-------------------------:|-----------------:|
| CAPLIPOINT | 2026-10-15   |       2301.8  |            2301.8    |     4 |        2301.3  |            9218.13 |                   0 |                     0    |                   -37.82 |          -0.4103 |
| SJVN       | 2026-10-01   |         57.91 |              56.9213 |   294 |          53.88 |           16754.8  |                   7 |                  6774.35 |                  -945.83 |          -5.6451 |

## Notes

- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.
- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.
- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.
- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.
