# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,628.80**
- Cash: **₹0.00**
- Total P&L: **₹-4,371.20 (-4.37%)**
- Realized P&L: **₹-4,399.73**
- Unrealized P&L: **₹28.54**
- Closed trades: **7** | Wins: **1** | Losses: **6** | Win rate: **14.29%**
- Max drawdown: **4.77%**
- Latest source close: **4,158.600098 USD**
- USD/INR used this run: **96.7500**
- Last processed candle: `2026-10-08T20:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-08T01:59:59.999000+00:00`
- Entry price: **4,156.500000 USD**
- Quantity (synthetic units): **0.2376788769**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-08T19:59:59.999000+00:00`
- Original OB candle open time: `2026-10-08T18:30:00+00:00`
- OB high / avg / low: **4150.399902 / 4148.250000 / 4146.100098**
- Move used by indicator: **0.1903%**

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
