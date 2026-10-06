# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹103,215.73**
- Cash: **₹0.00**
- Total P&L: **₹3,215.73 (3.22%)**
- Realized P&L: **₹3,003.35**
- Unrealized P&L: **₹212.38**
- Closed trades: **9** | Wins: **4** | Losses: **5** | Win rate: **44.44%**
- Max drawdown: **2.00%**
- Latest source close: **85,718.930000 USDT**
- USD/INR used this run: **96.4200**
- Last processed candle: `2026-10-06T16:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-05T18:59:59.999000+00:00`
- Entry price: **85,649.140000 USDT**
- Quantity (synthetic units): **0.0124882630**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-06T08:44:59.999000+00:00`
- Original OB candle open time: `2026-10-06T07:15:00+00:00`
- OB high / avg / low: **85376.010000 / 85336.410000 / 85296.810000**
- Move used by indicator: **0.7675%**

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
