# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹94,885.63**
- Cash: **₹0.00**
- Total P&L: **₹-5,114.37 (-5.11%)**
- Realized P&L: **₹-5,545.43**
- Unrealized P&L: **₹431.06**
- Closed trades: **4** | Wins: **0** | Losses: **4** | Win rate: **0.00%**
- Max drawdown: **5.72%**
- Latest source close: **22,562.449219 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-09T09:14:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-09T04:29:59.999000+00:00`
- Entry price: **22,459.949219 INR**
- Quantity (synthetic units): **4.2054666214**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-09T04:29:59.999000+00:00`
- Original OB candle open time: `2026-10-08T09:15:00+00:00`
- OB high / avg / low: **22226.150391 / 22213.650391 / 22201.150391**
- Move used by indicator: **1.1570%**

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
