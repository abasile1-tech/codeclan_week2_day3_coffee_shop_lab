import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def test_coffee_shop_has_name(self):
        coffee_shop = CoffeeShop("The Prancing Pony", 0, [])
        self.assertEqual("The Prancing Pony", coffee_shop.name)

    @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        pass