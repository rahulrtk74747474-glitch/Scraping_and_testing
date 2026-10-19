# BANKNIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,929.12**
- Cash: **₹0.00**
- Total P&L: **₹-4,070.88 (-4.07%)**
- Realized P&L: **₹-4,360.41**
- Unrealized P&L: **₹289.52**
- Closed trades: **4** | Wins: **1** | Losses: **3** | Win rate: **25.00%**
- Max drawdown: **4.59%**
- Latest source close: **55,565.851562 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-19T07:29:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-13T09:14:59.999000+00:00`
- Entry price: **55,398.148438 INR**
- Quantity (synthetic units): **1.7264041567**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-15T05:14:59.999000+00:00`
- Original OB candle open time: `2026-10-15T03:45:00+00:00`
- OB high / avg / low: **55445.750000 / 55364.425781 / 55283.101562**
- Move used by indicator: **0.6609%**

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
