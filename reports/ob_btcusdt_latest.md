# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,578.07**
- Cash: **₹93,578.07**
- Total P&L: **₹-6,421.93 (-6.42%)**
- Realized P&L: **₹-6,421.93**
- Unrealized P&L: **₹0.00**
- Closed trades: **24** | Wins: **7** | Losses: **17** | Win rate: **29.17%**
- Max drawdown: **11.11%**
- Latest source close: **79,714.010000 USDT**
- USD/INR used this run: **95.2100**
- Last processed candle: `2026-10-29T02:44:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-29T01:14:59.999000+00:00`
- Original OB candle open time: `2026-10-28T23:45:00+00:00`
- OB high / avg / low: **81366.010000 / 81343.010000 / 81320.010000**
- Move used by indicator: **0.4415%**

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
