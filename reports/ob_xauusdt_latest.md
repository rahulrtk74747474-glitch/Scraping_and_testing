# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹99,582.52**
- Cash: **₹0.00**
- Total P&L: **₹-417.48 (-0.42%)**
- Realized P&L: **₹0.00**
- Unrealized P&L: **₹-417.48**
- Closed trades: **0** | Wins: **0** | Losses: **0** | Win rate: **0.00%**
- Max drawdown: **0.99%**
- Latest source close: **4,389.000000 USD**
- USD/INR used this run: **95.8050**
- Last processed candle: `2026-09-21T22:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-21T12:14:59.999000+00:00`
- Entry price: **4,407.399902 USD**
- Quantity (synthetic units): **0.2368259923**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-21T12:14:59.999000+00:00`
- Original OB candle open time: `2026-09-21T10:45:00+00:00`
- OB high / avg / low: **4385.700195 / 4382.900146 / 4380.100098**
- Move used by indicator: **0.6164%**

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
