# NIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,507.53**
- Cash: **₹25,426.34**
- Total P&L: **₹-1,492.47 (-1.49%)**
- Realized / unrealized: **₹-1,180.40 / ₹-312.07**
- Max drawdown: **2.27%**
- Last processed candle: **2026-10-07T09:59:59.999000+00:00**
- Next same-side size: **50.000000% of current position unless a BUY reverses first**

## Position

- LONG qty: **3.2332446353** | cost basis: **₹73,393.26**

## Latest confirmed major swing

- **SELL** confirmed 2026-10-07T09:14:59.999000+00:00; pivot candle 2026-10-07T06:30:00+00:00; pivot 22,717.250000 INR

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
