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

my_restaurant = Restaurant('Bandidos', 'Mexican')

print(f"My restaurant's name is {my_restaurant.restaurant_name}.")
print(f"It serves {my_restaurant.cuisine_type} food.")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

am_restaurant = Restaurant('George\'s Kitchen', 'American')
fr_restaurant = Restaurant('Jean-Paul\'s Kitchen', 'French')
en_restaurant = Restaurant('Billy\'s Kitchen', 'English')

am_restaurant.describe_restaurant()
fr_restaurant.describe_restaurant()
en_restaurant.describe_restaurant()

new_restaurant = Restaurant('Bleeko', 'Jovian')
print(f"{new_restaurant.restaurant_name} has served {new_restaurant.number_served} customers.")

new_restaurant.number_served = 10
print(f"{new_restaurant.restaurant_name} has served {new_restaurant.number_served} customers.")

new_restaurant.set_number_served(20)
print(f"{new_restaurant.restaurant_name} has served {new_restaurant.number_served} customers.")

new_restaurant.increment_number_served(50)
print(f"{new_restaurant.restaurant_name} has served {new_restaurant.number_served} customers.")