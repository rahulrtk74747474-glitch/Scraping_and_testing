# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹103,264.14**
- Cash: **₹0.00**
- Total P&L: **₹3,264.14 (3.26%)**
- Realized P&L: **₹3,003.35**
- Unrealized P&L: **₹260.79**
- Closed trades: **9** | Wins: **4** | Losses: **5** | Win rate: **44.44%**
- Max drawdown: **2.00%**
- Latest source close: **85,865.990000 USDT**
- USD/INR used this run: **96.3000**
- Last processed candle: `2026-10-05T23:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-05T18:59:59.999000+00:00`
- Entry price: **85,649.140000 USDT**
- Quantity (synthetic units): **0.0124882630**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-05T22:29:59.999000+00:00`
- Original OB candle open time: `2026-10-05T21:00:00+00:00`
- OB high / avg / low: **85783.950000 / 85741.260000 / 85698.570000**
- Move used by indicator: **0.2983%**

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
