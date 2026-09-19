# BTCUSDT 4h SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹100,000.00**
- Cash: **₹100,000.00**
- Total P&L: **₹0.00 (0.00%)**
- Realized / unrealized: **₹0.00 / ₹0.00**
- Max drawdown: **0.00%**
- Last processed candle: **2026-09-19T11:59:59.999000+00:00**
- Next ladder fraction: **50.000000%**

## Position

_Flat. SELL while flat does not open a short._

## Latest confirmed major swing

_None recorded since initialization._

## Rules

- Timeframe **4h**, sig_sens **10**.
- BUY = confirmed pivot low; SELL = confirmed pivot high.
- Execute at confirmation-candle close, never on the older back-plotted pivot candle.
- BUY ladder: **50%, 25%, 12.5%, 6.25%, ...** of equity at start of the BUY sequence, capped by cash.
- SELL ladder: **50%, 25%, 12.5%, 6.25%, ...** of quantity at start of the SELL sequence, capped by remaining quantity.
- Opposite signal resets the ladder sequence.
- No historical trade replay on initialization.
- Data: **binance_spot / BTCUSDT**.
- Note: BTCUSDT spot candles from Binance public data; paper account is valued in INR.

_Paper trading only; no real orders._
