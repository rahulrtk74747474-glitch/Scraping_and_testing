# NIFTY 15m Order-Block Paper Trader — Latest

- Starting demo money: **₹100,000.00**
- Current equity: **₹96,614.77**
- Cash: **₹0.00**
- Total P&L: **₹-3,385.23 (-3.39%)**
- Realized P&L: **₹-4,787.19**
- Unrealized P&L: **₹1,401.96**
- Closed trades: **3** | Wins: **0** | Losses: **3** | Win rate: **0.00%**
- Max drawdown: **5.06%**
- Latest source close: **22,776.099609 INR**
- Quote currency: **INR**
- Last processed candle: `2026-10-06T09:59:59.999000+00:00`

## Position

- Status: **LONG / fully invested**
- Entry time: `2026-10-01T09:44:59.999000+00:00`
- Entry price: **22,445.599609 INR**
- Quantity (synthetic units): **4.2419367092**

## Latest detected order block

- Signal: **BULLISH_OB**
- Confirmation time: `2026-10-01T09:44:59.999000+00:00`
- Original OB candle open time: `2026-10-01T08:15:00+00:00`
- OB high / avg / low: **22295.650391 / 22271.549805 / 22247.449219**
- Move used by indicator: **0.8882%**

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
