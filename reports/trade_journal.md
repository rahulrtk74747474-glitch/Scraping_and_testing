# NIFTY Order Block 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **1**
- Profits / losses: **0 / 1**
- Net realized P&L in journal: **₹-987.03**
- Average return per closed trade: **-0.9870%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-24 12:44:59 IST | NIFTY | LONG | LOSS | ₹-987.03 | -0.9870% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.21702743149359446%. |

## Full trade details

### Trade 1 — LOSS — NIFTY

- Trade ID: `OB_NIFTY-1-1789971299999`
- Strategy: **NIFTY Order Block**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-21 11:44:59 IST**
- Entry signal: **BULLISH_OB**
- Why entry was taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.13242446490805995%.
- Entry price: **₹23,403.6504**
- Quantity: **4.272837712532993**
- Entry value/cost: **₹100,000.00**
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit time: **2026-09-24 12:44:59 IST**
- Exit signal: **BEARISH_OB**
- Why position was closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.21702743149359446%.
- Exit price: **₹23,172.6504**
- Exit value/proceeds: **₹99,012.97**
- Gross P&L: **₹-987.03**
- Fees/charges: **₹0.00**
- Net P&L: **₹-987.03**
- Profit/Loss percentage: **-0.9870%**
- Holding period: **3d 1h 0m**
- Notes: Entry OB candle=2026-09-21 10:15:00 IST; exit OB candle=2026-09-24 11:15:00 IST; use_wicks=False; threshold=0.0%.
