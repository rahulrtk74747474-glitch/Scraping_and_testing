# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹85,506.71**
- Cash: **₹85,506.71**
- Total P&L: **₹-14,493.29 (-14.49%)**
- Realized P&L: **₹-14,493.29**
- Unrealized P&L: **₹0.00**
- Closed trades: **39** | Wins: **10** | Losses: **29** | Win rate: **25.64%**
- Max drawdown: **21.63%**
- Latest source close: **61,683.390000 USDT**
- USD/INR used this run: **92.9400**
- Last processed candle: `2026-11-23T09:29:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-11-23T02:14:59.999000+00:00`
- Original OB candle open time: `2026-11-23T00:45:00+00:00`
- OB high / avg / low: **61352.330000 / 61253.170000 / 61154.010000**
- Move used by indicator: **0.8159%**

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
