# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹97,283.33**
- Cash: **₹0.00**
- Total P&L: **₹-2,716.67 (-2.72%)**
- Realized P&L: **₹-4,037.97**
- Unrealized P&L: **₹1,321.30**
- Closed trades: **16** | Wins: **5** | Losses: **11** | Win rate: **31.25%**
- Max drawdown: **9.22%**
- Latest source close: **82,884.010000 USDT**
- USD/INR used this run: **94.8425**
- Last processed candle: `2026-10-19T07:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-17T21:14:59.999000+00:00`
- Entry price: **81,665.720000 USDT**
- Quantity (synthetic units): **0.0123755553**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-18T09:14:59.999000+00:00`
- Original OB candle open time: `2026-10-18T07:45:00+00:00`
- OB high / avg / low: **81700.850000 / 81682.255000 / 81663.660000**
- Move used by indicator: **0.3602%**

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
