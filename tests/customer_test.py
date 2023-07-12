import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.americano = Drink("Americano", 2)
        self.steve = Customer("Steve", 100, 22)

    # A Customer should have a name, and a wallet
    # A Customer should have method which reduces the wallet by a specified amount as a parameter
    # A Customer should be able to buy a Drink and reduce their wallet by the Drink's price.
    def test_customer_has_name(self):
        self.assertEqual("Steve", self.steve.name)
    def test_customer_has_wallet(self):
        self.assertEqual(100, self.steve.wallet)
    def test_spend_money_works(self):
        self.assertEqual(5, self.steve.spend_money(5))
        self.assertEqual(95, self.steve.wallet)
    def test_buy_drink_works(self):
        self.assertEqual(2, self.steve.buy_drink(self.americano))
        self.assertEqual(98, self.steve.wallet)