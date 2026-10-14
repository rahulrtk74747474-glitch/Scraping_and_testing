# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,958.22**
- Cash: **₹0.00**
- Total P&L: **₹-3,041.78 (-3.04%)**
- Realized P&L: **₹-1,010.61**
- Unrealized P&L: **₹-2,031.17**
- Closed trades: **13** | Wins: **5** | Losses: **8** | Win rate: **38.46%**
- Max drawdown: **7.52%**
- Latest source close: **81,800.740000 USDT**
- USD/INR used this run: **95.1400**
- Last processed candle: `2026-10-14T19:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-14T03:44:59.999000+00:00`
- Entry price: **83,820.530000 USDT**
- Quantity (synthetic units): **0.0124584566**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-14T03:44:59.999000+00:00`
- Original OB candle open time: `2026-10-14T02:15:00+00:00`
- OB high / avg / low: **83357.550000 / 83322.775000 / 83288.000000**
- Move used by indicator: **0.6123%**

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
