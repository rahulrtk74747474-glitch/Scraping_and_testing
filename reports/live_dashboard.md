# Live Strategy Dashboard

_Seeded from the latest committed strategy state. It will be rebuilt automatically by GitHub Actions._

> **Live = latest completed GitHub strategy run/candle, not tick-by-tick streaming quotes.**

[Combined performance](all_strategies_combined_latest.md) · [Full trade journal](all_trades_journal.md)

## Open positions

### Vertex 500 Daily — PFIZER

- Status: **OPEN LONG**
- Entry date: **2026-09-18**
- Entry / weighted average: **₹4,002.40 / ₹4,002.40**
- Quantity: **2**
- Capital in trade: **₹8,014.31**
- Latest portfolio unrealized P&L: **₹-33.16**
- Position price chart: _starts automatically after at least two per-position price snapshots are stored._

### Vertex 500 3:15 — PFIZER

- Status: **OPEN LONG**
- Entry date: **2026-09-18**
- Entry / weighted average: **₹4,002.40 / ₹4,002.40**
- Quantity: **2**
- Capital in trade: **₹8,014.31**
- Latest portfolio unrealized P&L: **₹-33.16**
- Position price chart: _starts automatically after at least two per-position price snapshots are stored._

## Strategy status

| Strategy | Status | Equity | P&L |
|---|---|---:|---:|
| Vertex Daily | FLAT | ₹100,000.00 | ₹0.00 |
| Vertex 3:15 | FLAT | ₹100,000.00 | ₹0.00 |
| Vertex 500 Daily | 1 open | ₹99,966.84 | ₹-33.16 |
| Vertex 500 3:15 | 1 open | ₹99,966.84 | ₹-33.16 |
| BTCUSDT 15m Existing Strategy | FLAT | $100.2408 | $0.2408 |
| OB NIFTY 15m | FLAT | ₹100,000.00 | ₹0.00 |
| OB BANKNIFTY 15m | FLAT | ₹100,000.00 | ₹0.00 |
| OB BTCUSDT 15m | FLAT | ₹100,000.00 | ₹0.00 |
| OB XAUUSDT 15m | FLAT | ₹100,000.00 | ₹0.00 |
| SMC NIFTY 15m | FLAT | ₹100,000.00 | ₹0.00 |
| SMC BANKNIFTY 15m | FLAT | ₹100,000.00 | ₹0.00 |
| SMC BTCUSDT 4h | FLAT | ₹100,000.00 | ₹0.00 |

## Automation

- GitHub rebuilds this dashboard after strategy workflows and on the master reporting refresh.
- Open-position data comes from the strategy branches themselves.
- Price/equity SVG charts are generated automatically from stored snapshots.
- The trade journal also updates automatically when a position or realized slice closes.
- **No ChatGPT intervention or subscription is required.**
