from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Iterable
import requests

BASE_URL = "https://data-api.binance.vision"
KLINES_PATH = "/api/v3/klines"
INTERVAL_MS = 15 * 60 * 1000

@dataclass(frozen=True)
class Bar:
    open_time: int
    open: float
    high: float
    low: float
    close: float
    close_time: int

def _parse_rows(rows: Iterable[list]) -> list[Bar]:
    out = []
    now_ms = int(time.time() * 1000)
    for r in rows:
        b = Bar(int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), int(r[6]))
        if b.close_time < now_ms:
            out.append(b)
    return out

def fetch_recent_klines(symbol: str = "BTCUSDT", interval: str = "15m", limit: int = 1000) -> list[Bar]:
    resp = requests.get(BASE_URL + KLINES_PATH, params={"symbol": symbol, "interval": interval, "limit": min(max(int(limit), 1), 1000)}, timeout=20)
    resp.raise_for_status()
    return _parse_rows(resp.json())

def fetch_klines_from(start_time_ms: int, symbol: str = "BTCUSDT", interval: str = "15m", max_pages: int = 20) -> list[Bar]:
    rows = []
    cursor = int(start_time_ms)
    for _ in range(max_pages):
        resp = requests.get(BASE_URL + KLINES_PATH, params={"symbol": symbol, "interval": interval, "limit": 1000, "startTime": cursor}, timeout=20)
        resp.raise_for_status()
        page = _parse_rows(resp.json())
        if not page:
            break
        if rows and page[0].open_time <= rows[-1].open_time:
            page = [b for b in page if b.open_time > rows[-1].open_time]
        if not page:
            break
        rows.extend(page)
        if len(page) < 1000:
            break
        cursor = page[-1].open_time + 1
    return rows
