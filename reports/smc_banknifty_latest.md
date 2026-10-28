# BANKNIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,010.17**
- Cash: **₹79,803.24**
- Total P&L: **₹-1,989.83 (-1.99%)**
- Realized / unrealized: **₹-1,976.63 / ₹-13.20**
- Max drawdown: **2.15%**
- Last processed candle: **2026-10-28T09:59:59.999000+00:00**
- Next same-side size: **50.000000% of current cash unless a SELL reverses first**

## Position

- LONG qty: **0.3355040782** | cost basis: **₹18,220.13**

## Latest confirmed major swing

- **BUY** confirmed 2026-10-28T06:29:59.999000+00:00; pivot candle 2026-10-28T03:45:00+00:00; pivot 53,626.148438 INR

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
