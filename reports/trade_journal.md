# NIFTY SMC 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **1**
- Profits / losses: **1 / 0**
- Net realized P&L in journal: **₹51.50**
- Average return per closed trade: **0.1030%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-23 14:59:59 IST | NIFTY | LONG | PROFIT | ₹51.50 | 0.1030% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |

## Full trade details

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
