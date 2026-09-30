# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹103,170.00**
- Cash: **₹0.00**
- Total P&L: **₹3,170.00 (3.17%)**
- Realized P&L: **₹3,107.51**
- Unrealized P&L: **₹62.50**
- Closed trades: **5** | Wins: **1** | Losses: **4** | Win rate: **20.00%**
- Max drawdown: **2.00%**
- Latest source close: **83,766.010000 USDT**
- USD/INR used this run: **95.8200**
- Last processed candle: `2026-09-30T21:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-30T10:14:59.999000+00:00`
- Entry price: **83,706.530000 USDT**
- Quantity (synthetic units): **0.0128537381**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-30T10:14:59.999000+00:00`
- Original OB candle open time: `2026-09-30T08:45:00+00:00`
- OB high / avg / low: **83080.000000 / 83051.845000 / 83023.690000**
- Move used by indicator: **0.7755%**

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
