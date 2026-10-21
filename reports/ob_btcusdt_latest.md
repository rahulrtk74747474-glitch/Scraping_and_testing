# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,548.87**
- Cash: **₹0.00**
- Total P&L: **₹-4,451.13 (-4.45%)**
- Realized P&L: **₹-4,077.48**
- Unrealized P&L: **₹-373.65**
- Closed trades: **17** | Wins: **5** | Losses: **12** | Win rate: **29.41%**
- Max drawdown: **9.22%**
- Latest source close: **82,816.010000 USDT**
- USD/INR used this run: **94.5300**
- Last processed candle: `2026-10-21T04:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-20T21:14:59.999000+00:00`
- Entry price: **82,929.320000 USDT**
- Quantity (synthetic units): **0.0122051078**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-20T21:14:59.999000+00:00`
- Original OB candle open time: `2026-10-20T19:45:00+00:00`
- OB high / avg / low: **82614.010000 / 82593.005000 / 82572.000000**
- Move used by indicator: **0.3914%**

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
