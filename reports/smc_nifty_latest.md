# NIFTY 15m SMC Major-Swing Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,855.88**
- Cash: **₹55,720.57**
- Total P&L: **₹-1,144.12 (-1.14%)**
- Realized / unrealized: **₹-1,288.30 / ₹144.18**
- Max drawdown: **2.88%**
- Last processed candle: **2026-10-27T09:59:59.999000+00:00**
- Next same-side size: **12.500000% of current position unless a BUY reverses first**

## Position

- LONG qty: **1.8960781565** | cost basis: **₹42,991.12**

## Latest confirmed major swing

- **SELL** confirmed 2026-10-27T09:44:59.999000+00:00; pivot candle 2026-10-27T07:00:00+00:00; pivot 22,829.699219 INR

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
