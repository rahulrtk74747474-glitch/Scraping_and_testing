# Rahul-606569 Friday 3:15 PM — Paper Backtest Report

**As of market date:** 2026-09-25

## Portfolio

- External capital contributed: **₹329,263.82**
- Estimated liquidation equity: **₹328,363.40**
- Cash: **₹0.00**
- Total profit/loss: **₹-900.42 (-0.27%)**
- Realized P&L: **₹0.00**
- Unrealized P&L estimate: **₹-900.42**
- Open positions: **11**
- Max drawdown observed (return-based): **0.27%**
- Max capital deployed: **₹329,263.82**

## Closed-trade statistics

- Closed trades: **0**
- Wins / losses: **0 / 0**
- Win rate: **0.00%**
- Max winning streak: **0**
- Max losing streak: **0**
- Average net P&L/trade: **₹0.00**
- Average net return/trade: **0.00%**
- Profit factor: **N/A**
- Max averaging amount added in a closed trade: **₹0.00**

## Open positions

| symbol     | entry_date   |   entry_price |   weighted_avg_price |    qty |   latest_close |   capital_in_trade |   average_add_count |   average_added_notional |   unrealized_net_pnl_est |   return_pct_est |
|:-----------|:-------------|--------------:|---------------------:|-------:|---------------:|-------------------:|--------------------:|-------------------------:|-------------------------:|-----------------:|
| AVANTIFEED | 2026-09-25   |        753.15 |               753.15 |     39 |         753.15 |            29407.7 |                   0 |                        0 |                   -80.69 |          -0.2744 |
| SUPREME    | 2026-09-25   |         31.39 |                31.39 |    955 |          31.39 |            30013   |                   0 |                        0 |                   -82.04 |          -0.2733 |
| ACL        | 2026-09-25   |         42.63 |                42.63 |    703 |          42.63 |            30004.5 |                   0 |                        0 |                   -82.02 |          -0.2734 |
| RTNPOWER   | 2026-09-25   |          7    |                 7    |   4285 |           7    |            30030.6 |                   0 |                        0 |                   -82.08 |          -0.2733 |
| ASALCBR    | 2026-09-25   |        644.95 |               644.95 |     46 |         644.95 |            29702.9 |                   0 |                        0 |                   -81.35 |          -0.2739 |
| HDIL       | 2026-09-25   |          1.45 |                 1.45 |  20689 |           1.45 |            30034.7 |                   0 |                        0 |                   -82.08 |          -0.2733 |
| RAJVIR     | 2026-09-25   |          5.21 |                 5.21 |   5758 |           5.21 |            30034.8 |                   0 |                        0 |                   -82.08 |          -0.2733 |
| AGIIL      | 2026-09-25   |        264.55 |               264.55 |    113 |         264.55 |            29929.6 |                   0 |                        0 |                   -81.84 |          -0.2734 |
| FCONSUMER  | 2026-09-25   |          0.22 |                 0.22 | 136363 |           0.22 |            30035.5 |                   0 |                        0 |                   -82.08 |          -0.2733 |
| DIL        | 2026-09-25   |          0.65 |                 0.65 |  46153 |           0.65 |            30035.1 |                   0 |                        0 |                   -82.08 |          -0.2733 |
| NAGAFERT   | 2026-09-25   |          1.77 |                 1.77 |  16949 |           1.77 |            30035.3 |                   0 |                        0 |                   -82.08 |          -0.2733 |

## Strategy rules implemented

- Scanner: https://chartink.com/screener/rahul-606569
- Decision cycle: every Friday at **3:15 PM IST**.
- New scanner stock: buy the largest whole-share quantity whose gross value is **not above ₹30,000**.
- Existing position: on the next Friday, if price is **above the original entry price**, sell the full accumulated quantity.
- If price is not above the original entry price, add the largest whole-share quantity whose value is within **10% of the initial invested notional**.
- Held stocks are checked every Friday even if they are no longer present in the scanner.
- A stock already held is not given another ₹30,000 entry; it follows the exit/10% averaging rule.
- No fixed total account size was specified, so this branch uses capital-on-demand. Return is calculated against cumulative external capital actually contributed.
- Zerodha equity-delivery charges are estimated by the existing project charge model.

_Paper trading/backtest only; no real broker order is placed._
