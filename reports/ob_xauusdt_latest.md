# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,744.35**
- Cash: **₹0.00**
- Total P&L: **₹-6,255.65 (-6.26%)**
- Realized P&L: **₹-8,059.52**
- Unrealized P&L: **₹1,803.87**
- Closed trades: **29** | Wins: **8** | Losses: **21** | Win rate: **27.59%**
- Max drawdown: **7.09%**
- Latest source close: **3,611.800049 USD**
- USD/INR used this run: **92.2200**
- Last processed candle: `2026-11-25T20:29:59.999000+00:00`

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
