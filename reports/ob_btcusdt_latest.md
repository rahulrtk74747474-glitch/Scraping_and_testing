# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹102,959.74**
- Cash: **₹102,959.74**
- Total P&L: **₹2,959.74 (2.96%)**
- Realized P&L: **₹2,959.74**
- Unrealized P&L: **₹0.00**
- Closed trades: **8** | Wins: **3** | Losses: **5** | Win rate: **37.50%**
- Max drawdown: **2.00%**
- Latest source close: **84,912.010000 USDT**
- USD/INR used this run: **96.3000**
- Last processed candle: `2026-10-04T05:59:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-04T01:29:59.999000+00:00`
- Original OB candle open time: `2026-10-04T00:00:00+00:00`
- OB high / avg / low: **84840.010000 / 84796.790000 / 84753.570000**
- Move used by indicator: **0.0855%**

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
