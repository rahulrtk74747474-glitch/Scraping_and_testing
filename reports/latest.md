# Vertex 500 Paper Trader — Latest Report

**As of:** 2026-10-09

## Portfolio

- Equity (estimated liquidation value): **₹100,321.99**
- Cash: **₹59,167.24**
- Total profit/loss: **₹321.99 (0.32%)**
- Realized P&L: **₹1,089.83**
- Unrealized P&L estimate: **₹-767.84**
- Open positions: **4**
- Max drawdown observed: **0.92%**
- Max capital deployed: **₹41,922.59**

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
| BAJAJ-AUTO | 2026-10-07   |       9884    |            9884      |     1 |        9778    |            9895.73 |                   0 |                     0    |                  -143.22 |          -1.4473 |
| BBTC       | 2026-10-08   |       1224.6  |            1224.6    |     8 |        1222.1  |            9808.44 |                   0 |                     0    |                   -57.13 |          -0.5825 |
| SJVN       | 2026-10-01   |         57.91 |              57.2861 |   242 |          55.27 |           13879.7  |                   4 |                  3902.72 |                  -533.6  |          -3.8445 |
| ZFCVINDIA  | 2026-10-09   |       2082.2  |            2082.2    |     4 |        2082.2  |            8338.7  |                   0 |                     0    |                   -33.89 |          -0.4064 |

## Notes

- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.
- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.
- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.
- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.
