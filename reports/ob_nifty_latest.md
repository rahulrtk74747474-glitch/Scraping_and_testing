# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹94,161.03**
- Cash: **₹94,161.03**
- Total P&L: **₹-5,838.97 (-5.84%)**
- Realized P&L: **₹-5,838.97**
- Unrealized P&L: **₹0.00**
- Closed trades: **5** | Wins: **0** | Losses: **5** | Win rate: **0.00%**
- Max drawdown: **6.01%**
- Latest source close: **22,377.449219 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-12T06:29:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-12T05:44:59.999000+00:00`
- Original OB candle open time: `2026-10-12T04:15:00+00:00`
- OB high / avg / low: **22538.150391 / 22525.150391 / 22512.150391**
- Move used by indicator: **0.5439%**

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
