# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹94,864.43**
- Cash: **₹0.00**
- Total P&L: **₹-5,135.57 (-5.14%)**
- Realized P&L: **₹-6,169.84**
- Unrealized P&L: **₹1,034.27**
- Closed trades: **20** | Wins: **6** | Losses: **14** | Win rate: **30.00%**
- Max drawdown: **6.78%**
- Latest source close: **4,072.399902 USD**
- USD/INR used this run: **94.6300**
- Last processed candle: `2026-11-04T23:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-04T06:29:59.999000+00:00`
- Entry price: **4,028.000000 USD**
- Quantity (synthetic units): **0.2461637824**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-04T06:29:59.999000+00:00`
- Original OB candle open time: `2026-11-04T05:00:00+00:00`
- OB high / avg / low: **3962.699951 / 3959.449951 / 3956.199951**
- Move used by indicator: **1.7172%**

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

- Source: **yahoo / GC=F**.
- Note: COMEX Gold futures (Yahoo GC=F) 15-minute candles are used as a gold-price proxy for XAUUSDT because Binance's public Options API exposes the live XAUUSDT underlying index but not historical underlying-index OHLC klines. USD values are converted to INR for paper reporting.

_Paper trading/research only; no real order is sent._
