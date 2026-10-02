# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹97,503.64**
- Cash: **₹0.00**
- Total P&L: **₹-2,496.36 (-2.50%)**
- Realized P&L: **₹-2,616.78**
- Unrealized P&L: **₹120.42**
- Closed trades: **5** | Wins: **1** | Losses: **4** | Win rate: **20.00%**
- Max drawdown: **3.41%**
- Latest source close: **4,210.700195 USD**
- USD/INR used this run: **96.3000**
- Last processed candle: `2026-10-02T08:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-02T03:59:59.999000+00:00`
- Entry price: **4,205.500000 USD**
- Quantity (synthetic units): **0.2404585301**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-02T03:59:59.999000+00:00`
- Original OB candle open time: `2026-10-02T02:30:00+00:00`
- OB high / avg / low: **4189.399902 / 4186.949951 / 4184.500000**
- Move used by indicator: **0.4778%**

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
