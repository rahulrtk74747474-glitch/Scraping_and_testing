# XAUUSDT Order Block 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **2**
- Profits / losses: **0 / 2**
- Net realized P&L in journal: **₹-1,436.97**
- Average return per closed trade: **-0.7210%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-24 23:14:59 IST | XAUUSDT | LONG | LOSS | ₹-683.73 | -0.6889% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.38738331693043265%. |
| 2 | 2026-09-23 10:59:59 IST | XAUUSDT | LONG | LOSS | ₹-753.24 | -0.7532% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.11179079269419598%. |

## Full trade details

### Trade 2 — LOSS — XAUUSDT

- Trade ID: `OB_XAUUSDT-2-1790211599999`
- Strategy: **XAUUSDT Order Block**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-24 06:29:59 IST**
- Entry signal: **BULLISH_OB**
- Why entry was taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.3078486545084587%.
- Entry price: **₹414,865.1342**
- Quantity: **0.23922655453694186**
- Entry value/cost: **₹99,246.76**
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit time: **2026-09-24 23:14:59 IST**
- Exit signal: **BEARISH_OB**
- Why position was closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.38738331693043265%.
- Exit price: **₹412,007.0364**
- Exit value/proceeds: **₹98,563.02**
- Gross P&L: **₹-683.73**
- Fees/charges: **₹0.00**
- Net P&L: **₹-683.73**
- Profit/Loss percentage: **-0.6889%**
- Holding period: **0d 16h 45m**
- Notes: Entry OB candle=2026-09-24 05:00:00 IST; exit OB candle=2026-09-24 21:45:00 IST; use_wicks=False; threshold=0%.

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
