# BANKNIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹100,045.56**
- Cash: **₹0.00**
- Total P&L: **₹45.56 (0.05%)**
- Realized P&L: **₹0.00**
- Unrealized P&L: **₹45.56**
- Closed trades: **0** | Wins: **0** | Losses: **0** | Win rate: **0.00%**
- Max drawdown: **0.04%**
- Latest source close: **56,548.898438 INR**
- Quote currency: **INR**
- Last processed candle: `2026-09-23T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-09-23T04:59:59.999000+00:00`
- Entry price: **56,523.148438 INR**
- Quantity (synthetic units): **1.7691866565**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-09-23T04:59:59.999000+00:00`
- Original OB candle open time: `2026-09-22T09:45:00+00:00`
- OB high / avg / low: **56280.949219 / 56248.250000 / 56215.550781**
- Move used by indicator: **0.5472%**

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
