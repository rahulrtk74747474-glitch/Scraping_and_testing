# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹103,713.20**
- Cash: **₹0.00**
- Total P&L: **₹3,713.20 (3.71%)**
- Realized P&L: **₹3,857.29**
- Unrealized P&L: **₹-144.09**
- Closed trades: **4** | Wins: **1** | Losses: **3** | Win rate: **25.00%**
- Max drawdown: **1.95%**
- Latest source close: **83,960.010000 USDT**
- USD/INR used this run: **95.8020**
- Last processed candle: `2026-09-26T14:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-26T01:59:59.999000+00:00`
- Entry price: **84,076.660000 USDT**
- Quantity (synthetic units): **0.0128939788**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-26T10:59:59.999000+00:00`
- Original OB candle open time: `2026-09-26T09:30:00+00:00`
- OB high / avg / low: **84031.180000 / 84006.140000 / 83981.100000**
- Move used by indicator: **0.1915%**

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
