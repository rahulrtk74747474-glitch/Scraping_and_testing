from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ChargeBreakdown:
    brokerage: float = 0.0
    stt: float = 0.0
    transaction: float = 0.0
    sebi: float = 0.0
    stamp: float = 0.0
    gst: float = 0.0
    dp: float = 0.0

    @property
    def total(self) -> float:
        return round(
            self.brokerage
            + self.stt
            + self.transaction
            + self.sebi
            + self.stamp
            + self.gst
            + self.dp,
            2,
        )

    def to_dict(self) -> dict:
        data = asdict(self)
        data["total"] = self.total
        return data


# Zerodha resident-individual, NSE equity-delivery approximation.
# Rates checked against Zerodha's charges pages in September 2026.
NSE_TRANSACTION_RATE = 0.0000307      # 0.00307%
SEBI_RATE = 0.000001                  # Rs 10 / crore
STT_DELIVERY_RATE = 0.001             # 0.1%, both sides
STAMP_BUY_RATE = 0.00015              # 0.015%, buy side
GST_RATE = 0.18
DP_SELL_PER_SCRIP = 15.34             # Zerodha + CDSL + GST shown by Zerodha


def _round_money(value: float) -> float:
    return round(float(value), 2)


def equity_delivery_charges(turnover: float, side: str, include_dp: bool = False) -> ChargeBreakdown:
    """Approximate Zerodha NSE equity-delivery charges for one executed order.

    This is intended for paper-trading analytics, not contract-note reconciliation.
    """
    turnover = max(float(turnover), 0.0)
    side = side.lower().strip()
    if side not in {"buy", "sell"}:
        raise ValueError("side must be 'buy' or 'sell'")

    brokerage = 0.0
    stt = _round_money(turnover * STT_DELIVERY_RATE)
    transaction = _round_money(turnover * NSE_TRANSACTION_RATE)
    sebi = _round_money(turnover * SEBI_RATE)
    stamp = _round_money(turnover * STAMP_BUY_RATE) if side == "buy" else 0.0
    gst = _round_money((brokerage + transaction + sebi) * GST_RATE)
    dp = DP_SELL_PER_SCRIP if side == "sell" and include_dp else 0.0

    return ChargeBreakdown(
        brokerage=brokerage,
        stt=stt,
        transaction=transaction,
        sebi=sebi,
        stamp=stamp,
        gst=gst,
        dp=_round_money(dp),
    )
