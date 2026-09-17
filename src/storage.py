from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REPORT_DIR = ROOT / "reports"
STATE_PATH = DATA_DIR / "state.json"


def ensure_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)


def initial_state(starting_capital: float) -> dict:
    return {"version": 1, "starting_capital": round(float(starting_capital), 2), "cash": round(float(starting_capital), 2), "positions": {}, "realized_pnl": 0.0, "last_run_date": None, "equity_peak": round(float(starting_capital), 2), "max_drawdown_pct": 0.0, "max_capital_deployed": 0.0}


def load_state(starting_capital: float) -> dict:
    ensure_dirs()
    if not STATE_PATH.exists():
        return initial_state(starting_capital)
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    ensure_dirs()
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def append_csv(path: Path, rows: Iterable[dict], fieldnames: list[str]) -> None:
    rows = list(rows)
    if not rows:
        return
    ensure_dirs()
    exists = path.exists() and path.stat().st_size > 0
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerows(rows)
