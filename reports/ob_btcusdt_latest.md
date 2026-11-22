# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹83,777.08**
- Cash: **₹83,777.08**
- Total P&L: **₹-16,222.92 (-16.22%)**
- Realized P&L: **₹-16,222.92**
- Unrealized P&L: **₹0.00**
- Closed trades: **38** | Wins: **9** | Losses: **29** | Win rate: **23.68%**
- Max drawdown: **21.63%**
- Latest source close: **58,924.260000 USDT**
- USD/INR used this run: **92.6600**
- Last processed candle: `2026-11-22T05:59:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-11-22T03:14:59.999000+00:00`
- Original OB candle open time: `2026-11-22T01:45:00+00:00`
- OB high / avg / low: **60215.440000 / 60151.140000 / 60086.840000**
- Move used by indicator: **1.3259%**

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

- Source: **binance_spot / BTCUSDT**.
- Note: BTCUSDT 15-minute spot candles from Binance public market data. USDT values are converted to INR using the latest USD/INR rate for paper-account reporting.

_Paper trading/research only; no real order is sent._
