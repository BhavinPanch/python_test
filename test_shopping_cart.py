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


class TestShoppingCartWithOffers(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_buy_one_get_one_free_on_apples(self):
        self.cart.scan('Apple')
        self.cart.scan('Apple')
        self.assertEqual(self.cart.calculate_total(), 0.60)

    def test_3_for_price_of_2_on_oranges(self):
        self.cart.scan('Orange')
        self.cart.scan('Orange')
        self.cart.scan('Orange')
        self.assertEqual(self.cart.calculate_total(), 0.50)

    def test_combined_offers(self):
        self.cart.scan('Apple')
        self.cart.scan('Apple')
        self.cart.scan('Orange')
        self.cart.scan('Apple')
        self.cart.scan('Orange')
        self.cart.scan('Orange')
        # Allow a small tolerance for rounding differences
        self.assertAlmostEqual(self.cart.calculate_total(), 1.7)

if __name__ == "__main__":
    unittest.main()
