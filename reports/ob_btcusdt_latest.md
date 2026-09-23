# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹104,216.58**
- Cash: **₹0.00**
- Total P&L: **₹4,216.58 (4.22%)**
- Realized P&L: **₹4,074.84**
- Unrealized P&L: **₹141.74**
- Closed trades: **2** | Wins: **1** | Losses: **1** | Win rate: **50.00%**
- Max drawdown: **1.95%**
- Latest source close: **84,563.010000 USDT**
- USD/INR used this run: **95.7300**
- Last processed candle: `2026-09-23T22:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-23T19:44:59.999000+00:00`
- Entry price: **84,448.000000 USDT**
- Quantity (synthetic units): **0.0128738458**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-23T19:44:59.999000+00:00`
- Original OB candle open time: `2026-09-23T18:15:00+00:00`
- OB high / avg / low: **84203.360000 / 84173.265000 / 84143.170000**
- Move used by indicator: **0.3446%**

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
