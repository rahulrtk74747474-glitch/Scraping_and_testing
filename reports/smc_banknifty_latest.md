# BANKNIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹100,000.06**
- Cash: **₹25,410.26**
- Total P&L: **₹0.06 (0.00%)**
- Realized / unrealized: **₹13.66 / ₹-13.60**
- Max drawdown: **0.15%**
- Last processed candle: **2026-09-25T09:59:59.999000+00:00**
- Next same-side size: **50.000000% of current cash unless a SELL reverses first**

## Position

- LONG qty: **1.3420163128** | cost basis: **₹74,603.40**

## Latest confirmed major swing

- **BUY** confirmed 2026-09-25T09:59:59.999000+00:00; pivot candle 2026-09-25T07:15:00+00:00; pivot 55,424.300781 INR

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
