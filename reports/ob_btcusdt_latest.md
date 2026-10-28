# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,980.78**
- Cash: **₹0.00**
- Total P&L: **₹-6,019.22 (-6.02%)**
- Realized P&L: **₹-6,207.44**
- Unrealized P&L: **₹188.22**
- Closed trades: **23** | Wins: **7** | Losses: **16** | Win rate: **30.43%**
- Max drawdown: **11.11%**
- Latest source close: **81,332.900000 USDT**
- USD/INR used this run: **95.2100**
- Last processed candle: `2026-10-28T19:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-28T08:14:59.999000+00:00`
- Entry price: **81,170.010000 USDT**
- Quantity (synthetic units): **0.0121364096**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-28T08:14:59.999000+00:00`
- Original OB candle open time: `2026-10-28T06:45:00+00:00`
- OB high / avg / low: **80935.570000 / 80896.825000 / 80858.080000**
- Move used by indicator: **0.3739%**

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
