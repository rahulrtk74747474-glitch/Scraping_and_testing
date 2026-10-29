# BANKNIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹95,180.70**
- Cash: **₹0.00**
- Total P&L: **₹-4,819.30 (-4.82%)**
- Realized P&L: **₹-5,072.28**
- Unrealized P&L: **₹252.99**
- Closed trades: **5** | Wins: **1** | Losses: **4** | Win rate: **20.00%**
- Max drawdown: **5.16%**
- Latest source close: **54,909.648438 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-29T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-29T08:44:59.999000+00:00`
- Entry price: **54,763.699219 INR**
- Quantity (synthetic units): **1.7334058215**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-29T08:44:59.999000+00:00`
- Original OB candle open time: `2026-10-29T07:15:00+00:00`
- OB high / avg / low: **54571.898438 / 54521.199219 / 54470.500000**
- Move used by indicator: **0.3743%**

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
