# NIFTY SMC 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **2**
- Profits / losses: **1 / 1**
- Net realized P&L in journal: **₹-228.44**
- Average return per closed trade: **-0.5012%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-28 10:29:59 IST | NIFTY | LONG | LOSS | ₹-279.94 | -1.1054% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |
| 2 | 2026-09-23 14:59:59 IST | NIFTY | LONG | PROFIT | ₹51.50 | 0.1030% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |

## Full trade details

### Trade 2 — LOSS — NIFTY

- Trade ID: `SMC_NIFTY-2-1790571599999`
- Strategy: **NIFTY SMC Clean Wave major swings**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-25 11:59:59 IST**
- Entry signal: **CONFIRMED_PIVOT_LOW_BUY**
- Why entry was taken: A confirmed major pivot low generated the BUY side of the SMC major-swing strategy. Position size follows the configured restore/50%/12.5% ladder rules.
- Entry price: **₹23,098.0362**
- Quantity: **1.0963417838362193**
- Entry value/cost: **₹25,323.34**
- Stop: **Not used — this strategy reduces/exits on confirmed opposite major swings.**
- Target: **Not fixed — SELL decisions come from confirmed pivot-high signals.**
- Exit time: **2026-09-28 10:29:59 IST**
- Exit signal: **CONFIRMED_PIVOT_HIGH_SELL**
- Why position was closed/reduced: A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY.
- Exit price: **₹22,842.6992**
- Exit value/proceeds: **₹25,043.41**
- Gross P&L: **-**
- Fees/charges: **₹0.00**
- Net P&L: **₹-279.94**
- Profit/Loss percentage: **-1.1054%**
- Holding period: **2d 22h 30m**
- Notes: SMC uses scale-in/scale-out sizing. This row is a realized SELL slice; exit ladder step=0, fraction=%. A position can remain partly open after this journal row.

### Trade 1 — PROFIT — NIFTY

- Trade ID: `SMC_NIFTY-1-1790155799999`
- Strategy: **NIFTY SMC Clean Wave major swings**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-23 10:29:59 IST**
- Entry signal: **CONFIRMED_PIVOT_LOW_BUY**
- Why entry was taken: A confirmed major pivot low generated the BUY side of the SMC major-swing strategy. Position size follows the configured restore/50%/12.5% ladder rules.
- Entry price: **₹23,398.3496**
- Quantity: **2.1369028514714787**
- Entry value/cost: **₹50,000.00**
- Stop: **Not used — this strategy reduces/exits on confirmed opposite major swings.**
- Target: **Not fixed — SELL decisions come from confirmed pivot-high signals.**
- Exit time: **2026-09-23 14:59:59 IST**
- Exit signal: **CONFIRMED_PIVOT_HIGH_SELL**
- Why position was closed/reduced: A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY.
- Exit price: **₹23,422.4492**
- Exit value/proceeds: **₹50,051.50**
- Gross P&L: **-**
- Fees/charges: **₹0.00**
- Net P&L: **₹51.50**
- Profit/Loss percentage: **0.1030%**
- Holding period: **0d 4h 30m**
- Notes: SMC uses scale-in/scale-out sizing. This row is a realized SELL slice; exit ladder step=0, fraction=%. A position can remain partly open after this journal row.
