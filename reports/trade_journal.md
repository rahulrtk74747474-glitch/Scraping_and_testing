# BTCUSDT 15m — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **2**
- Profits / losses: **1 / 1**
- Net realized P&L in journal: **$0.2408**
- Average return per closed trade: **0.1218%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-19 20:14:59 IST | BTCUSDT | SHORT | LOSS | $-0.4243 | -0.4215% | Configured stop level was hit. |
| 2 | 2026-09-19 06:44:59 IST | BTCUSDT | LONG | PROFIT | $0.6650 | 0.6650% | Configured profit target was hit. |

## Full trade details

### Trade 2 — LOSS — BTCUSDT

- Trade ID: `BTCUSDT-1789780500000`
- Strategy: **BTCUSDT confirmed-distribution paper trader**
- Timeframe: **15m**
- Direction: **SHORT**
- Entry time: **2026-09-19 14:44:59 IST**
- Entry signal: **DISTRIBUTION_DOWN_CONFIRMED**
- Why entry was taken: A confirmed distribution signal opened a SHORT after the strategy's sweep/distribution conditions.
- Entry price: **$81,435.1100**
- Quantity: **0.0012349029419191694**
- Entry value/cost: **$100.5645**
- Stop: **$81,615.6200**
- Target: **$80,602.6700**
- Exit time: **2026-09-19 20:14:59 IST**
- Exit signal: **STOP**
- Why position was closed/reduced: Configured stop level was hit.
- Exit price: **$81,615.6200**
- Exit value/proceeds: **$100.7874**
- Gross P&L: **$-0.2229**
- Fees/charges: **$0.2014**
- Net P&L: **$-0.4243**
- Profit/Loss percentage: **-0.4215%**
- Holding period: **0d 5h 30m**
- Notes: Outcome=STOP; R multiple=-1.0; balance after=$100.2408.

### Trade 1 — PROFIT — BTCUSDT

- Trade ID: `BTCUSDT-1789753500000`
- Strategy: **BTCUSDT confirmed-distribution paper trader**
- Timeframe: **15m**
- Direction: **LONG**
- Entry time: **2026-09-19 05:44:59 IST**
- Entry signal: **DISTRIBUTION_UP_CONFIRMED**
- Why entry was taken: A confirmed distribution signal opened a LONG after the strategy's sweep/distribution conditions.
- Entry price: **$80,976.0100**
- Quantity: **0.001233699955086697**
- Entry value/cost: **$99.9001**
- Stop: **$80,720.4100**
- Target: **$81,677.7100**
- Exit time: **2026-09-19 06:44:59 IST**
- Exit signal: **TARGET**
- Why position was closed/reduced: Configured profit target was hit.
- Exit price: **$81,677.7100**
- Exit value/proceeds: **$100.7658**
- Gross P&L: **$0.8657**
- Fees/charges: **$0.2007**
- Net P&L: **$0.6650**
- Profit/Loss percentage: **0.6650%**
- Holding period: **0d 1h 0m**
- Notes: Outcome=TARGET; R multiple=2.745305164319388; balance after=$100.6650.
