# BTCUSDT 4h SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹100,000.00**
- Cash: **₹100,000.00**
- Total P&L: **₹0.00 (0.00%)**
- Realized / unrealized: **₹0.00 / ₹0.00**
- Max drawdown: **0.00%**
- Last processed candle: **2026-09-23T19:59:59.999000+00:00**
- Next same-side size: **50.000000% on the first executable signal**

## Position

_Flat. SELL while flat does not open a short._

## Latest confirmed major swing

- **SELL** confirmed 2026-09-23T15:59:59.999000+00:00; pivot candle 2026-09-21T20:00:00+00:00; pivot 87,395.670000 USDT

## Updated sizing rules

- **SELL → BUY:** first BUY buys back the **same quantity as the immediately preceding executed SELL** (limited by available cash).
- If another BUY follows without an intervening SELL: buy **50% of current cash**.
- Next consecutive BUY: buy **12.5% of current cash**; then **6.25%, 3.125%, ...** on further BUY signals.
- **BUY → SELL:** first SELL sells the **same quantity as the immediately preceding executed BUY** (limited by current holding).
- If another SELL follows without an intervening BUY: sell **50% of the current position**.
- Next consecutive SELL: sell **12.5% of the current position**; then **6.25%, 3.125%, ...** on further SELL signals.
- The restore trade is based on **quantity**, not the old rupee value, so it reverses the actual units previously traded.
- BUY = confirmed pivot low; SELL = confirmed pivot high.
- Execute at confirmation-candle close, never on the older back-plotted pivot candle.
- No historical trade replay on initialization.
- Data: **binance_spot / BTCUSDT**.
- Note: BTCUSDT spot candles from Binance public data; paper account is valued in INR.

_Paper trading only; no real orders._
