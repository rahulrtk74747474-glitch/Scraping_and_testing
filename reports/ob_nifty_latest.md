# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹106,147.76**
- Cash: **₹0.00**
- Total P&L: **₹6,147.76 (6.15%)**
- Realized P&L: **₹5,383.09**
- Unrealized P&L: **₹764.67**
- Closed trades: **10** | Wins: **4** | Losses: **6** | Win rate: **40.00%**
- Max drawdown: **6.37%**
- Latest source close: **25,514.300781 INR**
- Quote currency: **INR**
- Last processed candle: `2026-11-19T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-11-19T06:14:59.999000+00:00`
- Entry price: **25,330.500000 INR**
- Quantity (synthetic units): **4.1603240524**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-11-19T08:59:59.999000+00:00`
- Original OB candle open time: `2026-11-19T07:30:00+00:00`
- OB high / avg / low: **25374.250000 / 25359.400391 / 25344.550781**
- Move used by indicator: **0.4413%**

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
