# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹100,150.19**
- Cash: **₹0.00**
- Total P&L: **₹150.19 (0.15%)**
- Realized P&L: **₹0.00**
- Unrealized P&L: **₹150.19**
- Closed trades: **0** | Wins: **0** | Losses: **0** | Win rate: **0.00%**
- Max drawdown: **0.43%**
- Latest source close: **23,438.800781 INR**
- Quote currency: **INR**
- Last processed candle: `2026-09-23T06:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-21T06:14:59.999000+00:00`
- Entry price: **23,403.650391 INR**
- Quantity (synthetic units): **4.2728377125**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-21T06:14:59.999000+00:00`
- Original OB candle open time: `2026-09-21T04:45:00+00:00`
- OB high / avg / low: **23373.650391 / 23366.200195 / 23358.750000**
- Move used by indicator: **0.1324%**

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
