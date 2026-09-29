# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,585.97**
- Cash: **₹0.00**
- Total P&L: **₹-3,414.03 (-3.41%)**
- Realized P&L: **₹-3,221.77**
- Unrealized P&L: **₹-192.26**
- Closed trades: **4** | Wins: **0** | Losses: **4** | Win rate: **0.00%**
- Max drawdown: **3.41%**
- Latest source close: **4,169.899902 USD**
- USD/INR used this run: **95.9675**
- Last processed candle: `2026-09-29T08:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-29T06:14:59.999000+00:00`
- Entry price: **4,178.200195 USD**
- Quantity (synthetic units): **0.2413594202**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-29T06:14:59.999000+00:00`
- Original OB candle open time: `2026-09-29T04:45:00+00:00`
- OB high / avg / low: **4158.500000 / 4157.850098 / 4157.200195**
- Move used by indicator: **0.4810%**

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
