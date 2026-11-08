# BTCUSDT 4h SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,475.12**
- Cash: **₹73,314.14**
- Total P&L: **₹-4,524.88 (-4.52%)**
- Realized / unrealized: **₹-3,005.93 / ₹-1,518.95**
- Max drawdown: **6.99%**
- Last processed candle: **2026-11-08T03:59:59.999000+00:00**
- Next same-side size: **12.500000% of current position unless a BUY reverses first**

## Position

- LONG qty: **0.0031088634** | cost basis: **₹23,679.93**

## Latest confirmed major swing

- **SELL** confirmed 2026-11-06T07:59:59.999000+00:00; pivot candle 2026-11-04T12:00:00+00:00; pivot 81,196.010000 USDT

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
