# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹84,114.07**
- Cash: **₹0.00**
- Total P&L: **₹-15,885.93 (-15.89%)**
- Realized P&L: **₹-14,493.29**
- Unrealized P&L: **₹-1,392.64**
- Closed trades: **39** | Wins: **10** | Losses: **29** | Win rate: **25.64%**
- Max drawdown: **21.63%**
- Latest source close: **59,552.020000 USDT**
- USD/INR used this run: **92.9000**
- Last processed candle: `2026-11-24T16:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-24T04:29:59.999000+00:00`
- Entry price: **60,538.000000 USDT**
- Quantity (synthetic units): **0.0152039493**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-24T04:29:59.999000+00:00`
- Original OB candle open time: `2026-11-24T03:00:00+00:00`
- OB high / avg / low: **60074.900000 / 59824.665000 / 59574.430000**
- Move used by indicator: **1.5186%**

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
