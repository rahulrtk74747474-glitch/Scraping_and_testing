# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,378.57**
- Cash: **₹0.00**
- Total P&L: **₹-6,621.43 (-6.62%)**
- Realized P&L: **₹-6,621.43**
- Unrealized P&L: **₹0.00**
- Closed trades: **17** | Wins: **3** | Losses: **14** | Win rate: **17.65%**
- Max drawdown: **6.62%**
- Latest source close: **4,061.199951 USD**
- USD/INR used this run: **95.1900**
- Last processed candle: `2026-10-28T08:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-28T08:14:59.999000+00:00`
- Entry price: **4,061.199951 USD**
- Quantity (synthetic units): **0.2415469334**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-28T08:14:59.999000+00:00`
- Original OB candle open time: `2026-10-28T06:45:00+00:00`
- OB high / avg / low: **4043.899902 / 4042.799927 / 4041.699951**
- Move used by indicator: **0.4377%**

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
