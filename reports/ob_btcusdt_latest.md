# BTCUSDT 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹100,995.18**
- Cash: **₹0.00**
- Total P&L: **₹995.18 (1.00%)**
- Realized P&L: **₹1,450.35**
- Unrealized P&L: **₹-455.17**
- Closed trades: **10** | Wins: **4** | Losses: **6** | Win rate: **40.00%**
- Max drawdown: **3.67%**
- Latest source close: **83,589.610000 USDT**
- USD/INR used this run: **95.7175**
- Last processed candle: `2026-10-12T09:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-11T05:14:59.999000+00:00`
- Entry price: **83,044.510000 USDT**
- Quantity (synthetic units): **0.0126228381**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-12T00:59:59.999000+00:00`
- Original OB candle open time: `2026-10-11T23:30:00+00:00`
- OB high / avg / low: **83728.000000 / 83709.845000 / 83691.690000**
- Move used by indicator: **0.3204%**

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
