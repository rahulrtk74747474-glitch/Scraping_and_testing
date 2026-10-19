# Vertex 500 Paper Trader — Latest Report

**As of:** 2026-10-19

## Portfolio

- Equity (estimated liquidation value): **₹99,744.71**
- Cash: **₹64,202.16**
- Total profit/loss: **₹-255.29 (-0.26%)**
- Realized P&L: **₹1,842.17**
- Unrealized P&L estimate: **₹-2,097.46**
- Open positions: **3**
- Max drawdown observed: **1.90%**
- Max capital deployed: **₹41,922.59**

## Closed-trade statistics

- Closed trades: **9**
- Wins / losses: **9 / 0**
- Win rate: **100.00%**
- Max winning streak: **9**
- Max losing streak: **0**
- Average net P&L/trade: **₹204.69**
- Average net return/trade: **2.23%**
- Profit factor: **N/A**
- Max averaging amount added in a closed trade: **₹0.00**

## Open positions

| symbol     | entry_date   |   entry_price |   weighted_avg_price |   qty |   latest_close |   capital_in_trade |   average_add_count |   average_added_notional |   unrealized_net_pnl_est |   return_pct_est |
|:-----------|:-------------|--------------:|---------------------:|------:|---------------:|-------------------:|--------------------:|-------------------------:|-------------------------:|-----------------:|
| CAPLIPOINT | 2026-10-15   |       2301.8  |            2301.8    |     4 |        2258.8  |            9218.13 |                   0 |                     0    |                  -207.65 |          -2.2526 |
| SJVN       | 2026-10-01   |         57.91 |              56.5578 |   330 |          51.11 |           18686.3  |                   9 |                  8703.56 |                 -1852.83 |          -9.9155 |
| EXIDEIND   | 2026-10-19   |        360.15 |             360.15   |    27 |         360.15 |            9735.6  |                   0 |                     0    |                   -36.98 |          -0.3798 |

## Notes

- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.
- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.
- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.
- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.
