class Dog: # In Python, it's customary to capitalize class names.
	"""A simple attempt to model a dog."""

	# Functions that are a part of a class are referred to as "methods."
	def __init__(self, name, age): 	# Special method for creating a new instance based on the class.
									# Self parameter is required, must come first.
									# It gives individual instance access to the class components.

		"""Initialize the name and age attributes."""
		self.name = name 	# Variables with self prefix are available to every method in the class.
							# Also accessible through any instance created from the class.
							# Variables that are accesible through instances are called "attributes."
		self.age = age

	# These methods don't require additional info, so they just have the "self" parameter.

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6) 	# Instance of "Dog" has been created, with arguments provided.
your_dog = Dog('Lucy', 3) 	# Can create multiple instances from one class.
							# As long as each instance has a unique variable name,
							# Or occupies a unique spot in a list or dictionary.					

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
