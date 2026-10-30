# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,894.80**
- Cash: **₹0.00**
- Total P&L: **₹-4,105.20 (-4.11%)**
- Realized P&L: **₹-5,586.42**
- Unrealized P&L: **₹1,481.21**
- Closed trades: **7** | Wins: **1** | Losses: **6** | Win rate: **14.29%**
- Max drawdown: **6.37%**
- Latest source close: **23,102.800781 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-30T07:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-27T03:59:59.999000+00:00`
- Entry price: **22,745.949219 INR**
- Quantity (synthetic units): **4.1507867282**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-30T06:14:59.999000+00:00`
- Original OB candle open time: `2026-10-30T04:45:00+00:00`
- OB high / avg / low: **22938.599609 / 22921.849609 / 22905.099609**
- Move used by indicator: **0.5094%**

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
