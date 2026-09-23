# BANKNIFTY SMC 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **1**
- Profits / losses: **1 / 0**
- Net realized P&L in journal: **₹39.23**
- Average return per closed trade: **0.0785%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-23 13:44:59 IST | BANKNIFTY | LONG | PROFIT | ₹39.23 | 0.0785% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |

## Full trade details

### Trade 1 — PROFIT — BANKNIFTY

- Trade ID: `SMC_BANKNIFTY-1-1790151299999`
- Strategy: **BANKNIFTY SMC Clean Wave major swings**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-23 10:29:59 IST**
- Entry signal: **CONFIRMED_PIVOT_LOW_BUY**
- Why entry was taken: A confirmed major pivot low generated the BUY side of the SMC major-swing strategy. Position size follows the configured restore/50%/12.5% ladder rules.
- Entry price: **₹56,523.1484**
- Quantity: **0.8845933282589006**
- Entry value/cost: **₹50,000.00**
- Stop: **Not used — this strategy reduces/exits on confirmed opposite major swings.**
- Target: **Not fixed — SELL decisions come from confirmed pivot-high signals.**
- Exit time: **2026-09-23 13:44:59 IST**
- Exit signal: **CONFIRMED_PIVOT_HIGH_SELL**
- Why position was closed/reduced: A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY.
- Exit price: **₹56,567.5000**
- Exit value/proceeds: **₹50,039.23**
- Gross P&L: **-**
- Fees/charges: **₹0.00**
- Net P&L: **₹39.23**
- Profit/Loss percentage: **0.0785%**
- Holding period: **0d 3h 15m**
- Notes: SMC uses scale-in/scale-out sizing. This row is a realized SELL slice; exit ladder step=0, fraction=%. A position can remain partly open after this journal row.
