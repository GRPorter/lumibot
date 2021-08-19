import unittest
import pandas as pd
from lumibot.entities import Asset, Bars

class TestBars(unittest.TestCase):
    def test_bars(self):
        df = pd.read_csv("tests/data/day_20bars.csv")
        df = df.set_index("date")
        df.index = pd.to_datetime(df.index)

        asset = Asset(symbol='SPY')
        bar = Bars(df, "testbroker", asset)


        self.assertEqual(bar.get_last_price(), 288.2900085449219)
        self.assertEqual(bar.get_last_dividend(), 0)
        self.assertEqual(bar.get_momentum(), 0.02535924309981552)
        self.assertEqual(bar.get_total_volume(), 1418326100)

if __name__ == "__main__":
    unittest.main()
