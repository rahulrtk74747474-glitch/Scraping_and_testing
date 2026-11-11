# BANKNIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹103,901.31**
- Cash: **₹71,967.93**
- Total P&L: **₹3,901.31 (3.90%)**
- Realized / unrealized: **₹1,512.15 / ₹2,389.16**
- Max drawdown: **2.15%**
- Last processed candle: **2026-11-11T09:59:59.999000+00:00**
- Next same-side size: **12.500000% of current position unless a BUY reverses first**

## Position

- LONG qty: **0.5252857316** | cost basis: **₹29,544.22**

## Latest confirmed major swing

- **SELL** confirmed 2026-11-11T08:44:59.999000+00:00; pivot candle 2026-11-11T06:00:00+00:00; pivot 61,394.050781 INR

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
