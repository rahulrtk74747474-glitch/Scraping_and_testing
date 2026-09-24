# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,661.72**
- Cash: **₹0.00**
- Total P&L: **₹-1,338.28 (-1.34%)**
- Realized P&L: **₹-753.24**
- Unrealized P&L: **₹-585.04**
- Closed trades: **1** | Wins: **0** | Losses: **1** | Win rate: **0.00%**
- Max drawdown: **1.34%**
- Latest source close: **4,298.500000 USD**
- USD/INR used this run: **95.9450**
- Last processed candle: `2026-09-24T12:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-24T00:59:59.999000+00:00`
- Entry price: **4,333.700195 USD**
- Quantity (synthetic units): **0.2392265545**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-24T05:29:59.999000+00:00`
- Original OB candle open time: `2026-09-24T04:00:00+00:00`
- OB high / avg / low: **4320.100098 / 4318.250000 / 4316.399902**
- Move used by indicator: **0.1273%**

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
