# All Strategies — Trade Journal

_Aggregated automatically from each strategy branch. INR and USD results are kept separate._

## Summary

- Closed trade records: **15**
- Profits / losses: **7 / 8**
- Net INR P&L: **₹2,381.12**
- Net USD P&L: **$-0.4908**

## All closed trades

| Exit | Strategy | Symbol | Direction | Result | Net P&L | Return | Why closed |
|---|---|---|---|---|---:|---:|---|
| 2026-09-24 12:44:59 IST | OB NIFTY 15m | NIFTY | LONG | LOSS | ₹-987.03 | -0.9870% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.21702743149359446%. |
| 2026-09-24 05:44:59 IST | OB BTCUSDT 15m | BTCUSDT | LONG | LOSS | ₹-110.92 | -0.1066% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.242434605863716%. |
| 2026-09-23 14:59:59 IST | SMC NIFTY 15m | NIFTY | LONG | PROFIT | ₹51.50 | 0.1030% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |
| 2026-09-23 13:44:59 IST | SMC BANKNIFTY 15m | BANKNIFTY | LONG | PROFIT | ₹39.23 | 0.0785% | A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY. |
| 2026-09-23 10:59:59 IST | OB XAUUSDT 15m | XAUUSDT | LONG | LOSS | ₹-753.24 | -0.7532% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.11179079269419598%. |
| 2026-09-23 09:14:59 IST | BTCUSDT 15m | BTCUSDT | SHORT | LOSS | $-0.5954 | -0.5948% | Configured stop level was hit. |
| 2026-09-22 21:14:59 IST | BTCUSDT 15m | BTCUSDT | SHORT | LOSS | $-0.4613 | -0.4587% | Configured stop level was hit. |
| 2026-09-22 14:29:59 IST | BTCUSDT 15m | BTCUSDT | LONG | PROFIT | $0.8380 | 0.8402% | Configured profit target was hit. |
| 2026-09-22 06:44:59 IST | OB BTCUSDT 15m | BTCUSDT | LONG | PROFIT | ₹5,288.06 | 5.3530% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.9625836989147929%. |
| 2026-09-21 | Vertex 500 Daily | PFIZER | LONG | PROFIT | ₹33.37 | 0.4164% | A later completed daily close was above the original entry price, which is the configured Vertex exit rule. |
| 2026-09-21 | Vertex 500 3:15 | PFIZER | LONG | PROFIT | ₹33.37 | 0.4164% | A later completed daily close was above the original entry price, which is the configured Vertex exit rule. |
| 2026-09-20 20:44:59 IST | BTCUSDT 15m | BTCUSDT | SHORT | LOSS | $-0.5128 | -0.5116% | Configured stop level was hit. |
| 2026-09-20 16:29:59 IST | OB BTCUSDT 15m | BTCUSDT | LONG | LOSS | ₹-1,213.22 | -1.2132% | Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.28853411460919437%. |
| 2026-09-19 20:14:59 IST | BTCUSDT 15m | BTCUSDT | SHORT | LOSS | $-0.4243 | -0.4215% | Configured stop level was hit. |
| 2026-09-19 06:44:59 IST | BTCUSDT 15m | BTCUSDT | LONG | PROFIT | $0.6650 | 0.6650% | Configured profit target was hit. |

## Detailed journal

### OB NIFTY 15m — NIFTY — LOSS

- Trade ID: `OB_NIFTY-1-1789971299999`
- Branch: `ob-nifty-15m-paper`
- Entry: **2026-09-21 11:44:59 IST** at **23403.6504**
- Entry signal: **BULLISH_OB**
- Why taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.13242446490805995%.
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit: **2026-09-24 12:44:59 IST** at **23172.6504**
- Exit signal: **BEARISH_OB**
- Why closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.21702743149359446%.
- Quantity: **4.272837712532993**
- Gross P&L: **₹-987.03**
- Fees/charges: **₹0.00**
- Net P&L: **₹-987.03**
- Profit/Loss percentage: **-0.9870%**
- Holding period: **3d 1h 0m**
- Notes: Entry OB candle=2026-09-21 10:15:00 IST; exit OB candle=2026-09-24 11:15:00 IST; use_wicks=False; threshold=0.0%.

### OB BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `OB_BTCUSDT-3-1790192699999`
- Branch: `ob-btcusdt-15m-paper`
- Entry: **2026-09-24 01:14:59 IST** at **8084207.3235**
- Entry signal: **BULLISH_OB**
- Why taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.344578014617985%.
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit: **2026-09-24 05:44:59 IST** at **8075591.6232**
- Exit signal: **BEARISH_OB**
- Why closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.242434605863716%.
- Quantity: **0.01287384575013027**
- Gross P&L: **₹-110.92**
- Fees/charges: **₹0.00**
- Net P&L: **₹-110.92**
- Profit/Loss percentage: **-0.1066%**
- Holding period: **0d 4h 30m**
- Notes: Entry OB candle=2026-09-23 23:45:00 IST; exit OB candle=2026-09-24 04:15:00 IST; use_wicks=False; threshold=0%.

### SMC NIFTY 15m — NIFTY — PROFIT

- Trade ID: `SMC_NIFTY-1-1790155799999`
- Branch: `smc-nifty-15m-paper`
- Entry: **2026-09-23 10:29:59 IST** at **23398.3496**
- Entry signal: **CONFIRMED_PIVOT_LOW_BUY**
- Why taken: A confirmed major pivot low generated the BUY side of the SMC major-swing strategy. Position size follows the configured restore/50%/12.5% ladder rules.
- Stop: **Not used — this strategy reduces/exits on confirmed opposite major swings.**
- Target: **Not fixed — SELL decisions come from confirmed pivot-high signals.**
- Exit: **2026-09-23 14:59:59 IST** at **23422.4492**
- Exit signal: **CONFIRMED_PIVOT_HIGH_SELL**
- Why closed/reduced: A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY.
- Quantity: **2.1369028514714787**
- Gross P&L: **-**
- Fees/charges: **₹0.00**
- Net P&L: **₹51.50**
- Profit/Loss percentage: **0.1030%**
- Holding period: **0d 4h 30m**
- Notes: SMC uses scale-in/scale-out sizing. This row is a realized SELL slice; exit ladder step=0, fraction=%. A position can remain partly open after this journal row.

### SMC BANKNIFTY 15m — BANKNIFTY — PROFIT

- Trade ID: `SMC_BANKNIFTY-1-1790151299999`
- Branch: `smc-banknifty-15m-paper`
- Entry: **2026-09-23 10:29:59 IST** at **56523.1484**
- Entry signal: **CONFIRMED_PIVOT_LOW_BUY**
- Why taken: A confirmed major pivot low generated the BUY side of the SMC major-swing strategy. Position size follows the configured restore/50%/12.5% ladder rules.
- Stop: **Not used — this strategy reduces/exits on confirmed opposite major swings.**
- Target: **Not fixed — SELL decisions come from confirmed pivot-high signals.**
- Exit: **2026-09-23 13:44:59 IST** at **56567.5000**
- Exit signal: **CONFIRMED_PIVOT_HIGH_SELL**
- Why closed/reduced: A confirmed major pivot high generated a SELL. This realized slice used sizing rule RESTORE_LAST_BUY_QTY.
- Quantity: **0.8845933282589006**
- Gross P&L: **-**
- Fees/charges: **₹0.00**
- Net P&L: **₹39.23**
- Profit/Loss percentage: **0.0785%**
- Holding period: **0d 3h 15m**
- Notes: SMC uses scale-in/scale-out sizing. This row is a realized SELL slice; exit ladder step=0, fraction=%. A position can remain partly open after this journal row.

### OB XAUUSDT 15m — XAUUSDT — LOSS

- Trade ID: `OB_XAUUSDT-1-1789992899999`
- Branch: `ob-xauusdt-15m-paper`
- Entry: **2026-09-21 17:44:59 IST** at **422250.9490**
- Entry signal: **BULLISH_OB**
- Why taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.6163820793063561%.
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit: **2026-09-23 10:59:59 IST** at **419070.3719**
- Exit signal: **BEARISH_OB**
- Why closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.11179079269419598%.
- Quantity: **0.2368259923143178**
- Gross P&L: **₹-753.24**
- Fees/charges: **₹0.00**
- Net P&L: **₹-753.24**
- Profit/Loss percentage: **-0.7532%**
- Holding period: **1d 17h 15m**
- Notes: Entry OB candle=2026-09-21 16:15:00 IST; exit OB candle=2026-09-23 09:30:00 IST; use_wicks=False; threshold=0%.

### BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `BTCUSDT-1790089200000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-23 06:59:59 IST** at **86632.6800**
- Entry signal: **DISTRIBUTION_DOWN_CONFIRMED**
- Why taken: A confirmed distribution signal opened a SHORT after the strategy's sweep/distribution conditions.
- Stop: **86974.8700**
- Target: **85577.3000**
- Exit: **2026-09-23 09:14:59 IST** at **86974.8700**
- Exit signal: **STOP**
- Why closed/reduced: Configured stop level was hit.
- Quantity: **0.0011543523426639157**
- Gross P&L: **$-0.3950**
- Fees/charges: **$0.2004**
- Net P&L: **$-0.5954**
- Profit/Loss percentage: **-0.5948%**
- Holding period: **0d 2h 15m**
- Notes: Outcome=STOP; R multiple=-1.0; balance after=$99.5092.

### BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `BTCUSDT-1790066700000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-22 19:44:59 IST** at **86350.0100**
- Entry signal: **DISTRIBUTION_DOWN_CONFIRMED**
- Why taken: A confirmed distribution signal opened a SHORT after the strategy's sweep/distribution conditions.
- Stop: **86573.5400**
- Target: **85349.2700**
- Exit: **2026-09-22 21:14:59 IST** at **86573.5400**
- Exit signal: **STOP**
- Why closed/reduced: Configured stop level was hit.
- Quantity: **0.0011634675799293355**
- Gross P&L: **$-0.2601**
- Fees/charges: **$0.2012**
- Net P&L: **$-0.4613**
- Profit/Loss percentage: **-0.4587%**
- Holding period: **0d 1h 30m**
- Notes: Outcome=STOP; R multiple=-1.0; balance after=$100.1046.

### BTCUSDT 15m — BTCUSDT — PROFIT

- Trade ID: `BTCUSDT-1790039700000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-22 12:59:59 IST** at **85322.7100**
- Entry signal: **DISTRIBUTION_UP_CONFIRMED**
- Why taken: A confirmed distribution signal opened a LONG after the strategy's sweep/distribution conditions.
- Stop: **85095.1000**
- Target: **86211.8800**
- Exit: **2026-09-22 14:29:59 IST** at **86211.8800**
- Exit signal: **TARGET**
- Why closed/reduced: Configured profit target was hit.
- Quantity: **0.0011676647019865868**
- Gross P&L: **$1.0383**
- Fees/charges: **$0.2003**
- Net P&L: **$0.8380**
- Profit/Loss percentage: **0.8402%**
- Holding period: **0d 1h 30m**
- Notes: Outcome=TARGET; R multiple=3.906550678792654; balance after=$100.5659.

### OB BTCUSDT 15m — BTCUSDT — PROFIT

- Trade ID: `OB_BTCUSDT-2-1789922699999`
- Branch: `ob-btcusdt-15m-paper`
- Entry: **2026-09-20 22:14:59 IST** at **7800948.3622**
- Entry signal: **BULLISH_OB**
- Why taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.8786842731618274%.
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit: **2026-09-22 06:44:59 IST** at **8218533.2003**
- Exit signal: **BEARISH_OB**
- Why closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.9625836989147929%.
- Quantity: **0.012663432215771722**
- Gross P&L: **₹5,288.06**
- Fees/charges: **₹0.00**
- Net P&L: **₹5,288.06**
- Profit/Loss percentage: **5.3530%**
- Holding period: **1d 8h 30m**
- Notes: Entry OB candle=2026-09-20 20:45:00 IST; exit OB candle=2026-09-22 05:15:00 IST; use_wicks=False; threshold=0%.

### Vertex 500 Daily — PFIZER — PROFIT

- Trade ID: `VERTEX-PFIZER-2026-09-18-2026-09-21`
- Branch: `vertex-500-paper`
- Entry: **2026-09-18** at **4002.4000**
- Entry signal: **VERTEX_CHARTINK_SIGNAL**
- Why taken: Stock appeared in the configured Chartink/Vertex screener on the entry date. Scanner name: Pfizer Limited. Scanner change: -0.31%.
- Stop: **Not used — no fixed stop is configured.**
- Target: **Rule-based target: first later daily close above original entry price.**
- Exit: **2026-09-21** at **4035.7000**
- Exit signal: **DAILY_CLOSE_ABOVE_ORIGINAL_ENTRY**
- Why closed/reduced: A later completed daily close was above the original entry price, which is the configured Vertex exit rule.
- Quantity: **2**
- Gross P&L: **₹66.60**
- Fees/charges: **₹33.23**
- Net P&L: **₹33.37**
- Profit/Loss percentage: **0.4164%**
- Holding period: **3 day(s)**
- Notes: Average-add count: 0; average-added notional: ₹0.00; maximum capital in trade: ₹8,014.31.

### Vertex 500 3:15 — PFIZER — PROFIT

- Trade ID: `VERTEX-PFIZER-2026-09-18-2026-09-21`
- Branch: `vertex-500-315-paper`
- Entry: **2026-09-18** at **4002.4000**
- Entry signal: **VERTEX_CHARTINK_SIGNAL**
- Why taken: Stock appeared in the configured Chartink/Vertex screener on the entry date. Scanner name: Pfizer Limited. Scanner change: -0.31%.
- Stop: **Not used — no fixed stop is configured.**
- Target: **Rule-based target: first later daily close above original entry price.**
- Exit: **2026-09-21** at **4035.7000**
- Exit signal: **DAILY_CLOSE_ABOVE_ORIGINAL_ENTRY**
- Why closed/reduced: A later completed daily close was above the original entry price, which is the configured Vertex exit rule.
- Quantity: **2**
- Gross P&L: **₹66.60**
- Fees/charges: **₹33.23**
- Net P&L: **₹33.37**
- Profit/Loss percentage: **0.4164%**
- Holding period: **3 day(s)**
- Notes: Average-add count: 0; average-added notional: ₹0.00; maximum capital in trade: ₹8,014.31.

### BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `BTCUSDT-1789872300000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-20 19:44:59 IST** at **80592.0100**
- Entry signal: **DISTRIBUTION_DOWN_CONFIRMED**
- Why taken: A confirmed distribution signal opened a SHORT after the strategy's sweep/distribution conditions.
- Stop: **80843.2800**
- Target: **79794.3900**
- Exit: **2026-09-20 20:44:59 IST** at **80843.2800**
- Exit signal: **STOP**
- Why closed/reduced: Configured stop level was hit.
- Quantity: **0.0012425625890038253**
- Gross P&L: **$-0.3122**
- Fees/charges: **$0.2006**
- Net P&L: **$-0.5128**
- Profit/Loss percentage: **-0.5116%**
- Holding period: **0d 1h 0m**
- Notes: Outcome=STOP; R multiple=-1.0; balance after=$99.7279.

### OB BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `OB_BTCUSDT-1-1789860599999`
- Branch: `ob-btcusdt-15m-paper`
- Entry: **2026-09-20 04:59:59 IST** at **7794236.9936**
- Entry signal: **BULLISH_OB**
- Why taken: Confirmed bullish order block: the identified OB candle was the last down candle before 5 required up candles; entry executed at the confirmation-candle close. Detected move=0.3703305470791676%.
- Stop: **Not used — this strategy exits on a confirmed bearish order block.**
- Target: **Not fixed — position remains open until a confirmed bearish order block.**
- Exit: **2026-09-20 16:29:59 IST** at **7699675.8142**
- Exit signal: **BEARISH_OB**
- Why closed/reduced: Confirmed bearish order block: opposite OB signal closed the full long position at the confirmation-candle close. Detected move=0.28853411460919437%.
- Quantity: **0.01282999222138564**
- Gross P&L: **₹-1,213.22**
- Fees/charges: **₹0.00**
- Net P&L: **₹-1,213.22**
- Profit/Loss percentage: **-1.2132%**
- Holding period: **0d 11h 30m**
- Notes: Entry OB candle=2026-09-20 03:30:00 IST; exit OB candle=2026-09-20 15:00:00 IST; use_wicks=False; threshold=0%.

### BTCUSDT 15m — BTCUSDT — LOSS

- Trade ID: `BTCUSDT-1789780500000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-19 14:44:59 IST** at **81435.1100**
- Entry signal: **DISTRIBUTION_DOWN_CONFIRMED**
- Why taken: A confirmed distribution signal opened a SHORT after the strategy's sweep/distribution conditions.
- Stop: **81615.6200**
- Target: **80602.6700**
- Exit: **2026-09-19 20:14:59 IST** at **81615.6200**
- Exit signal: **STOP**
- Why closed/reduced: Configured stop level was hit.
- Quantity: **0.0012349029419191694**
- Gross P&L: **$-0.2229**
- Fees/charges: **$0.2014**
- Net P&L: **$-0.4243**
- Profit/Loss percentage: **-0.4215%**
- Holding period: **0d 5h 30m**
- Notes: Outcome=STOP; R multiple=-1.0; balance after=$100.2408.

### BTCUSDT 15m — BTCUSDT — PROFIT

- Trade ID: `BTCUSDT-1789753500000`
- Branch: `btcusdt-paper`
- Entry: **2026-09-19 05:44:59 IST** at **80976.0100**
- Entry signal: **DISTRIBUTION_UP_CONFIRMED**
- Why taken: A confirmed distribution signal opened a LONG after the strategy's sweep/distribution conditions.
- Stop: **80720.4100**
- Target: **81677.7100**
- Exit: **2026-09-19 06:44:59 IST** at **81677.7100**
- Exit signal: **TARGET**
- Why closed/reduced: Configured profit target was hit.
- Quantity: **0.001233699955086697**
- Gross P&L: **$0.8657**
- Fees/charges: **$0.2007**
- Net P&L: **$0.6650**
- Profit/Loss percentage: **0.6650%**
- Holding period: **0d 1h 0m**
- Notes: Outcome=TARGET; R multiple=2.745305164319388; balance after=$100.6650.
