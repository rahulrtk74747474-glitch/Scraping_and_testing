# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹99,342.93**
- Cash: **₹0.00**
- Total P&L: **₹-657.07 (-0.66%)**
- Realized P&L: **₹-753.24**
- Unrealized P&L: **₹96.18**
- Closed trades: **1** | Wins: **0** | Losses: **1** | Win rate: **0.00%**
- Max drawdown: **1.23%**
- Latest source close: **4,337.899902 USD**
- USD/INR used this run: **95.7300**
- Last processed candle: `2026-09-24T01:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-24T00:59:59.999000+00:00`
- Entry price: **4,333.700195 USD**
- Quantity (synthetic units): **0.2392265545**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-24T00:59:59.999000+00:00`
- Original OB candle open time: `2026-09-23T23:30:00+00:00`
- OB high / avg / low: **4323.600098 / 4321.900146 / 4320.200195**
- Move used by indicator: **0.3078%**

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
