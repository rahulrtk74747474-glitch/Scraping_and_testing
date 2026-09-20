# BTCUSDT Order Block 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **1**
- Profits / losses: **0 / 1**
- Net realized P&L in journal: **₹-1,213.22**
- Average return per closed trade: **-1.2132%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-20 16:29:59 IST | BTCUSDT | LONG | LOSS | ₹-1,213.22 | -1.2132% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.28853411460919437%. |

## Full trade details

### Trade 1 — LOSS — BTCUSDT

- Trade ID: `OB_BTCUSDT-1-1789860599999`
- Strategy: **BTCUSDT Order Block**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-20 04:59:59 IST**
- Entry signal: **BULLISH_OB**
- Why entry was taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.3703305470791676%.
- Entry price: **₹7,794,236.9936**
- Quantity: **0.01282999222138564**
- Entry value/cost: **₹100,000.00**
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit time: **2026-09-20 16:29:59 IST**
- Exit signal: **BEARISH_OB**
- Why position was closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.28853411460919437%.
- Exit price: **₹7,699,675.8142**
- Exit value/proceeds: **₹98,786.78**
- Gross P&L: **₹-1,213.22**
- Fees/charges: **₹0.00**
- Net P&L: **₹-1,213.22**
- Profit/Loss percentage: **-1.2132%**
- Holding period: **0d 11h 30m**
- Notes: Entry OB candle=2026-09-20 03:30:00 IST; exit OB candle=2026-09-20 15:00:00 IST; use_wicks=False; threshold=0%.
