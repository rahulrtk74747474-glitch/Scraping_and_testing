# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹99,091.98**
- Cash: **₹0.00**
- Total P&L: **₹-908.02 (-0.91%)**
- Realized P&L: **₹-987.03**
- Unrealized P&L: **₹79.00**
- Closed trades: **1** | Wins: **0** | Losses: **1** | Win rate: **0.00%**
- Max drawdown: **1.17%**
- Latest source close: **23,140.500000 INR**
- Quote currency: **INR**
- Last processed candle: `2026-09-25T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-25T09:14:59.999000+00:00`
- Entry price: **23,122.050781 INR**
- Quantity (synthetic units): **4.2821882637**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-25T09:14:59.999000+00:00`
- Original OB candle open time: `2026-09-25T07:45:00+00:00`
- OB high / avg / low: **23043.000000 / 23036.825195 / 23030.650391**
- Move used by indicator: **0.3542%**

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
