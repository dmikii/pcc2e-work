destinations = {}

polling_active = True

while polling_active:
	name = input("Please tell me your name: ") 
	destination = input("\nIf you could visit one place in the world, where would you go? ")

	destinations[name] = destination

	repeat = input("Would you like someone else to take the poll? (yes/ no)")
	if repeat == 'no':
		polling_active = False

print("\n--- Here's the poll results! ---")
for name, destination in destinations.items():
	print(f"{name.title()} wants to visit {destination.title()}!")