# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹99,847.97**
- Cash: **₹0.00**
- Total P&L: **₹-152.03 (-0.15%)**
- Realized P&L: **₹-2,199.32**
- Unrealized P&L: **₹2,047.29**
- Closed trades: **12** | Wins: **4** | Losses: **8** | Win rate: **33.33%**
- Max drawdown: **6.72%**
- Latest source close: **84,168.000000 USDT**
- USD/INR used this run: **95.2750**
- Last processed candle: `2026-10-13T08:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-13T01:59:59.999000+00:00`
- Entry price: **82,442.210000 USDT**
- Quantity (synthetic units): **0.0124512593**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-13T01:59:59.999000+00:00`
- Original OB candle open time: `2026-10-13T00:30:00+00:00`
- OB high / avg / low: **81469.290000 / 81365.050000 / 81260.810000**
- Move used by indicator: **1.2998%**

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
