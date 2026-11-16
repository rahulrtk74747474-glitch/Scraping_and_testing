# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹85,624.40**
- Cash: **₹85,624.40**
- Total P&L: **₹-14,375.60 (-14.38%)**
- Realized P&L: **₹-14,375.60**
- Unrealized P&L: **₹0.00**
- Closed trades: **36** | Wins: **8** | Losses: **28** | Win rate: **22.22%**
- Max drawdown: **18.33%**
- Latest source close: **65,188.010000 USDT**
- USD/INR used this run: **94.2300**
- Last processed candle: `2026-11-16T02:59:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-11-15T14:44:59.999000+00:00`
- Original OB candle open time: `2026-11-15T13:15:00+00:00`
- OB high / avg / low: **65800.750000 / 65675.380000 / 65550.010000**
- Move used by indicator: **1.4213%**

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
