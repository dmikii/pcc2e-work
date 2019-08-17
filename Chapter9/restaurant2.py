class Restaurant:
	"""A simple attempt to model a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is now open.")

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, number):
		self.number_served += number

class IceCreamStand(Restaurant):
	"""A simple attempt to model an ice cream stand, inheriting from Restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'strawberry']

	def show_flavors(self):
		for flavor in self.flavors:
			print(f"We have {flavor}.")

my_ice_cream_stand = IceCreamStand('Frosty\'s', 'ICS')
my_ice_cream_stand.show_flavors()

