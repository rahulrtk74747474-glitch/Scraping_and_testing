# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹85,169.71**
- Cash: **₹0.00**
- Total P&L: **₹-14,830.29 (-14.83%)**
- Realized P&L: **₹-17,014.92**
- Unrealized P&L: **₹2,184.63**
- Closed trades: **40** | Wins: **10** | Losses: **30** | Win rate: **25.00%**
- Max drawdown: **21.63%**
- Latest source close: **59,913.710000 USDT**
- USD/INR used this run: **92.9800**
- Last processed candle: `2026-11-28T03:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-25T13:29:59.999000+00:00`
- Entry price: **58,858.000000 USDT**
- Quantity (synthetic units): **0.0152886592**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-28T02:14:59.999000+00:00`
- Original OB candle open time: `2026-11-28T00:45:00+00:00`
- OB high / avg / low: **59987.360000 / 59942.305000 / 59897.250000**
- Move used by indicator: **0.5722%**

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

- Source: **binance_spot / BTCUSDT**.
- Note: BTCUSDT 15-minute spot candles from Binance public market data. USDT values are converted to INR using the latest USD/INR rate for paper-account reporting.

_Paper trading/research only; no real order is sent._
