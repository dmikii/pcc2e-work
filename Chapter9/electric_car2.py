class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize the attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odomoter reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def upgrade_battery(self):
		self.battery_size = 100

	def get_range(self):
		"""Print a statement aabout the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car): # See above - parent class must be part of the current file
						# and appear before the child class.
						# Parent class must be included in () in the child class def.
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)	# super function allows you to call a method
											# from the parent class - in this case, __init__.
		self.battery = Battery() # creates new instance of Battery and assigns it to the self.battery attribute.

	#If class Car had a fill_gas_tank() method, this would override it:
	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # look at my_tesla instance, find its battery attribute,
									# and call the describe_battery() method associated with
									# the Battery instance stored in the attribute.
my_tesla.battery.get_range()

my_toyota = ElectricCar('toyota', 'rav4', 2019)
print(my_toyota.get_descriptive_name())
my_toyota.battery.get_range()
my_toyota.battery.upgrade_battery()
my_toyota.battery.get_range()