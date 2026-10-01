# BANKNIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,413.13**
- Cash: **₹61,939.81**
- Total P&L: **₹-1,586.87 (-1.59%)**
- Realized / unrealized: **₹-1,123.80 / ₹-463.07**
- Max drawdown: **1.78%**
- Last processed candle: **2026-10-01T09:14:59.999000+00:00**
- Next same-side size: **50.000000% of current position unless a BUY reverses first**

## Position

- LONG qty: **0.6710081564** | cost basis: **₹36,936.39**

## Latest confirmed major swing

- **SELL** confirmed 2026-10-01T07:44:59.999000+00:00; pivot candle 2026-10-01T05:00:00+00:00; pivot 55,090.699219 INR

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
