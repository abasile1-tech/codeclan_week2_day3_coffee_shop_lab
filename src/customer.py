class Customer:
	def __init__(self, name, wallet):
		self.name = name
		self.wallet = wallet

	def spend_money(self, amount):
		wallet -= amount
		return amount

	def buy_drink(self, drink):
		self.spend_money(drink.price)