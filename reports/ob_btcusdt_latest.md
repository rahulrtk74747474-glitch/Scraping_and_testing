# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹103,221.47**
- Cash: **₹0.00**
- Total P&L: **₹3,221.47 (3.22%)**
- Realized P&L: **₹-1,213.22**
- Unrealized P&L: **₹4,434.69**
- Closed trades: **1** | Wins: **0** | Losses: **1** | Win rate: **0.00%**
- Max drawdown: **1.95%**
- Latest source close: **85,080.580000 USDT**
- USD/INR used this run: **95.8050**
- Last processed candle: `2026-09-21T13:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-20T16:44:59.999000+00:00`
- Entry price: **81,376.010000 USDT**
- Quantity (synthetic units): **0.0126634322**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-21T11:59:59.999000+00:00`
- Original OB candle open time: `2026-09-21T10:30:00+00:00`
- OB high / avg / low: **84368.160000 / 84249.185000 / 84130.210000**
- Move used by indicator: **0.7414%**

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
