# BANKNIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,360.70**
- Cash: **₹0.00**
- Total P&L: **₹-3,639.30 (-3.64%)**
- Realized P&L: **₹-3,545.87**
- Unrealized P&L: **₹-93.43**
- Closed trades: **2** | Wins: **1** | Losses: **1** | Win rate: **50.00%**
- Max drawdown: **4.21%**
- Latest source close: **55,125.101562 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-09T05:44:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-09T04:44:59.999000+00:00`
- Entry price: **55,178.550781 INR**
- Quantity (synthetic units): **1.7480366246**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-09T04:44:59.999000+00:00`
- Original OB candle open time: `2026-10-08T09:30:00+00:00`
- OB high / avg / low: **54470.601562 / 54439.750000 / 54408.898438**
- Move used by indicator: **1.3124%**

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
