
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

# This function is called with positional arguments.
# The arguments are passed in a specific order.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Here the function is called with keyword arguments.
# They clarify the role of each value in the function call.
describe_pet(animal_type='hamster', pet_name='harry')

# The function is rewritten with a default value for one of the parameters.
# NOTE: The order of the parameters in the function had to be changed.
# This is interpreted as a positional argument, in case the function is only called with a pet's name.
# So parameters with default values need to go after ones that don't, so Python can interpet positional arguments correctly.
def describe_pet(pet_name, animal_type='dog'):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster') # function still accepts explicit argument for animal_type.

describe_pet('willie') # also works
describe_pet('harry', 'hamster') # so does this
describe_pet(animal_type='hamster', pet_name='harry') # out of order but also works