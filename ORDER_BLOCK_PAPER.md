# Order Block 15m paper trader

This branch is isolated from the existing Vertex and BTC strategy branches.

Rules:
- Starting paper capital: ₹1,00,000.
- Timeframe: 15m.
- Mirrors the supplied Pine v4 Order Block Finder defaults: periods=5, threshold=0%, usewicks=false.
- Confirmed bullish OB while flat: buy with the full available paper account.
- Confirmed bearish OB while long: sell the full position.
- Bearish OB while flat does not open a short.
- First run initializes at the latest completed candle and does not replay old trades.
- State, signals, orders, trades, snapshots and latest report are committed to this branch after each scheduled run.

The Pine script plots the OB back on the source candle, but confirmation occurs later. This paper engine executes only at the confirmation candle close, so it does not backdate fills.
