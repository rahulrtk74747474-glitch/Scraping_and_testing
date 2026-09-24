# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹104,234.84**
- Cash: **₹0.00**
- Total P&L: **₹4,234.84 (4.23%)**
- Realized P&L: **₹3,963.92**
- Unrealized P&L: **₹270.92**
- Closed trades: **3** | Wins: **1** | Losses: **2** | Win rate: **33.33%**
- Max drawdown: **1.95%**
- Latest source close: **84,478.000000 USDT**
- USD/INR used this run: **95.9450**
- Last processed candle: `2026-09-24T17:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-24T13:59:59.999000+00:00`
- Entry price: **84,258.430000 USDT**
- Quantity (synthetic units): **0.0128601769**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-24T13:59:59.999000+00:00`
- Original OB candle open time: `2026-09-24T12:30:00+00:00`
- OB high / avg / low: **83550.010000 / 83448.335000 / 83346.660000**
- Move used by indicator: **0.9083%**

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
