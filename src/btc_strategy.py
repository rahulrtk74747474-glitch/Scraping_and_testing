from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from .btc_market import Bar

RANGE_WIN = 20
PIVOT_LR = 3
PIVOT_CAP = 60

@dataclass(frozen=True)
class StrategyParams:
    min_range_bars: int = 12
    max_range_bars: int = 96
    compression_pct: int = 25
    stat_window: int = 200
    range_tolerance: float = 0.10
    min_range_width_pct: float = 0.15
    trim_tail_pct: int = 15
    sweep_return_bars: int = 6
    dist_timeout_bars: int = 64
    stop_buf_atr: float = 0.4
    fib_ext: float = 1.5
    tick_size: float = 0.01

class Phase(str, Enum):
    IDLE = "idle"
    ACCUM = "accum"
    SWEEP = "sweepPending"
    DIST = "dist"

def _rma(values: list[float], length: int) -> list[Optional[float]]:
    out: list[Optional[float]] = [None] * len(values)
    if len(values) < length:
        return out
    seed = sum(values[:length]) / length
    out[length - 1] = seed
    prev = seed
    alpha = 1.0 / length
    for i in range(length, len(values)):
        prev = alpha * values[i] + (1 - alpha) * prev
        out[i] = prev
    return out

def _true_ranges(bars: list[Bar]) -> list[float]:
    tr = []
    for i, b in enumerate(bars):
        if i == 0:
            tr.append(b.high - b.low)
        else:
            pc = bars[i - 1].close
            tr.append(max(b.high - b.low, abs(b.high - pc), abs(b.low - pc)))
    return tr

def _atr14(bars: list[Bar]) -> list[Optional[float]]:
    return _rma(_true_ranges(bars), 14)

def _percent_rank(values: list[Optional[float]], idx: int, length: int) -> Optional[float]:
    if idx - length + 1 < 0 or values[idx] is None:
        return None
    window = values[idx - length + 1:idx + 1]
    if any(v is None for v in window):
        return None
    cur = float(values[idx])
    return 100.0 * sum(float(v) <= cur for v in window) / length

def _pivots(bars: list[Bar]) -> tuple[list[Optional[float]], list[Optional[float]]]:
    ph: list[Optional[float]] = [None] * len(bars)
    pl: list[Optional[float]] = [None] * len(bars)
    lr = PIVOT_LR
    for confirm in range(2 * lr, len(bars)):
        c = confirm - lr
        hs = [bars[j].high for j in range(c - lr, c + lr + 1)]
        ls = [bars[j].low for j in range(c - lr, c + lr + 1)]
        hv, lv = bars[c].high, bars[c].low
        if hv == max(hs) and hs.count(hv) == 1:
            ph[confirm] = hv
        if lv == min(ls) and ls.count(lv) == 1:
            pl[confirm] = lv
    return ph, pl

def _round_tick(p: float, tick: float) -> float:
    return round(round(p / tick) * tick, 10)

def _tick_out(p: float, round_up: bool, tick: float) -> float:
    import math
    q = p / tick
    return round((math.ceil(q) if round_up else math.floor(q)) * tick, 10)

def compute_events(bars: list[Bar], p: StrategyParams = StrategyParams()) -> list[dict]:
    if len(bars) < p.stat_window + RANGE_WIN + 5:
        return []

    atr = _atr14(bars)
    ph, pl = _pivots(bars)
    hi20: list[Optional[float]] = [None] * len(bars)
    lo20: list[Optional[float]] = [None] * len(bars)
    chw: list[Optional[float]] = [None] * len(bars)
    for i in range(RANGE_WIN - 1, len(bars)):
        w = bars[i - RANGE_WIN + 1:i + 1]
        hi20[i] = max(x.high for x in w)
        lo20[i] = min(x.low for x in w)
        chw[i] = hi20[i] - lo20[i]

    piv_hi: list[tuple[int, float]] = []
    piv_lo: list[tuple[int, float]] = []
    state = Phase.IDLE
    last_end_i = -100
    cycle_id = 0
    range_high = range_low = range_mid = range_width = tol_px = None
    range_start_i = expiry_anchor_i = None
    atr_anchor = None
    sweep_side = 0
    sweep_extreme = None
    sweep_i = None
    dist_dir = 0
    entry = stop = target = risk_r = None
    dist_i = None
    events = []

    for i, b in enumerate(bars):
        if ph[i] is not None:
            piv_hi.append((i - PIVOT_LR, float(ph[i])))
            piv_hi = piv_hi[-PIVOT_CAP:]
        if pl[i] is not None:
            piv_lo.append((i - PIVOT_LR, float(pl[i])))
            piv_lo = piv_lo[-PIVOT_CAP:]

        warmed = i >= p.stat_window + RANGE_WIN
        pr = _percent_rank(chw, i, p.stat_window) if chw[i] is not None else None
        inside = range_high is not None and range_low <= b.close <= range_high
        tol = tol_px or 0.0
        breach_high = range_high is not None and b.high > range_high + tol
        breach_low = range_low is not None and b.low < range_low - tol

        if state == Phase.IDLE:
            if warmed and b.close > 0 and pr is not None and pr <= p.compression_pct and chw[i] is not None and chw[i] >= p.min_range_width_pct / 100.0 * b.close and i - last_end_i >= 10:
                win_last = RANGE_WIN - 1
                t_hi = float(hi20[i])
                t_lo = float(lo20[i])
                if p.trim_tail_pct > 0:
                    keep = True
                    while keep and win_last > p.min_range_bars:
                        subset = bars[i - (win_last - 1):i + 1]
                        hi2 = max(x.high for x in subset)
                        lo2 = min(x.low for x in subset)
                        if (t_hi - t_lo) - (hi2 - lo2) > p.trim_tail_pct / 100.0 * (t_hi - t_lo):
                            win_last -= 1
                            t_hi, t_lo = hi2, lo2
                        else:
                            keep = False
                cand_start = i - win_last
                cand_high, cand_low = t_hi, t_lo
                hi_candidates = [v for idx, v in piv_hi if idx >= cand_start]
                lo_candidates = [v for idx, v in piv_lo if idx >= cand_start]
                if hi_candidates:
                    cand_high = max(hi_candidates)
                if lo_candidates:
                    cand_low = min(lo_candidates)
                cand_w = cand_high - cand_low
                if cand_w >= p.min_range_width_pct / 100.0 * b.close and cand_low <= b.close <= cand_high:
                    range_start_i = cand_start
                    expiry_anchor_i = cand_start
                    range_high, range_low, range_width = cand_high, cand_low, cand_w
                    tol_px = cand_w * p.range_tolerance
                    range_mid = (cand_high + cand_low) / 2.0
                    anchor_idx = i - (win_last + 1)
                    aa = atr[anchor_idx] if anchor_idx >= 0 else None
                    atr_anchor = aa if aa is not None and aa > 0 else max(b.high - b.low, p.tick_size)
                    cycle_id = int(bars[range_start_i].open_time)
                    state = Phase.ACCUM
            continue

        if state == Phase.ACCUM:
            range_age = i - range_start_i
            if i - expiry_anchor_i > p.max_range_bars:
                state = Phase.IDLE
                last_end_i = i
                continue
            if breach_high and breach_low:
                state = Phase.IDLE
                last_end_i = i
                continue
            if breach_high or breach_low:
                side = 1 if breach_high else -1
                if range_age < p.min_range_bars:
                    state = Phase.IDLE
                    last_end_i = i
                    continue
                sweep_side = side
                sweep_i = i
                sweep_extreme = b.high if side == 1 else b.low
                events.append({"event":"sweep","cycle":cycle_id,"bar_index":i,"close_time":b.close_time,"side":"HIGH" if side == 1 else "LOW","price":b.close})
                state = Phase.SWEEP
                if inside:
                    dist_dir = 1 if sweep_side == -1 else -1
                    entry = b.close
                    fib_leg = (range_high - sweep_extreme) if dist_dir == 1 else (sweep_extreme - range_low)
                    target = _round_tick(range_high + (p.fib_ext - 1.0) * fib_leg if dist_dir == 1 else range_low - (p.fib_ext - 1.0) * fib_leg, p.tick_size)
                    stop_raw = sweep_extreme - p.stop_buf_atr * atr_anchor if dist_dir == 1 else sweep_extreme + p.stop_buf_atr * atr_anchor
                    stop = _tick_out(stop_raw, dist_dir == -1, p.tick_size)
                    risk_r = max(abs(entry - stop), p.tick_size)
                    reward_ok = target - entry >= p.tick_size if dist_dir == 1 else entry - target >= p.tick_size
                    if not reward_ok:
                        state = Phase.IDLE
                        last_end_i = i
                        continue
                    dist_i = i
                    state = Phase.DIST
                    events.append({"event":"dist_confirmed","cycle":cycle_id,"bar_index":i,"close_time":b.close_time,"dir":"long" if dist_dir == 1 else "short","entry":entry,"stop":stop,"target":target,"rr":abs(target-entry)/risk_r})
                continue

            if ph[i] is not None:
                pivot_idx = i - PIVOT_LR
                if pivot_idx >= range_start_i and ph[i] > range_high and ph[i] <= range_high + tol:
                    range_high = float(ph[i])
                    range_width = range_high - range_low
                    range_mid = (range_high + range_low) / 2.0
            if pl[i] is not None:
                pivot_idx = i - PIVOT_LR
                if pivot_idx >= range_start_i and pl[i] < range_low and pl[i] >= range_low - tol:
                    range_low = float(pl[i])
                    range_width = range_high - range_low
                    range_mid = (range_high + range_low) / 2.0
            continue

        if state == Phase.SWEEP:
            if sweep_side == 1:
                sweep_extreme = max(sweep_extreme, b.high)
            else:
                sweep_extreme = min(sweep_extreme, b.low)
            opp = b.low < range_low - tol if sweep_side == 1 else b.high > range_high + tol
            if opp:
                state = Phase.IDLE
                last_end_i = i
                continue
            if i - sweep_i > p.sweep_return_bars:
                state = Phase.IDLE
                last_end_i = i
                continue
            if inside:
                dist_dir = 1 if sweep_side == -1 else -1
                entry = b.close
                fib_leg = (range_high - sweep_extreme) if dist_dir == 1 else (sweep_extreme - range_low)
                target = _round_tick(range_high + (p.fib_ext - 1.0) * fib_leg if dist_dir == 1 else range_low - (p.fib_ext - 1.0) * fib_leg, p.tick_size)
                stop_raw = sweep_extreme - p.stop_buf_atr * atr_anchor if dist_dir == 1 else sweep_extreme + p.stop_buf_atr * atr_anchor
                stop = _tick_out(stop_raw, dist_dir == -1, p.tick_size)
                risk_r = max(abs(entry - stop), p.tick_size)
                reward_ok = target - entry >= p.tick_size if dist_dir == 1 else entry - target >= p.tick_size
                if not reward_ok:
                    state = Phase.IDLE
                    last_end_i = i
                    continue
                dist_i = i
                state = Phase.DIST
                events.append({"event":"dist_confirmed","cycle":cycle_id,"bar_index":i,"close_time":b.close_time,"dir":"long" if dist_dir == 1 else "short","entry":entry,"stop":stop,"target":target,"rr":abs(target-entry)/risk_r})
            continue

        if state == Phase.DIST:
            if i - dist_i >= 1:
                hit_t = b.high >= target if dist_dir == 1 else b.low <= target
                hit_s = b.low <= stop if dist_dir == 1 else b.high >= stop
                timed = i - dist_i >= p.dist_timeout_bars
                if hit_t or hit_s or timed:
                    if hit_t and hit_s:
                        result = "ambiguous_stop"
                        exit_price = min(stop, b.open) if dist_dir == 1 else max(stop, b.open)
                        r_mult = -1.0
                    elif hit_t:
                        result = "target"
                        exit_price = max(target, b.open) if dist_dir == 1 else min(target, b.open)
                        r_mult = abs(exit_price - entry) / risk_r
                    elif hit_s:
                        result = "stop"
                        exit_price = min(stop, b.open) if dist_dir == 1 else max(stop, b.open)
                        r_mult = (exit_price - entry) / risk_r if dist_dir == 1 else (entry - exit_price) / risk_r
                    else:
                        result = "timeout"
                        exit_price = b.close
                        r_mult = (b.close - entry) / risk_r if dist_dir == 1 else (entry - b.close) / risk_r
                    events.append({"event":"outcome","cycle":cycle_id,"bar_index":i,"close_time":b.close_time,"dir":"long" if dist_dir == 1 else "short","result":result,"exit":exit_price,"entry":entry,"stop":stop,"target":target,"r":r_mult})
                    state = Phase.IDLE
                    last_end_i = i
            continue
    return events
