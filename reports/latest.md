# Vertex 500 Paper Trader — Latest Report

**As of:** 2026-10-09

## Portfolio

- Equity (estimated liquidation value): **₹100,589.91**
- Cash: **₹70,126.28**
- Total profit/loss: **₹589.91 (0.59%)**
- Realized P&L: **₹1,193.88**
- Unrealized P&L estimate: **₹-603.97**
- Open positions: **3**
- Max drawdown observed: **0.64%**
- Max capital deployed: **₹35,539.37**

## Closed-trade statistics

- Closed trades: **7**
- Wins / losses: **7 / 0**
- Win rate: **100.00%**
- Max winning streak: **7**
- Max losing streak: **0**
- Average net P&L/trade: **₹170.55**
- Average net return/trade: **1.88%**
- Profit factor: **N/A**
- Max averaging amount added in a closed trade: **₹0.00**

## Open positions

| symbol    | entry_date   |   entry_price |   weighted_avg_price |   qty |   latest_close |   capital_in_trade |   average_add_count |   average_added_notional |   unrealized_net_pnl_est |   return_pct_est |
|:----------|:-------------|--------------:|---------------------:|------:|---------------:|-------------------:|--------------------:|-------------------------:|-------------------------:|-----------------:|
| BBTC      | 2026-10-08   |       1224.6  |            1224.6    |     8 |        1222.1  |            9808.44 |                   0 |                      0   |                   -57.13 |          -0.5825 |
| SJVN      | 2026-10-01   |         57.91 |              57.3561 |   225 |          55.27 |           12920.5  |                   3 |                   2944.6 |                  -512.95 |          -3.9701 |
| ZFCVINDIA | 2026-10-09   |       2082.2  |            2082.2    |     4 |        2082.2  |            8338.7  |                   0 |                      0   |                   -33.89 |          -0.4064 |

## Notes

- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.
- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.
- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.
- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.
