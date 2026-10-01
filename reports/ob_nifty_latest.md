# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,212.81**
- Cash: **₹95,212.81**
- Total P&L: **₹-4,787.19 (-4.79%)**
- Realized P&L: **₹-4,787.19**
- Unrealized P&L: **₹0.00**
- Closed trades: **3** | Wins: **0** | Losses: **3** | Win rate: **0.00%**
- Max drawdown: **4.96%**
- Latest source close: **22,358.150391 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-01T09:14:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-01T07:29:59.999000+00:00`
- Original OB candle open time: `2026-10-01T06:00:00+00:00`
- OB high / avg / low: **22573.699219 / 22558.924805 / 22544.150391**
- Move used by indicator: **1.0890%**

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
