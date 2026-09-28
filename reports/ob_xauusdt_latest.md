# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,778.23**
- Cash: **₹96,778.23**
- Total P&L: **₹-3,221.77 (-3.22%)**
- Realized P&L: **₹-3,221.77**
- Unrealized P&L: **₹0.00**
- Closed trades: **4** | Wins: **0** | Losses: **4** | Win rate: **0.00%**
- Max drawdown: **3.22%**
- Latest source close: **4,184.200195 USD**
- USD/INR used this run: **95.9800**
- Last processed candle: `2026-09-28T11:44:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-09-28T05:44:59.999000+00:00`
- Original OB candle open time: `2026-09-28T04:15:00+00:00`
- OB high / avg / low: **4232.700195 / 4232.350098 / 4232.000000**
- Move used by indicator: **0.3922%**

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
