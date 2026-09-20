# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,786.78**
- Cash: **₹98,786.78**
- Total P&L: **₹-1,213.22 (-1.21%)**
- Realized P&L: **₹-1,213.22**
- Unrealized P&L: **₹0.00**
- Closed trades: **1** | Wins: **0** | Losses: **1** | Win rate: **0.00%**
- Max drawdown: **1.23%**
- Latest source close: **81,160.080000 USDT**
- USD/INR used this run: **95.8630**
- Last processed candle: `2026-09-20T16:14:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-09-20T10:59:59.999000+00:00`
- Original OB candle open time: `2026-09-20T09:30:00+00:00`
- OB high / avg / low: **80581.820000 / 80481.915000 / 80382.010000**
- Move used by indicator: **0.2885%**

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
