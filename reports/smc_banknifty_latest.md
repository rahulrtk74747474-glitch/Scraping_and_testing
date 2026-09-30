# BANKNIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹99,381.46**
- Cash: **₹25,440.92**
- Total P&L: **₹-618.54 (-0.62%)**
- Realized / unrealized: **₹-611.12 / ₹-7.42**
- Max drawdown: **1.78%**
- Last processed candle: **2026-09-30T07:59:59.999000+00:00**
- Next same-side size: **50.000000% of current position unless a BUY reverses first**

## Position

- LONG qty: **1.3420163128** | cost basis: **₹73,947.95**

## Latest confirmed major swing

- **SELL** confirmed 2026-09-29T09:14:59.999000+00:00; pivot candle 2026-09-29T06:30:00+00:00; pivot 54,397.101562 INR

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
- Data: **yahoo / ^NSEBANK**.
- Note: NIFTY Bank index candles from Yahoo Finance. Paper units are synthetic index units.

_Paper trading only; no real orders._
