# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,198.57**
- Cash: **₹0.00**
- Total P&L: **₹-3,801.43 (-3.80%)**
- Realized P&L: **₹-3,880.23**
- Unrealized P&L: **₹78.80**
- Closed trades: **15** | Wins: **5** | Losses: **10** | Win rate: **33.33%**
- Max drawdown: **8.32%**
- Latest source close: **81,720.940000 USDT**
- USD/INR used this run: **94.9500**
- Last processed candle: `2026-10-17T08:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-17T07:14:59.999000+00:00`
- Entry price: **81,654.000000 USDT**
- Quantity (synthetic units): **0.0123976770**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-17T07:14:59.999000+00:00`
- Original OB candle open time: `2026-10-17T05:45:00+00:00`
- OB high / avg / low: **81604.860000 / 81588.430000 / 81572.000000**
- Move used by indicator: **0.0969%**

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
