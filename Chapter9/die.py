from random import randint

class Die:
	"""A simple attempt to model a die."""
	def __init__(self):
		self.sides = 6

	def roll_die(self):
		roll = randint(1, self.sides)
		print(f"You rolled a {roll}.")

my_die = Die()
my_die.roll_die()

my_die.sides = 10
my_die.roll_die()

my_die.sides = 20
my_die.roll_die()