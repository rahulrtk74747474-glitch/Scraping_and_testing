import unittest
from datetime import date

from src.charges import equity_delivery_charges
from src.engine import StrategyConfig, process_day, target_initial_allocation
from src.storage import initial_state


class EngineTests(unittest.TestCase):
    def test_allocation_rule(self):
        cfg = StrategyConfig()
        self.assertEqual(target_initial_allocation(5, cfg), 10000)
        self.assertEqual(target_initial_allocation(10, cfg), 10000)
        self.assertEqual(target_initial_allocation(20, cfg), 5000)

    def test_entry_average_exit_cycle(self):
        cfg = StrategyConfig()
        state = initial_state(100000)

        state, orders, trades, skipped = process_day(
            state,
            [{"symbol": "AAA", "name": "AAA", "close": 100.0}],
            {"AAA": {"date": date(2026, 9, 17), "close": 100.0}},
            "2026-09-17",
            cfg,
        )
        self.assertEqual(orders[0]["event"], "ENTRY")
        self.assertEqual(state["positions"]["AAA"]["qty"], 100)

        state, orders, trades, skipped = process_day(
            state,
            [],
            {"AAA": {"date": date(2026, 9, 18), "close": 99.0}},
            "2026-09-18",
            cfg,
        )
        self.assertEqual(orders[0]["event"], "AVERAGE_ADD")
        self.assertEqual(state["positions"]["AAA"]["average_add_count"], 1)

        state, orders, trades, skipped = process_day(
            state,
            [],
            {"AAA": {"date": date(2026, 9, 21), "close": 101.0}},
            "2026-09-21",
            cfg,
        )
        self.assertEqual(orders[0]["event"], "EXIT")
        self.assertEqual(len(trades), 1)
        self.assertNotIn("AAA", state["positions"])
        self.assertGreater(trades[0]["net_pnl"], 0)

    def test_delivery_charges_have_dp_on_sell_only(self):
        buy = equity_delivery_charges(10000, "buy")
        sell = equity_delivery_charges(10000, "sell", include_dp=True)
        self.assertEqual(buy.dp, 0)
        self.assertGreater(sell.dp, 0)
        self.assertGreater(buy.stamp, 0)
        self.assertEqual(sell.stamp, 0)


if __name__ == "__main__":
    unittest.main()
