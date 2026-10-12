# BANKNIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,699.43**
- Cash: **₹89,477.77**
- Total P&L: **₹-1,300.57 (-1.30%)**
- Realized / unrealized: **₹-1,280.77 / ₹-19.81**
- Max drawdown: **1.78%**
- Last processed candle: **2026-10-12T05:14:59.999000+00:00**
- Next same-side size: **12.500000% of current position unless a BUY reverses first**

## Position

- LONG qty: **0.1677520391** | cost basis: **₹9,241.46**

## Latest confirmed major swing

- **SELL** confirmed 2026-10-12T05:14:59.999000+00:00; pivot candle 2026-10-09T08:45:00+00:00; pivot 55,418.750000 INR

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
