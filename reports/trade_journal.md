# Vertex — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **1**
- Profits / losses: **1 / 0**
- Net realized P&L in journal: **₹170.82**
- Average return per closed trade: **1.8862%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-30 | ICICIBANK | LONG | PROFIT | ₹170.82 | 1.8862% | A later completed daily close was above the original entry price, which is the configured Vertex exit rule. |

## Full trade details

### Trade 1 — PROFIT — ICICIBANK

- Trade ID: `VERTEX-ICICIBANK-2026-09-29-2026-09-30`
- Strategy: **Vertex Chartink paper trader**
- Timeframe: **Daily decision cycle**
- Direction: **LONG**
- Entry time: **2026-09-29**
- Entry signal: **VERTEX_CHARTINK_SIGNAL**
- Why entry was taken: Stock appeared in the configured Chartink/Vertex screener on the entry date. Scanner name: Icici Bank Limited. Scanner change: -0.75%.
- Entry price: **₹1,292.2000**
- Quantity: **7**
- Entry value/cost: **₹9,045.40**
- Stop: **Not used — no fixed stop is configured.**
- Target: **Rule-based target: first later daily close above original entry price.**
- Exit time: **2026-09-30**
- Exit signal: **DAILY_CLOSE_ABOVE_ORIGINAL_ENTRY**
- Why position was closed/reduced: A later completed daily close was above the original entry price, which is the configured Vertex exit rule.
- Exit price: **₹1,321.7000**
- Exit value/proceeds: **₹9,251.90**
- Gross P&L: **₹206.50**
- Fees/charges: **₹35.68**
- Net P&L: **₹170.82**
- Profit/Loss percentage: **1.8862%**
- Holding period: **1 day(s)**
- Notes: Average-add count: 0; average-added notional: ₹0.00; maximum capital in trade: ₹9,056.15.
