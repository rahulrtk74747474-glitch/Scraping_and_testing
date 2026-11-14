# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹89,846.90**
- Cash: **₹0.00**
- Total P&L: **₹-10,153.10 (-10.15%)**
- Realized P&L: **₹-10,023.75**
- Unrealized P&L: **₹-129.35**
- Closed trades: **33** | Wins: **8** | Losses: **25** | Win rate: **24.24%**
- Max drawdown: **14.31%**
- Latest source close: **68,230.770000 USDT**
- USD/INR used this run: **94.2300**
- Last processed candle: `2026-11-14T01:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-14T00:29:59.999000+00:00`
- Entry price: **68,329.000000 USDT**
- Quantity (synthetic units): **0.0139744140**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-14T00:29:59.999000+00:00`
- Original OB candle open time: `2026-11-13T23:00:00+00:00`
- OB high / avg / low: **68254.010000 / 68082.505000 / 67911.000000**
- Move used by indicator: **0.4838%**

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
