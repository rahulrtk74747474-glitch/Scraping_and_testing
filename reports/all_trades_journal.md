# All Strategies — Trade Journal

_Aggregated automatically from each strategy branch. INR and USD results are kept separate._

## Summary

- Closed trade records: **3**
- Profits / losses: **1 / 2**
- Net INR P&L: **₹-1,213.22**
- Net USD P&L: **$0.2408**

## All closed trades

| Exit | Strategy | Symbol | Direction | Result | Net P&L | Return | Why closed |
|---|---|---|---|---|---:|---:|---|
| 2026-09-20 16:29:59 IST | OB BTCUSDT 15m | BTCUSDT | LONG | LOSS | ₹-1,213.22 | -1.2132% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.28853411460919437%. |
| 2026-09-19 20:14:59 IST | BTCUSDT 15m | BTCUSDT | SHORT | LOSS | $-0.4243 | -0.4215% | Configured stop level was hit. |
| 2026-09-19 06:44:59 IST | BTCUSDT 15m | BTCUSDT | LONG | PROFIT | $0.6650 | 0.6650% | Configured profit target was hit. |

## Detailed journal

### OB BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `OB_BTCUSDT-1-1789860599999`
- Branch: `ob-btcusdt-15m-paper`
- Entry: **2026-09-20 04:59:59 IST** at **7794236.9936**
- Entry signal: **BULLISH_OB**
- Why taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.3703305470791676%.
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit: **2026-09-20 16:29:59 IST** at **7699675.8142**
- Exit signal: **BEARISH_OB**
- Why closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.28853411460919437%.
- Quantity: **0.01282999222138564**
- Gross P&L: **₹-1,213.22**
- Fees/charges: **₹0.00**
- Net P&L: **₹-1,213.22**
- Profit/Loss percentage: **-1.2132%**
- Holding period: **0d 11h 30m**
- Notes: Entry OB candle=2026-09-20 03:30:00 IST; exit OB candle=2026-09-20 15:00:00 IST; use_wicks=False; threshold=0%.

### BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `BTCUSDT-1789780500000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-19 14:44:59 IST** at **81435.1100**
- Entry signal: **DISTRIBUTION_DOWN_CONFIRMED**
- Why taken: A confirmed distribution signal opened a SHORT after the strategy's sweep/distribution conditions.
- Stop: **81615.6200**
- Target: **80602.6700**
- Exit: **2026-09-19 20:14:59 IST** at **81615.6200**
- Exit signal: **STOP**
- Why closed/reduced: Configured stop level was hit.
- Quantity: **0.0012349029419191694**
- Gross P&L: **$-0.2229**
- Fees/charges: **$0.2014**
- Net P&L: **$-0.4243**
- Profit/Loss percentage: **-0.4215%**
- Holding period: **0d 5h 30m**
- Notes: Outcome=STOP; R multiple=-1.0; balance after=$100.2408.

### BTCUSDT 15m — BTCUSDT — PROFIT

- Trade ID: `BTCUSDT-1789753500000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-19 05:44:59 IST** at **80976.0100**
- Entry signal: **DISTRIBUTION_UP_CONFIRMED**
- Why taken: A confirmed distribution signal opened a LONG after the strategy's sweep/distribution conditions.
- Stop: **80720.4100**
- Target: **81677.7100**
- Exit: **2026-09-19 06:44:59 IST** at **81677.7100**
- Exit signal: **TARGET**
- Why closed/reduced: Configured profit target was hit.
- Quantity: **0.001233699955086697**
- Gross P&L: **$0.8657**
- Fees/charges: **$0.2007**
- Net P&L: **$0.6650**
- Profit/Loss percentage: **0.6650%**
- Holding period: **0d 1h 0m**
- Notes: Outcome=TARGET; R multiple=2.745305164319388; balance after=$100.6650.
