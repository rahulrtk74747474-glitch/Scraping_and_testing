# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹98,774.31**
- Cash: **₹0.00**
- Total P&L: **₹-1,225.69 (-1.23%)**
- Realized P&L: **₹0.00**
- Unrealized P&L: **₹-1,225.69**
- Closed trades: **0** | Wins: **0** | Losses: **0** | Win rate: **0.00%**
- Max drawdown: **1.23%**
- Latest source close: **80,309.440000 USDT**
- USD/INR used this run: **95.8630**
- Last processed candle: `2026-09-20T06:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-19T23:29:59.999000+00:00`
- Entry price: **81,306.000000 USDT**
- Quantity (synthetic units): **0.0128299922**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-19T23:29:59.999000+00:00`
- Original OB candle open time: `2026-09-19T22:00:00+00:00`
- OB high / avg / low: **81100.420000 / 81031.210000 / 80962.000000**
- Move used by indicator: **0.3703%**

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
