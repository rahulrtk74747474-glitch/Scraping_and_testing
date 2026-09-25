# BANKNIFTY SMC 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **2**
- Profits / losses: **1 / 1**
- Net realized P&L in journal: **₹13.65**
- Average return per closed trade: **-0.0110%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-25 12:44:59 IST | BANKNIFTY | LONG | LOSS | ₹-25.58 | -0.1006% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |
| 2 | 2026-09-23 13:44:59 IST | BANKNIFTY | LONG | PROFIT | ₹39.23 | 0.0785% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |

## Full trade details

### Trade 2 — LOSS — BANKNIFTY

- Trade ID: `SMC_BANKNIFTY-2-1790320499999`
- Strategy: **BANKNIFTY SMC Clean Wave major swings**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-24 12:29:59 IST**
- Entry signal: **CONFIRMED_PIVOT_LOW_BUY**
- Why entry was taken: A confirmed major pivot low generated the BUY side of the SMC major-swing strategy. Position size follows the configured restore/50%/12.5% ladder rules.
- Entry price: **₹55,595.7672**
- Quantity: **0.45742298452793023**
- Entry value/cost: **₹25,430.78**
- Stop: **Not used — this strategy reduces/exits on confirmed opposite major swings.**
- Target: **Not fixed — SELL decisions come from confirmed pivot-high signals.**
- Exit time: **2026-09-25 12:44:59 IST**
- Exit signal: **CONFIRMED_PIVOT_HIGH_SELL**
- Why position was closed/reduced: A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY.
- Exit price: **₹55,539.8516**
- Exit value/proceeds: **₹25,405.20**
- Gross P&L: **-**
- Fees/charges: **₹0.00**
- Net P&L: **₹-25.58**
- Profit/Loss percentage: **-0.1006%**
- Holding period: **1d 0h 15m**
- Notes: SMC uses scale-in/scale-out sizing. This row is a realized SELL slice; exit ladder step=0, fraction=%. A position can remain partly open after this journal row.

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
