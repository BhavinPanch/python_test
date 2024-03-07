import unittest
from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_scan_single_item(self):
        self.cart.scan("Apple")
        self.assertEqual(self.cart.calculate_total(), 0.60)

    def test_scan_multiple_items(self):
        self.cart.scan("Apple")
        self.cart.scan("Orange")
        self.assertEqual(self.cart.calculate_total(), 0.85)

    def test_scan_unknown_item(self):
        self.cart.scan("Banana")
        self.assertEqual(self.cart.calculate_total(), 0)


if __name__ == "__main__":
    unittest.main()
