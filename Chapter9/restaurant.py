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