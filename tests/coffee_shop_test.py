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
        self.steve = Customer("Steve", 100, 22)

    # A CoffeeShop should have a name, a till, and a collection of drinks containing 
    # instances of class Drink (Mocha, Latte, Hot Chocolate, Tea etc)
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(500, self.coffee_shop.till)

    def test_coffee_shop_has_drinks(self):
        self.assertEqual([self.mocha, self.latte, self.americano], self.coffee_shop.drinks)

    # A CoffeeShop should be able to sell a drink to a customer and increase it's till by the price of Drink. 
    # Hint: Use a Customer method you already have.
    def test_coffee_shop_can_sell_drink(self):
        self.coffee_shop.sell_drink(self.steve, self.latte)
        self.assertEqual(503, self.coffee_shop.till)
        self.assertEqual(97, self.steve.wallet)

    # Most coffee shops won't serve coffee to anyone under 16. Add an age to the Customer. 
    # Make sure the CoffeeShop checks the age before serving the Customer.
    @unittest.skip("Delete this line to run the test")
    def test_age(self):
        pass

    # Add a caffeine_level to the Drink, and an energy level to the Customer. 
    # Every time a Customer buys a drink, the energy level should go up by the caffeine_level.
    @unittest.skip("Delete this line to run the test")
    def test_caffeine(self):
        pass

    # CoffeeShop should refuse service to a Customer with an energy above a certain amount!
    @unittest.skip("Delete this line to run the test")
    def test_refuse_service(self):
        pass