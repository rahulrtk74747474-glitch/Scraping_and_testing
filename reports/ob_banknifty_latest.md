# BANKNIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,454.13**
- Cash: **₹96,454.13**
- Total P&L: **₹-3,545.87 (-3.55%)**
- Realized P&L: **₹-3,545.87**
- Unrealized P&L: **₹0.00**
- Closed trades: **2** | Wins: **1** | Losses: **1** | Win rate: **50.00%**
- Max drawdown: **4.21%**
- Latest source close: **54,714.101562 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-05T09:59:59.999000+00:00`

## Position

_Flat. Waiting for the next confirmed bullish order block._

## Latest detected order block

- Signal: **BEARISH_OB**
- Confirmation time: `2026-10-05T05:14:59.999000+00:00`
- Original OB candle open time: `2026-10-05T03:45:00+00:00`
- OB high / avg / low: **55191.250000 / 55015.949219 / 54840.648438**
- Move used by indicator: **0.5986%**

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
