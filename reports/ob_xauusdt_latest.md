# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,662.81**
- Cash: **₹0.00**
- Total P&L: **₹-4,337.19 (-4.34%)**
- Realized P&L: **₹-3,760.69**
- Unrealized P&L: **₹-576.50**
- Closed trades: **6** | Wins: **1** | Losses: **5** | Win rate: **16.67%**
- Max drawdown: **4.34%**
- Latest source close: **4,181.600098 USD**
- USD/INR used this run: **96.4100**
- Last processed candle: `2026-10-06T13:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-06T12:14:59.999000+00:00`
- Entry price: **4,206.799805 USD**
- Quantity (synthetic units): **0.2372895120**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-06T12:14:59.999000+00:00`
- Original OB candle open time: `2026-10-06T10:45:00+00:00`
- OB high / avg / low: **4188.200195 / 4186.850098 / 4185.500000**
- Move used by indicator: **0.4945%**

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
