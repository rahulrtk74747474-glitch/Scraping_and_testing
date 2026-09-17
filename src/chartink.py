from __future__ import annotations

import html
import json
import os
import re
from http.cookies import SimpleCookie
from typing import Any

import requests
from bs4 import BeautifulSoup


PROCESS_URL = "https://chartink.com/screener/process"
DEFAULT_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)


class ChartinkError(RuntimeError):
    pass


def _apply_cookie_header(session: requests.Session, raw_cookie: str) -> None:
    jar = SimpleCookie()
    jar.load(raw_cookie)
    for key, morsel in jar.items():
        session.cookies.set(key, morsel.value, domain=".chartink.com")


def _decode_js_string(value: str) -> str:
    value = html.unescape(value)
    try:
        return json.loads(f'"{value}"')
    except Exception:
        return value.replace("\\/", "/").replace('\\"', '"').replace("\\'", "'")


def extract_scan_clause(page_html: str) -> str | None:
    soup = BeautifulSoup(page_html, "lxml")
    node = soup.select_one(
        "textarea[name='scan_clause'], textarea#scan_clause, "
        "input[name='scan_clause'], input#scan_clause"
    )
    if node:
        value = node.get("value") if node.name == "input" else node.get_text()
        if value and value.strip():
            return html.unescape(value).strip()

    patterns = [
        r'["\']scan_clause["\']\s*:\s*["\'](.+?)["\']\s*[,}]',
        r'scan_clause\s*=\s*["\'](.+?)["\']\s*;',
    ]
    for pattern in patterns:
        match = re.search(pattern, page_html, flags=re.IGNORECASE | re.DOTALL)
        if match:
            value = _decode_js_string(match.group(1)).strip()
            if value:
                return value
    return None


def fetch_chartink_signals(
    scan_url: str | None = None,
    scan_clause: str | None = None,
    raw_cookie: str | None = None,
    timeout: int = 30,
) -> list[dict[str, Any]]:
    """Run a Chartink saved scanner using its normal CSRF/session request flow."""
    scan_url = (scan_url or os.getenv("CHARTINK_SCAN_URL", "")).strip()
    scan_clause = (scan_clause or os.getenv("CHARTINK_SCAN_CLAUSE", "")).strip()
    raw_cookie = raw_cookie or os.getenv("CHARTINK_COOKIE", "")

    if not scan_url:
        raise ChartinkError("CHARTINK_SCAN_URL is missing.")

    with requests.Session() as session:
        session.headers.update({"User-Agent": DEFAULT_UA, "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8"})
        if raw_cookie:
            _apply_cookie_header(session, raw_cookie)

        page = session.get(scan_url, timeout=timeout)
        page.raise_for_status()
        if "/login" in page.url and not scan_clause:
            raise ChartinkError("Chartink redirected to login. Add CHARTINK_SCAN_CLAUSE as a GitHub Secret or provide a valid CHARTINK_COOKIE secret.")

        soup = BeautifulSoup(page.text, "lxml")
        csrf_node = soup.select_one("[name='csrf-token']")
        if not csrf_node or not csrf_node.get("content"):
            raise ChartinkError("Could not find Chartink CSRF token.")
        csrf = csrf_node["content"]

        if not scan_clause:
            scan_clause = extract_scan_clause(page.text)
        if not scan_clause:
            raise ChartinkError("Could not extract scan_clause. For a private scanner, copy scan_clause from the browser Network request named 'process' and save it as CHARTINK_SCAN_CLAUSE.")

        headers = {"X-CSRF-TOKEN": csrf, "X-Requested-With": "XMLHttpRequest", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Referer": scan_url, "User-Agent": DEFAULT_UA}
        response = session.post(PROCESS_URL, data={"scan_clause": scan_clause}, headers=headers, timeout=timeout)
        response.raise_for_status()
        try:
            payload = response.json()
        except ValueError as exc:
            raise ChartinkError(f"Chartink returned non-JSON content (HTTP {response.status_code}).") from exc
        if "data" not in payload:
            raise ChartinkError(f"Unexpected Chartink response keys: {list(payload)[:10]}")

        out = []
        for row in payload.get("data") or []:
            symbol = str(row.get("nsecode") or "").strip().upper()
            if not symbol:
                continue
            try:
                close = float(row.get("close"))
            except (TypeError, ValueError):
                close = 0.0
            out.append({"symbol": symbol, "name": row.get("name") or symbol, "close": close, "change_pct": row.get("per_chg"), "volume": row.get("volume"), "raw": row})
        return out
