# Vertex Chartink Paper Trader

This repository runs an automated **end-of-day paper portfolio** from your Chartink Vertex scanner, records every simulated order, estimates Zerodha equity-delivery charges, and updates performance statistics after market hours.

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
- Averaging is cash-limited. The engine records skipped averages/entries when the ₹1,00,000 demo portfolio has insufficient cash.
- Whole shares only; no fractional shares.

> Research note: entering at the same closing price that caused an end-of-day scanner signal is an optimistic paper assumption because the close is only known after the candle completes. The project can later add a next-session-open execution mode for comparison.

## What the system records

- `data/signals.csv`: every daily Chartink match.
- `data/orders.csv`: ENTRY, AVERAGE_ADD and EXIT orders with quantity, price, turnover, charges and cash flow.
- `data/trades.csv`: closed-trade ledger with gross/net P&L, charges, percentage return, holding period, averaging count/amount, and maximum capital in the trade.
- `data/daily_snapshots.csv`: cash, estimated liquidation equity, realized/unrealized P&L, total return, drawdown and open-position count.
- `reports/latest.md`: current human-readable report including win rate, winning/losing streaks, profit factor and open positions.
- `app.py`: optional Streamlit dashboard.

## Chartink data: real web scraping

The project now uses **Playwright + headless Chromium** to open Chartink like a browser and scrape the rendered stock-results table. It does **not** require `scan_clause` and does not call Chartink's hidden screener-processing endpoint directly.

Configured scanner:

`https://chartink.com/screener/rahul-606569`

For a private scanner, authentication is required. The scraper supports either:

1. `CHARTINK_USER` + `CHARTINK_PASSWORD` GitHub Actions secrets; or
2. `CHARTINK_COOKIE` containing the full Cookie request header from an already logged-in Chartink browser session.

Credentials/cookies are never written to CSV files, reports, or source code.

### One-time GitHub setup for the private scanner

Open:

**Repository → Settings → Secrets and variables → Actions → New repository secret**

Add:

- `CHARTINK_USER` = your Chartink login email/user ID
- `CHARTINK_PASSWORD` = your Chartink password

You do **not** need a `CHARTINK_SCAN_CLAUSE` secret anymore.

Alternative: instead of login/password you can add `CHARTINK_COOKIE`, but browser cookies expire, so login secrets are generally more durable.

Do not post these values in an issue, commit, README, or other public repository content.

Then open:

**Actions → Vertex daily paper trade → Run workflow**

The workflow installs Chromium automatically and runs the scraper in a free GitHub-hosted runner.

## Daily schedule

The workflow is scheduled for **16:45 IST, Monday–Friday**. On an NSE holiday it checks the latest NIFTY daily date and exits without modifying the portfolio.

## Daily stock prices

Open positions are marked with daily NSE prices through the free `yfinance` library. Fresh entries prefer the daily close scraped from Chartink.

## Zerodha charge model

For NSE equity delivery the project estimates:

- brokerage: ₹0 for resident-individual delivery trades;
- STT: 0.1% on buy and sell;
- NSE transaction charge: 0.00307%;
- SEBI charge: ₹10/crore;
- GST: 18% on brokerage + SEBI + transaction charges;
- stamp duty: 0.015% on buy side;
- DP charge on delivery sell: ₹15.34 per scrip.

These are analytics estimates and not a replacement for a real contract note. Regulatory/exchange rates can change.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium

export CHARTINK_SCAN_URL="https://chartink.com/screener/rahul-606569"
export CHARTINK_USER="your-chartink-login"
export CHARTINK_PASSWORD="your-chartink-password"
python -m src.main
```

Optional dashboard:

```bash
streamlit run app.py
```

## Next phase: stock options

The scanner, market-data, charge, strategy and reporting layers are separated so we can add an options-data module next. The intended next step is to capture the relevant stock's option-chain snapshot when a Vertex stock appears, then paper-test stock-vs-option execution separately.

## Important

This is a paper-trading/research system, not an order-placement bot and not investment advice. Before using real money, test for look-ahead bias, survivorship bias, corporate actions, slippage, liquidity, partial fills and data-source failures.
