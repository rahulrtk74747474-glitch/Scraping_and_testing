# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹94,293.63**
- Cash: **₹0.00**
- Total P&L: **₹-5,706.37 (-5.71%)**
- Realized P&L: **₹-8,059.52**
- Unrealized P&L: **₹2,353.15**
- Closed trades: **29** | Wins: **8** | Losses: **21** | Win rate: **27.59%**
- Max drawdown: **7.09%**
- Latest source close: **3,620.399902 USD**
- USD/INR used this run: **92.5400**
- Last processed candle: `2026-11-26T04:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-25T17:59:59.999000+00:00`
- Entry price: **3,542.300049 USD**
- Quantity (synthetic units): **0.2814467873**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-25T17:59:59.999000+00:00`
- Original OB candle open time: `2026-11-25T16:30:00+00:00`
- OB high / avg / low: **3488.899902 / 3481.649902 / 3474.399902**
- Move used by indicator: **1.8019%**

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
