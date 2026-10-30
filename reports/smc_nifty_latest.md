# NIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹99,352.18**
- Cash: **₹77,496.94**
- Total P&L: **₹-647.82 (-0.65%)**
- Realized / unrealized: **₹-901.27 / ₹253.44**
- Max drawdown: **2.88%**
- Last processed candle: **2026-10-30T09:59:59.999000+00:00**
- Next same-side size: **12.500000% of current position unless a BUY reverses first**

## Position

- LONG qty: **0.9480390782** | cost basis: **₹21,601.79**

## Latest confirmed major swing

- **SELL** confirmed 2026-10-30T09:59:59.999000+00:00; pivot candle 2026-10-30T07:15:00+00:00; pivot 23,118.000000 INR

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
- Data: **yahoo / ^NSEI**.
- Note: NIFTY 50 index candles from Yahoo Finance. Paper units are synthetic index units.

_Paper trading only; no real orders._
