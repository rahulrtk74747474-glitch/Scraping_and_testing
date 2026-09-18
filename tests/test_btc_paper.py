import unittest
from src.btc_paper import initial_state, process_events

class BtcPaperTests(unittest.TestCase):
    def test_long_target(self):
        s = initial_state(100)
        ev = [
            {"event":"dist_confirmed","cycle":1,"close_time":1000,"dir":"long","entry":100.0,"stop":95.0,"target":110.0},
            {"event":"outcome","cycle":1,"close_time":2000,"dir":"long","result":"target","exit":110.0,"entry":100.0,"stop":95.0,"target":110.0,"r":2.0},
        ]
        orders, trades = process_events(s, ev, fee_rate=0.0)
        self.assertEqual(len(orders), 2)
        self.assertEqual(len(trades), 1)
        self.assertAlmostEqual(s["balance"], 110.0)

    def test_short_target(self):
        s = initial_state(100)
        ev = [
            {"event":"dist_confirmed","cycle":2,"close_time":1000,"dir":"short","entry":100.0,"stop":105.0,"target":90.0},
            {"event":"outcome","cycle":2,"close_time":2000,"dir":"short","result":"target","exit":90.0,"entry":100.0,"stop":105.0,"target":90.0,"r":2.0},
        ]
        _, trades = process_events(s, ev, fee_rate=0.0)
        self.assertEqual(len(trades), 1)
        self.assertAlmostEqual(s["balance"], 110.0)

if __name__ == "__main__":
    unittest.main()
