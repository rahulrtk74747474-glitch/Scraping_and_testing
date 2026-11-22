# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹84,949.55**
- Cash: **₹0.00**
- Total P&L: **₹-15,050.45 (-15.05%)**
- Realized P&L: **₹-16,222.92**
- Unrealized P&L: **₹1,172.47**
- Closed trades: **38** | Wins: **9** | Losses: **29** | Win rate: **23.68%**
- Max drawdown: **21.63%**
- Latest source close: **60,636.950000 USDT**
- USD/INR used this run: **92.6600**
- Last processed candle: `2026-11-22T20:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-22T08:59:59.999000+00:00`
- Entry price: **59,800.040000 USDT**
- Quantity (synthetic units): **0.0151192917**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-22T11:59:59.999000+00:00`
- Original OB candle open time: `2026-11-22T10:30:00+00:00`
- OB high / avg / low: **60890.710000 / 60796.430000 / 60702.150000**
- Move used by indicator: **0.5012%**

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
