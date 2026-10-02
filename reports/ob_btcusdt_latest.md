# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹102,842.77**
- Cash: **₹102,842.77**
- Total P&L: **₹2,842.77 (2.84%)**
- Realized P&L: **₹2,842.77**
- Unrealized P&L: **₹0.00**
- Closed trades: **7** | Wins: **2** | Losses: **5** | Win rate: **28.57%**
- Max drawdown: **2.00%**
- Latest source close: **84,315.280000 USDT**
- USD/INR used this run: **96.3100**
- Last processed candle: `2026-10-02T19:59:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-02T14:59:59.999000+00:00`
- Original OB candle open time: `2026-10-02T13:30:00+00:00`
- OB high / avg / low: **87150.000000 / 86878.290000 / 86606.580000**
- Move used by indicator: **1.3963%**

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
