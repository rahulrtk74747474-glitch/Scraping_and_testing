# Vertex — Closed Trade Journal

_This file is rebuilt automatically by the strategy workflow. A new closed trade appears here after the strategy records the exit._

## Journal summary

- Closed trade records: **1**
- Profits / losses: **1 / 0**
- Net realized P&L in journal: **₹33.37**
- Average return per closed trade: **0.4164%**

## Quick history

| # | Exit | Symbol | Direction | Result | Net P&L | Return | Exit reason |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-09-21 | PFIZER | LONG | PROFIT | ₹33.37 | 0.4164% | A later completed daily close was above the original entry price, which is the configured Vertex exit rule. |

## Full trade details

### Trade 1 — PROFIT — PFIZER

- Trade ID: `VERTEX-PFIZER-2026-09-18-2026-09-21`
- Strategy: **Vertex Chartink paper trader**
- Timeframe: **Daily decision cycle**
- Direction: **LONG**
- Entry time: **2026-09-18**
- Entry signal: **VERTEX_CHARTINK_SIGNAL**
- Why entry was taken: Stock appeared in the configured Chartink/Vertex screener on the entry date. Scanner name: Pfizer Limited. Scanner change: -0.31%.
- Entry price: **₹4,002.4000**
- Quantity: **2**
- Entry value/cost: **₹8,004.80**
- Stop: **Not used — no fixed stop is configured.**
- Target: **Rule-based target: first later daily close above original entry price.**
- Exit time: **2026-09-21**
- Exit signal: **DAILY_CLOSE_ABOVE_ORIGINAL_ENTRY**
- Why position was closed/reduced: A later completed daily close was above the original entry price, which is the configured Vertex exit rule.
- Exit price: **₹4,035.7000**
- Exit value/proceeds: **₹8,071.40**
- Gross P&L: **₹66.60**
- Fees/charges: **₹33.23**
- Net P&L: **₹33.37**
- Profit/Loss percentage: **0.4164%**
- Holding period: **3 day(s)**
- Notes: Average-add count: 0; average-added notional: ₹0.00; maximum capital in trade: ₹8,014.31.
