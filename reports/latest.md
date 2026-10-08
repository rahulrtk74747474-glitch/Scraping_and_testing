# Vertex 500 Paper Trader — Latest Report

**As of:** 2026-10-08

## Portfolio

- Equity (estimated liquidation value): **₹100,292.15**
- Cash: **₹69,708.51**
- Total profit/loss: **₹292.15 (0.29%)**
- Realized P&L: **₹1,089.83**
- Unrealized P&L estimate: **₹-797.68**
- Open positions: **3**
- Max drawdown observed: **0.64%**
- Max capital deployed: **₹35,539.37**

## Closed-trade statistics

- Closed trades: **6**
- Wins / losses: **6 / 0**
- Win rate: **100.00%**
- Max winning streak: **6**
- Max losing streak: **0**
- Average net P&L/trade: **₹181.64**
- Average net return/trade: **2.01%**
- Profit factor: **N/A**
- Max averaging amount added in a closed trade: **₹0.00**

## Open positions

| symbol     | entry_date   |   entry_price |   weighted_avg_price |   qty |   latest_close |   capital_in_trade |   average_add_count |   average_added_notional |   unrealized_net_pnl_est |   return_pct_est |
|:-----------|:-------------|--------------:|---------------------:|------:|---------------:|-------------------:|--------------------:|-------------------------:|-------------------------:|-----------------:|
| SJVN       | 2026-10-01   |         57.91 |              57.5375 |   207 |          54.24 |           11924.4  |                   2 |                  1949.74 |                  -723.72 |          -6.0692 |
| BAJAJ-AUTO | 2026-10-08   |       9637    |            9637      |     1 |        9637    |            9648.46 |                   0 |                     0    |                   -36.81 |          -0.3815 |
| BBTC       | 2026-10-08   |       1224.6  |            1224.6    |     8 |        1224.6  |            9808.44 |                   0 |                     0    |                   -37.15 |          -0.3788 |

## Notes

- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.
- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.
- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.
- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.
