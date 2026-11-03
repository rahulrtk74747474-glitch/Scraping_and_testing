# XAUUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,218.93**
- Cash: **₹0.00**
- Total P&L: **₹-6,781.07 (-6.78%)**
- Realized P&L: **₹-6,535.11**
- Unrealized P&L: **₹-245.95**
- Closed trades: **18** | Wins: **4** | Losses: **14** | Win rate: **22.22%**
- Max drawdown: **6.78%**
- Latest source close: **3,910.600098 USD**
- USD/INR used this run: **94.7250**
- Last processed candle: `2026-11-03T09:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-02T11:44:59.999000+00:00`
- Entry price: **3,914.100098 USD**
- Quantity (synthetic units): **0.2516495241**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-03T00:29:59.999000+00:00`
- Original OB candle open time: `2026-11-02T23:00:00+00:00`
- OB high / avg / low: **3960.500000 / 3956.650024 / 3952.800049**
- Move used by indicator: **0.3567%**

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
