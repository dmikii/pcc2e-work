# This code is done without functions.
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left.
# Move each design to completed models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

#Display all completed models:
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

#This same task will be done here with functions.

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)

# If we didn't want to empty the list of unprinted designs, we could do this:
# print_models(unprinted_designs[:], completed_models)
# The slice notation here makes a copy of the list to send to the function.
# The original list will be unaffected.
# Only keep a copy when needed - in most cases, the original list should be used.

show_completed_models(completed_models)
