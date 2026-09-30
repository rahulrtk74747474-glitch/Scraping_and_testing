# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,469.19**
- Cash: **₹0.00**
- Total P&L: **₹-3,530.81 (-3.53%)**
- Realized P&L: **₹-3,204.35**
- Unrealized P&L: **₹-326.47**
- Closed trades: **2** | Wins: **0** | Losses: **2** | Win rate: **0.00%**
- Max drawdown: **3.71%**
- Latest source close: **22,620.449219 INR**
- Quote currency: **INR**
- Last processed candle: `2026-09-30T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-29T05:59:59.999000+00:00`
- Entry price: **22,697.000000 INR**
- Quantity (synthetic units): **4.2646893448**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-30T03:59:59.999000+00:00`
- Original OB candle open time: `2026-09-29T08:45:00+00:00`
- OB high / avg / low: **22672.000000 / 22663.075195 / 22654.150391**
- Move used by indicator: **0.2424%**

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
