# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹84,035.19**
- Cash: **₹0.00**
- Total P&L: **₹-15,964.81 (-15.96%)**
- Realized P&L: **₹-17,836.64**
- Unrealized P&L: **₹1,871.83**
- Closed trades: **37** | Wins: **8** | Losses: **29** | Win rate: **21.62%**
- Max drawdown: **21.63%**
- Latest source close: **60,311.600000 USDT**
- USD/INR used this run: **92.6600**
- Last processed candle: `2026-11-21T19:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-21T12:44:59.999000+00:00`
- Entry price: **58,968.200000 USDT**
- Quantity (synthetic units): **0.0150372357**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-21T12:44:59.999000+00:00`
- Original OB candle open time: `2026-11-21T11:15:00+00:00`
- OB high / avg / low: **57960.050000 / 57910.250000 / 57860.450000**
- Move used by indicator: **1.7499%**

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
