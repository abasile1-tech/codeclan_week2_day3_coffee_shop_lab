import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.mocha = Drink("Mocha",5)

    # A Drink should have a name, and a price
    def test_drink_has_name(self):
        self.assertEqual("Mocha", self.mocha.name)
    def test_drink_has_price(self):
        self.assertEqual(5, self.mocha.price)