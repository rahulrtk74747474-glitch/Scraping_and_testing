# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,675.99**
- Cash: **₹93,675.99**
- Total P&L: **₹-6,324.01 (-6.32%)**
- Realized P&L: **₹-6,324.01**
- Unrealized P&L: **₹0.00**
- Closed trades: **27** | Wins: **8** | Losses: **19** | Win rate: **29.63%**
- Max drawdown: **11.11%**
- Latest source close: **77,042.000000 USDT**
- USD/INR used this run: **94.8050**
- Last processed candle: `2026-11-03T09:44:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-11-03T08:44:59.999000+00:00`
- Original OB candle open time: `2026-11-03T07:15:00+00:00`
- OB high / avg / low: **76913.990000 / 76746.080000 / 76578.170000**
- Move used by indicator: **0.4448%**

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
