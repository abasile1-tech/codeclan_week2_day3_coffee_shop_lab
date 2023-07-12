class Customer:
	def __init__(self, name, wallet, age):
		self.name = name
		self.wallet = wallet
		self.age = age

	def spend_money(self, amount):
		self.wallet -= amount
		return amount

	def buy_drink(self, drink):
		return self.spend_money(drink.price)