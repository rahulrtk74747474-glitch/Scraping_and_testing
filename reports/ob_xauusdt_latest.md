# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹94,668.54**
- Cash: **₹0.00**
- Total P&L: **₹-5,331.46 (-5.33%)**
- Realized P&L: **₹-4,996.77**
- Unrealized P&L: **₹-334.70**
- Closed trades: **23** | Wins: **7** | Losses: **16** | Win rate: **30.43%**
- Max drawdown: **6.78%**
- Latest source close: **4,073.000000 USD**
- USD/INR used this run: **93.8950**
- Last processed candle: `2026-11-06T20:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-06T18:59:59.999000+00:00`
- Entry price: **4,087.399902 USD**
- Quantity (synthetic units): **0.2475419501**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-06T18:59:59.999000+00:00`
- Original OB candle open time: `2026-11-06T17:30:00+00:00`
- OB high / avg / low: **4068.800049 / 4065.700073 / 4062.600098**
- Move used by indicator: **0.5708%**

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
