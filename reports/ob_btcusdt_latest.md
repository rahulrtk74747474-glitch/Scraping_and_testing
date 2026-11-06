# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹92,029.27**
- Cash: **₹0.00**
- Total P&L: **₹-7,970.73 (-7.97%)**
- Realized P&L: **₹-7,416.66**
- Unrealized P&L: **₹-554.07**
- Closed trades: **29** | Wins: **8** | Losses: **21** | Win rate: **27.59%**
- Max drawdown: **12.22%**
- Latest source close: **75,728.000000 USDT**
- USD/INR used this run: **94.1675**
- Last processed candle: `2026-11-06T06:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-06T00:29:59.999000+00:00`
- Entry price: **76,183.930000 USDT**
- Quantity (synthetic units): **0.0129053098**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-06T00:29:59.999000+00:00`
- Original OB candle open time: `2026-11-05T23:00:00+00:00`
- OB high / avg / low: **75718.020000 / 75463.220000 / 75208.420000**
- Move used by indicator: **1.0271%**

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
