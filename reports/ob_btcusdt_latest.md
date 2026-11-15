# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹87,625.01**
- Cash: **₹0.00**
- Total P&L: **₹-12,374.99 (-12.37%)**
- Realized P&L: **₹-12,286.89**
- Unrealized P&L: **₹-88.11**
- Closed trades: **34** | Wins: **8** | Losses: **26** | Win rate: **23.53%**
- Max drawdown: **16.42%**
- Latest source close: **64,834.810000 USDT**
- USD/INR used this run: **94.2300**
- Last processed candle: `2026-11-15T05:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-15T02:59:59.999000+00:00`
- Entry price: **64,900.000000 USDT**
- Quantity (synthetic units): **0.0143426904**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-15T02:59:59.999000+00:00`
- Original OB candle open time: `2026-11-15T01:30:00+00:00`
- OB high / avg / low: **62560.650000 / 62330.325000 / 62100.000000**
- Move used by indicator: **4.5026%**

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
