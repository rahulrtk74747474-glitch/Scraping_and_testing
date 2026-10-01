# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹97,383.22**
- Cash: **₹97,383.22**
- Total P&L: **₹-2,616.78 (-2.62%)**
- Realized P&L: **₹-2,616.78**
- Unrealized P&L: **₹0.00**
- Closed trades: **5** | Wins: **1** | Losses: **4** | Win rate: **20.00%**
- Max drawdown: **3.41%**
- Latest source close: **4,213.799805 USD**
- USD/INR used this run: **96.1050**
- Last processed candle: `2026-10-01T06:59:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-09-30T15:29:59.999000+00:00`
- Original OB candle open time: `2026-09-30T14:00:00+00:00`
- OB high / avg / low: **4215.000000 / 4211.899902 / 4208.799805**
- Move used by indicator: **0.5604%**

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

- Source: **yahoo / GC=F**.
- Note: COMEX Gold futures (Yahoo GC=F) 15-minute candles are used as a gold-price proxy for XAUUSDT because Binance's public Options API exposes the live XAUUSDT underlying index but not historical underlying-index OHLC klines. USD values are converted to INR for paper reporting.

_Paper trading/research only; no real order is sent._
