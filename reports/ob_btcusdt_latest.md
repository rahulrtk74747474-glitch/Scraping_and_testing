# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,584.79**
- Cash: **₹0.00**
- Total P&L: **₹-3,415.21 (-3.42%)**
- Realized P&L: **₹-3,415.21**
- Unrealized P&L: **₹0.00**
- Closed trades: **14** | Wins: **5** | Losses: **9** | Win rate: **35.71%**
- Max drawdown: **7.88%**
- Latest source close: **82,302.000000 USDT**
- USD/INR used this run: **95.0450**
- Last processed candle: `2026-10-15T15:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-15T15:14:59.999000+00:00`
- Entry price: **82,302.000000 USDT**
- Quantity (synthetic units): **0.0123472170**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-15T15:14:59.999000+00:00`
- Original OB candle open time: `2026-10-15T13:45:00+00:00`
- OB high / avg / low: **80716.000000 / 80258.000000 / 79800.000000**
- Move used by indicator: **2.6096%**

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
