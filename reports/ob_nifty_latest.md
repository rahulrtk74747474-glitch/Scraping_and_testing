# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹93,843.48**
- Cash: **₹0.00**
- Total P&L: **₹-6,156.52 (-6.16%)**
- Realized P&L: **₹-5,838.97**
- Unrealized P&L: **₹-317.55**
- Closed trades: **5** | Wins: **0** | Losses: **5** | Win rate: **0.00%**
- Max drawdown: **6.33%**
- Latest source close: **22,622.699219 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-14T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-13T09:44:59.999000+00:00`
- Entry price: **22,699.250000 INR**
- Quantity (synthetic units): **4.1482000557**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-13T09:44:59.999000+00:00`
- Original OB candle open time: `2026-10-13T08:15:00+00:00`
- OB high / avg / low: **22554.800781 / 22550.425781 / 22546.050781**
- Move used by indicator: **0.6641%**

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

- Source: **yahoo / ^NSEI**.
- Note: NIFTY 50 index candles from Yahoo Finance. Paper units are synthetic index units, not exchange-tradable shares.

_Paper trading/research only; no real order is sent._
