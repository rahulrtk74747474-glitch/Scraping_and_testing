# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,567.80**
- Cash: **₹0.00**
- Total P&L: **₹-6,432.20 (-6.43%)**
- Realized P&L: **₹-6,785.48**
- Unrealized P&L: **₹353.28**
- Closed trades: **25** | Wins: **7** | Losses: **18** | Win rate: **28.00%**
- Max drawdown: **11.11%**
- Latest source close: **77,299.870000 USDT**
- USD/INR used this run: **94.9400**
- Last processed candle: `2026-10-31T08:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-30T20:29:59.999000+00:00`
- Entry price: **77,008.010000 USDT**
- Quantity (synthetic units): **0.0127496548**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-30T20:29:59.999000+00:00`
- Original OB candle open time: `2026-10-30T19:00:00+00:00`
- OB high / avg / low: **76661.130000 / 76548.505000 / 76435.880000**
- Move used by indicator: **0.6009%**

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
