import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

# A Drink should have a name, and a price
# A CoffeeShop should have a name, a till, and a collection of drinks containing 
# instances of class Drink (Mocha, Latte, Hot Chocolate, Tea etc)
# A Customer should have a name, and a wallet
# A Customer should have method which reduces the wallet by a specified amount as a parameter
# A Customer should be able to buy a Drink and reduce their wallet by the Drink's price.
# A CoffeeShop should be able to sell a drink to a customer and increase it's till by the price of Drink. 
# Hint: Use a Customer method you already have.

mocha = Drink("Mocha",5)
latte = Drink("Latte",3)
americano = Drink("Americano", 2)
drinks = [mocha, latte, americano]
till = 500
coffee_shop = CoffeeShop("The Prancing Pony", till, drinks)

class TestCoffeeShop(unittest.TestCase):
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(500, coffee_shop.till)