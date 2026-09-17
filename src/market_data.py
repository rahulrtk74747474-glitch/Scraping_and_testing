from __future__ import annotations

from datetime import date
from typing import Iterable

import pandas as pd
import yfinance as yf


class MarketDataError(RuntimeError):
    pass


def _normalise_date_index(index_value) -> date:
    ts = pd.Timestamp(index_value)
    if ts.tzinfo is not None:
        ts = ts.tz_convert("Asia/Kolkata").tz_localize(None)
    return ts.date()


def latest_market_date() -> date:
    data = yf.download("^NSEI", period="10d", interval="1d", auto_adjust=False, progress=False, threads=False)
    if data is None or data.empty:
        raise MarketDataError("Could not fetch NIFTY 50 daily data from Yahoo Finance.")
    return _normalise_date_index(data.index[-1])


def latest_daily_closes(symbols: Iterable[str]) -> dict[str, dict]:
    result = {}
    for raw_symbol in sorted({s.strip().upper() for s in symbols if s and s.strip()}):
        ticker = f"{raw_symbol}.NS"
        try:
            hist = yf.Ticker(ticker).history(period="10d", interval="1d", auto_adjust=False, actions=False)
        except Exception:
            continue
        if hist is None or hist.empty:
            continue
        row = hist.iloc[-1]
        result[raw_symbol] = {"date": _normalise_date_index(hist.index[-1]), "open": float(row["Open"]), "high": float(row["High"]), "low": float(row["Low"]), "close": float(row["Close"])}
    return result
