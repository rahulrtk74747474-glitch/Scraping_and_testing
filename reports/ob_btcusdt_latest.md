# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹90,183.26**
- Cash: **₹0.00**
- Total P&L: **₹-9,816.74 (-9.82%)**
- Realized P&L: **₹-9,841.70**
- Unrealized P&L: **₹24.95**
- Closed trades: **32** | Wins: **8** | Losses: **24** | Win rate: **25.00%**
- Max drawdown: **14.01%**
- Latest source close: **69,171.880000 USDT**
- USD/INR used this run: **94.2300**
- Last processed candle: `2026-11-13T14:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-13T07:14:59.999000+00:00`
- Entry price: **69,152.740000 USDT**
- Quantity (synthetic units): **0.0138358910**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-13T10:14:59.999000+00:00`
- Original OB candle open time: `2026-11-13T08:45:00+00:00`
- OB high / avg / low: **68780.900000 / 68749.185000 / 68717.470000**
- Move used by indicator: **1.0174%**

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
