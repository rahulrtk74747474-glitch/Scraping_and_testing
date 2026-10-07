# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹101,878.94**
- Cash: **₹0.00**
- Total P&L: **₹1,878.94 (1.88%)**
- Realized P&L: **₹3,003.35**
- Unrealized P&L: **₹-1,124.41**
- Closed trades: **9** | Wins: **4** | Losses: **5** | Win rate: **44.44%**
- Max drawdown: **2.83%**
- Latest source close: **84,265.720000 USDT**
- USD/INR used this run: **96.8125**
- Last processed candle: `2026-10-07T07:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-05T18:59:59.999000+00:00`
- Entry price: **85,649.140000 USDT**
- Quantity (synthetic units): **0.0124882630**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-07T03:59:59.999000+00:00`
- Original OB candle open time: `2026-10-07T02:30:00+00:00`
- OB high / avg / low: **83857.120000 / 83828.560000 / 83800.000000**
- Move used by indicator: **0.3989%**

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
