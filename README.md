# Vertex Chartink Paper Trader

This repository runs an automated **end-of-day paper portfolio** from a Chartink scanner (your Vertex condition), records every simulated order, estimates current Zerodha equity-delivery charges, and updates performance statistics after market hours.

## Strategy implemented

- Starting demo money: **₹1,00,000**.
- A stock enters when it appears in the configured Chartink scanner.
- Entry price: the **Chartink reported daily close** on the signal day.
- If there are **1–10 fresh stocks**, target initial allocation is **₹10,000 per stock**.
- If there are **more than 10 fresh stocks**, ₹1,00,000 is divided approximately equally among them.
- If existing trades have already used some cash, the fresh basket is scaled down equally so total paper cash never exceeds the ₹1,00,000 portfolio.
- On each later completed daily candle:
  - if `close > original entry price`, sell the entire position;
  - otherwise, attempt to add **10% of that position's original invested notional** at that day's close.
- Averaging is cash-limited. The engine records skipped averages/entries when the ₹1,00,000 demo portfolio has no sufficient cash.
- Whole shares only; no fractional shares.

> Research note: entering at the same closing price that caused an end-of-day scanner signal is an optimistic paper assumption because the close is only known after the candle completes. I kept it because it matches the requested rule. A later version can switch to next-session open for a more execution-realistic test.

## What the system records

`data/signals.csv`: Every daily Chartink match.

`data/orders.csv`: ENTRY, AVERAGE_ADD and EXIT orders with quantity, price, turnover, charges and cash flow.

`data/trades.csv`: Closed-trade ledger with gross/net P&L, charges, percentage return, holding period, number/amount of averages, and maximum capital in the trade.

`data/daily_snapshots.csv`: Cash, estimated liquidation equity, realized/unrealized P&L, total return, drawdown and open-position count.

`reports/latest.md`: Human-readable current report including win rate, winning/losing streaks, profit factor and open positions.

`app.py`: Optional Streamlit dashboard for viewing results locally or on Streamlit Community Cloud.

## Free data path

### Chartink

The program uses the same session/CSRF flow used by the Chartink screener page and POSTs the scanner clause to Chartink's screener processing endpoint. No paid data API is required.

For a public saved scanner, the code first tries to extract the `scan_clause` from its page. For a private scanner, the most reliable setup is to store the scanner clause itself as a GitHub Secret, so your Chartink password is **not needed**.

### Daily stock closes

Open positions are marked with daily NSE prices obtained through the free `yfinance` library. New entries prefer the close returned directly by Chartink.

## One-time setup

Open this repository on GitHub and go to:

**Settings → Secrets and variables → Actions → New repository secret**

Add:

1. `CHARTINK_SCAN_URL` — the full URL of your saved Vertex scanner, for example `https://chartink.com/screener/...`
2. `CHARTINK_SCAN_CLAUSE` — recommended, especially if the scanner is private. In Chrome while running the scanner: DevTools → Network → choose the request named `process` → Payload/Form Data → copy the value of `scan_clause`.
3. `CHARTINK_COOKIE` — optional. Only use this if your private scanner page cannot be accessed with the clause alone. Copy the full Cookie request header from a logged-in Chartink browser session. Cookies expire, so the clause-secret method is preferred.

**Do not put your Chartink ID/password, cookie, or clause into a public file or commit.**

Then go to **Actions → Vertex daily paper trade → Run workflow** once to test.

The workflow is scheduled for **16:45 IST, Monday–Friday**. On an NSE holiday it checks the latest NIFTY daily date and exits without changing the portfolio.

## Zerodha charge model

For NSE equity delivery the project estimates:

- brokerage: ₹0 for resident-individual delivery trades;
- STT: 0.1% on buy and sell;
- NSE transaction charge: 0.00307%;
- SEBI charge: ₹10/crore;
- GST: 18% on brokerage + SEBI + transaction charges;
- stamp duty: 0.015% on buy side;
- DP charge on delivery sell: ₹15.34 per scrip.

These are analytics estimates, not a replacement for a real contract note. Regulatory/exchange rates can change.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export CHARTINK_SCAN_URL="https://chartink.com/screener/your-scan"
export CHARTINK_SCAN_CLAUSE="( {cash} ( ... ) )"
python -m src.main
```

Optional dashboard:

```bash
streamlit run app.py
```

## Next phase: options

The codebase is intentionally separated into scanner, price, charge, strategy and reporting layers so stock-option data can be added without changing the portfolio engine.

Direct automated aggregation/scraping of the NSE option-chain webpage may conflict with the NSE site's stated Terms of Use and can also be blocked from cloud runners. The safer next phase is to plug in an authorized broker/data API (for example a broker option-chain endpoint) and store end-of-day option snapshots for each Vertex stock. Do not add credentials to the repository; use GitHub Actions Secrets.

## Important

This is a paper-trading/research system, not an order-placement bot and not investment advice. Before using real money, test for look-ahead bias, survivorship bias, corporate actions, slippage, liquidity, partial fills and data-source failures.
