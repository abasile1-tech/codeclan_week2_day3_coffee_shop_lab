import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.mocha = Drink("Mocha",5)
        self.latte = Drink("Latte",3)
        self.americano = Drink("Americano", 2)
        self.drinks = [self.mocha, self.latte, self.americano]
        self.till = 500
        self.coffee_shop = CoffeeShop("The Prancing Pony", self.till, self.drinks)
        self.steve = Customer("Steve", 100)

    # A CoffeeShop should have a name, a till, and a collection of drinks containing 
    # instances of class Drink (Mocha, Latte, Hot Chocolate, Tea etc)
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(500, self.coffee_shop.till)

    def test_coffee_shop_has_drinks(self):
        self.assertEqual([self.mocha, self.latte, self.americano], self.coffee_shop.drinks)

    # A Drink should have a name, and a price
    def test_drink_has_name(self):
        self.assertEqual("Mocha", self.mocha.name)
    def test_drink_has_price(self):
        self.assertEqual(5, self.mocha.price)

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

    # A CoffeeShop should be able to sell a drink to a customer and increase it's till by the price of Drink. 
    # Hint: Use a Customer method you already have.
    def test_coffee_shop_can_sell_drink(self):
        self.coffee_shop.sell_drink(self.steve, self.latte)
        self.assertEqual(503, self.coffee_shop.till)
        self.assertEqual(97, self.steve.wallet)