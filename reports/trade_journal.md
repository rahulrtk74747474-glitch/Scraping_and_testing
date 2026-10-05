# BANKNIFTY Order Block 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **2**
- Profits / losses: **1 / 1**
- Net realized P&L in journal: **₹-3,545.87**
- Average return per closed trade: **-1.7651%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-10-05 10:44:59 IST | BANKNIFTY | LONG | PROFIT | ₹381.45 | 0.3970% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.5986001995097735%. |
| 2 | 2026-10-01 12:59:59 IST | BANKNIFTY | LONG | LOSS | ₹-3,927.32 | -3.9273% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=1.302167346725494%. |

## Full trade details

### Trade 2 — PROFIT — BANKNIFTY

- Trade ID: `OB_BANKNIFTY-2-1790847899999`
- Strategy: **BANKNIFTY Order Block**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-10-01 15:14:59 IST**
- Entry signal: **BULLISH_OB**
- Why entry was taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.7027880322519041%.
- Entry price: **₹54,565.1016**
- Quantity: **1.7606981824640526**
- Entry value/cost: **₹96,072.68**
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit time: **2026-10-05 10:44:59 IST**
- Exit signal: **BEARISH_OB**
- Why position was closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.5986001995097735%.
- Exit price: **₹54,781.7500**
- Exit value/proceeds: **₹96,454.13**
- Gross P&L: **₹381.45**
- Fees/charges: **₹0.00**
- Net P&L: **₹381.45**
- Profit/Loss percentage: **0.3970%**
- Holding period: **3d 19h 30m**
- Notes: Entry OB candle=2026-10-01 13:45:00 IST; exit OB candle=2026-10-05 09:15:00 IST; use_wicks=False; threshold=0%.

### Trade 1 — LOSS — BANKNIFTY

- Trade ID: `OB_BANKNIFTY-1-1790139599999`
- Strategy: **BANKNIFTY Order Block**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-23 10:29:59 IST**
- Entry signal: **BULLISH_OB**
- Why entry was taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.5471753847026175%.
- Entry price: **₹56,523.1484**
- Quantity: **1.7691866565178012**
- Entry value/cost: **₹100,000.00**
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit time: **2026-10-01 12:59:59 IST**
- Exit signal: **BEARISH_OB**
- Why position was closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=1.302167346725494%.
- Exit price: **₹54,303.3008**
- Exit value/proceeds: **₹96,072.68**
- Gross P&L: **₹-3,927.32**
- Fees/charges: **₹0.00**
- Net P&L: **₹-3,927.32**
- Profit/Loss percentage: **-3.9273%**
- Holding period: **8d 2h 30m**
- Notes: Entry OB candle=2026-09-22 15:15:00 IST; exit OB candle=2026-10-01 11:30:00 IST; use_wicks=False; threshold=0%.
