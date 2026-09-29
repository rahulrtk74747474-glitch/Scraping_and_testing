# NIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,599.96**
- Cash: **₹12,684.70**
- Total P&L: **₹-1,400.04 (-1.40%)**
- Realized / unrealized: **₹-228.44 / ₹-1,171.61**
- Max drawdown: **1.59%**
- Last processed candle: **2026-09-29T08:29:59.999000+00:00**
- Next same-side size: **12.500000% of current cash unless a SELL reverses first**

## Position

- LONG qty: **3.7910088109** | cost basis: **₹87,086.86**

## Latest confirmed major swing

- **BUY** confirmed 2026-09-29T06:44:59.999000+00:00; pivot candle 2026-09-29T04:00:00+00:00; pivot 22,569.650391 INR

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
