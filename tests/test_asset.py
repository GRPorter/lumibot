import unittest
from lumibot.entities import Asset


class TestAsset(unittest.TestCase):
    def test_asset(self):

        assets = {}

        test_cases = dict(
            test_case_1=dict(
                symbol="SPY",
                asset_type="stock",
            ),
            test_case_2=dict(
                symbol="XYZ",
                asset_type="option",
                expiration="20000901",
                strike="145",
                right="CALL",
                multiplier=100,
            ),
        )

        for tc, tcattrs in test_cases.items():
            assets[tc] = Asset(**tcattrs)

        for tc, tcattrs in test_cases.items():
            for attr, param in tcattrs.items():
                self.assertEqual(param, assets[tc].__getattribute__(attr))




if __name__ == "__main__":
    unittest.main()
