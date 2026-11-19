# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹85,654.39**
- Cash: **₹0.00**
- Total P&L: **₹-14,345.61 (-14.35%)**
- Realized P&L: **₹-14,375.60**
- Unrealized P&L: **₹29.99**
- Closed trades: **36** | Wins: **8** | Losses: **28** | Win rate: **22.22%**
- Max drawdown: **18.33%**
- Latest source close: **63,774.670000 USDT**
- USD/INR used this run: **93.3100**
- Last processed candle: `2026-11-19T09:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-19T06:59:59.999000+00:00`
- Entry price: **63,752.340000 USDT**
- Quantity (synthetic units): **0.0143937253**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-19T06:59:59.999000+00:00`
- Original OB candle open time: `2026-11-19T05:30:00+00:00`
- OB high / avg / low: **63409.510000 / 63367.130000 / 63324.750000**
- Move used by indicator: **0.6411%**

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
