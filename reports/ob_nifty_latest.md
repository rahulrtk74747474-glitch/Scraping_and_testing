# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹104,882.29**
- Cash: **₹0.00**
- Total P&L: **₹4,882.29 (4.88%)**
- Realized P&L: **₹4,882.29**
- Unrealized P&L: **₹0.00**
- Closed trades: **8** | Wins: **2** | Losses: **6** | Win rate: **25.00%**
- Max drawdown: **6.37%**
- Latest source close: **25,144.300781 INR**
- Quote currency: **INR**
- Last processed candle: `2026-11-13T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-13T09:59:59.999000+00:00`
- Entry price: **25,144.300781 INR**
- Quantity (synthetic units): **4.1712152087**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-13T09:59:59.999000+00:00`
- Original OB candle open time: `2026-11-13T08:30:00+00:00`
- OB high / avg / low: **25097.050781 / 25084.750000 / 25072.449219**
- Move used by indicator: **0.2838%**

## Rules mirrored from the supplied Pine indicator

- Timeframe: **15 minutes**.
- Relevant periods: **5**.
- Minimum percent move threshold: **0.00%**.
- Use whole wick range: **No**.
- Bullish OB: last down candle before the required sequence of up candles.
- Bearish OB: last up candle before the required sequence of down candles.
- Buy only when the bullish OB is confirmed; use the full available paper account.
- Sell the entire long position when a bearish OB is confirmed.
- No short position is opened while flat.
- Signals are executed at the confirmation candle close, not backdated to the visually offset OB candle.
- Fee assumption: **0.0000% per side**; slippage: **0**.

## Data source

- Source: **yahoo / ^NSEI**.
- Note: NIFTY 50 index candles from Yahoo Finance. Paper units are synthetic index units, not exchange-tradable shares.

_Paper trading/research only; no real order is sent._
