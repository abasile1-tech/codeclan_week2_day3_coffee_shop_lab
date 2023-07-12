class CoffeeShop:
	def __init__(self, name, till, drinks):
		self.name = name
		self.till = till
		self.drinks = drinks

	def sell_drink(self, customer, drink):
		self.till += customer.buy_drink(drink)