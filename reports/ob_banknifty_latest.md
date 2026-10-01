# BANKNIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,871.34**
- Cash: **₹0.00**
- Total P&L: **₹-4,128.66 (-4.13%)**
- Realized P&L: **₹-3,927.32**
- Unrealized P&L: **₹-201.34**
- Closed trades: **1** | Wins: **0** | Losses: **1** | Win rate: **0.00%**
- Max drawdown: **4.21%**
- Latest source close: **54,450.750000 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-01T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-01T09:44:59.999000+00:00`
- Entry price: **54,565.101562 INR**
- Quantity (synthetic units): **1.7606981825**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-01T09:44:59.999000+00:00`
- Original OB candle open time: `2026-10-01T08:15:00+00:00`
- OB high / avg / low: **54294.648438 / 54237.673828 / 54180.699219**
- Move used by indicator: **0.7028%**

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

- Source: **yahoo / ^NSEBANK**.
- Note: NIFTY BANK index candles from Yahoo Finance. Paper units are synthetic index units, not exchange-tradable shares.

_Paper trading/research only; no real order is sent._
