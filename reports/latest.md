# Vertex 500 Paper Trader — Latest Report

**As of:** 2026-10-01

## Portfolio

- Equity (estimated liquidation value): **₹99,937.97**
- Cash: **₹64,747.53**
- Total profit/loss: **₹-62.03 (-0.06%)**
- Realized P&L: **₹286.90**
- Unrealized P&L estimate: **₹-348.93**
- Open positions: **4**
- Max drawdown observed: **0.31%**
- Max capital deployed: **₹35,539.37**

## Closed-trade statistics

- Closed trades: **3**
- Wins / losses: **3 / 0**
- Win rate: **100.00%**
- Max winning streak: **3**
- Max losing streak: **0**
- Average net P&L/trade: **₹95.63**
- Average net return/trade: **1.04%**
- Profit factor: **N/A**
- Max averaging amount added in a closed trade: **₹0.00**

## Open positions

| symbol    | entry_date   |   entry_price |   weighted_avg_price |   qty |   latest_close |   capital_in_trade |   average_add_count |   average_added_notional |   unrealized_net_pnl_est |   return_pct_est |
|:----------|:-------------|--------------:|---------------------:|------:|---------------:|-------------------:|--------------------:|-------------------------:|-------------------------:|-----------------:|
| GRAVITA   | 2026-09-30   |       1447.4  |              1447.4  |     6 |        1412.6  |            8694.71 |                   0 |                        0 |                  -243.25 |          -2.7977 |
| SJVN      | 2026-10-01   |         57.91 |                57.91 |   172 |          57.91 |            9972.35 |                   0 |                        0 |                   -37.51 |          -0.3761 |
| CROMPTON  | 2026-10-01   |        202.7  |               202.7  |    49 |         202.7  |            9944.09 |                   0 |                        0 |                   -37.43 |          -0.3764 |
| EICHERMOT | 2026-10-01   |       6920    |              6920    |     1 |        6920    |            6928.22 |                   0 |                        0 |                   -30.74 |          -0.4437 |

## Notes

- Entry is modeled at the Chartink signal day's reported close, because that is the requested paper-trading rule.
- Exit is evaluated on the next or later completed daily candle and occurs only when close > original entry price.
- If close is not above original entry price, the engine attempts to add 10% of the initial invested notional, subject to remaining ₹1,00,000 portfolio cash.
- Zerodha charges are estimates for NSE equity delivery; actual contract notes can differ due to rounding/aggregation and future rate changes.
