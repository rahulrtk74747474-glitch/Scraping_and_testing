# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,805.52**
- Cash: **₹0.00**
- Total P&L: **₹-6,194.48 (-6.19%)**
- Realized P&L: **₹-6,194.48**
- Unrealized P&L: **₹-0.00**
- Closed trades: **19** | Wins: **5** | Losses: **14** | Win rate: **26.32%**
- Max drawdown: **6.78%**
- Latest source close: **3,940.199951 USD**
- USD/INR used this run: **94.7300**
- Last processed candle: `2026-11-03T21:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-03T21:59:59.999000+00:00`
- Entry price: **3,940.199951 USD**
- Quantity (synthetic units): **0.2513174178**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-03T21:59:59.999000+00:00`
- Original OB candle open time: `2026-11-03T20:30:00+00:00`
- OB high / avg / low: **3932.699951 / 3931.049927 / 3929.399902**
- Move used by indicator: **0.2442%**

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
