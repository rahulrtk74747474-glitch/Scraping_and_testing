# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹101,450.35**
- Cash: **₹101,450.35**
- Total P&L: **₹1,450.35 (1.45%)**
- Realized P&L: **₹1,450.35**
- Unrealized P&L: **₹0.00**
- Closed trades: **10** | Wins: **4** | Losses: **6** | Win rate: **40.00%**
- Max drawdown: **3.24%**
- Latest source close: **82,694.000000 USDT**
- USD/INR used this run: **96.7800**
- Last processed candle: `2026-10-10T01:59:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-08T23:59:59.999000+00:00`
- Original OB candle open time: `2026-10-08T22:30:00+00:00`
- OB high / avg / low: **81930.010000 / 81858.880000 / 81787.750000**
- Move used by indicator: **0.2070%**

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
