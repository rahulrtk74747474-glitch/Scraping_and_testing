# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,571.62**
- Cash: **₹93,571.62**
- Total P&L: **₹-6,428.38 (-6.43%)**
- Realized P&L: **₹-6,428.38**
- Unrealized P&L: **₹0.00**
- Closed trades: **16** | Wins: **3** | Losses: **13** | Win rate: **18.75%**
- Max drawdown: **6.43%**
- Latest source close: **4,036.699951 USD**
- USD/INR used this run: **95.1050**
- Last processed candle: `2026-10-27T12:44:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-27T05:29:59.999000+00:00`
- Original OB candle open time: `2026-10-27T04:00:00+00:00`
- OB high / avg / low: **4036.300049 / 4033.450073 / 4030.600098**
- Move used by indicator: **0.4312%**

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
