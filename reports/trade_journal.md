# XAUUSDT Order Block 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **1**
- Profits / losses: **0 / 1**
- Net realized P&L in journal: **₹-753.24**
- Average return per closed trade: **-0.7532%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-23 10:59:59 IST | XAUUSDT | LONG | LOSS | ₹-753.24 | -0.7532% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.11179079269419598%. |

## Full trade details

### Trade 1 — LOSS — XAUUSDT

- Trade ID: `OB_XAUUSDT-1-1789992899999`
- Strategy: **XAUUSDT Order Block**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-21 17:44:59 IST**
- Entry signal: **BULLISH_OB**
- Why entry was taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.6163820793063561%.
- Entry price: **₹422,250.9490**
- Quantity: **0.2368259923143178**
- Entry value/cost: **₹100,000.00**
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit time: **2026-09-23 10:59:59 IST**
- Exit signal: **BEARISH_OB**
- Why position was closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.11179079269419598%.
- Exit price: **₹419,070.3719**
- Exit value/proceeds: **₹99,246.76**
- Gross P&L: **₹-753.24**
- Fees/charges: **₹0.00**
- Net P&L: **₹-753.24**
- Profit/Loss percentage: **-0.7532%**
- Holding period: **1d 17h 15m**
- Notes: Entry OB candle=2026-09-21 16:15:00 IST; exit OB candle=2026-09-23 09:30:00 IST; use_wicks=False; threshold=0%.
