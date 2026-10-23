# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹97,273.25**
- Cash: **₹97,273.25**
- Total P&L: **₹-2,726.75 (-2.73%)**
- Realized P&L: **₹-2,726.75**
- Unrealized P&L: **₹0.00**
- Closed trades: **18** | Wins: **6** | Losses: **12** | Win rate: **33.33%**
- Max drawdown: **9.22%**
- Latest source close: **81,492.010000 USDT**
- USD/INR used this run: **94.8080**
- Last processed candle: `2026-10-23T01:44:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-22T08:59:59.999000+00:00`
- Original OB candle open time: `2026-10-22T07:30:00+00:00`
- OB high / avg / low: **82323.000000 / 82298.870000 / 82274.740000**
- Move used by indicator: **0.5180%**

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
