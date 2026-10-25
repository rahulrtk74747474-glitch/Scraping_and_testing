# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,450.16**
- Cash: **₹0.00**
- Total P&L: **₹-3,549.84 (-3.55%)**
- Realized P&L: **₹-3,556.39**
- Unrealized P&L: **₹6.54**
- Closed trades: **19** | Wins: **6** | Losses: **13** | Win rate: **31.58%**
- Max drawdown: **9.22%**
- Latest source close: **80,611.070000 USDT**
- USD/INR used this run: **94.9300**
- Last processed candle: `2026-10-25T16:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-24T22:59:59.999000+00:00`
- Entry price: **80,605.600000 USDT**
- Quantity (synthetic units): **0.0126038949**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-24T22:59:59.999000+00:00`
- Original OB candle open time: `2026-10-24T21:30:00+00:00`
- OB high / avg / low: **80469.750000 / 80411.660000 / 80353.570000**
- Move used by indicator: **0.3137%**

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
