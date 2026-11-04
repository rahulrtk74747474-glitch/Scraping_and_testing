# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,015.12**
- Cash: **₹0.00**
- Total P&L: **₹-6,984.88 (-6.98%)**
- Realized P&L: **₹-6,518.30**
- Unrealized P&L: **₹-466.59**
- Closed trades: **28** | Wins: **8** | Losses: **20** | Win rate: **28.57%**
- Max drawdown: **11.28%**
- Latest source close: **80,536.010000 USDT**
- USD/INR used this run: **94.6300**
- Last processed candle: `2026-11-04T23:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-04T22:44:59.999000+00:00`
- Entry price: **80,940.000000 USDT**
- Quantity (synthetic units): **0.0122049103**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-04T22:44:59.999000+00:00`
- Original OB candle open time: `2026-11-04T21:15:00+00:00`
- OB high / avg / low: **80278.000000 / 80189.000000 / 80100.000000**
- Move used by indicator: **1.0260%**

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
