import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (existing behaviour preserved)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    # ------------------------------------------------------------------
    # Express service – $7.00 surcharge on top of standard
    # ------------------------------------------------------------------
    def test_express_local(self):
        # standard local for 2 kg = 8.0; express = 8.0 + 7.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional for 2 kg = 11.0; express = 11.0 + 7.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # standard local for 1.5 kg = 5 + 1.5*1.5 = 7.25; express = 14.25
        self.assertAlmostEqual(
            shipping_quote(1.5, "local", service="express"), 14.25
        )

    # ------------------------------------------------------------------
    # Input validation
    # ------------------------------------------------------------------
    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "intergalactic")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
