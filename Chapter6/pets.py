spiky = {
	'animal': 'hedgehog',
	'owner': 'henry',
}

slinky = {
	'animal': 'ferret',
	'owner': 'frank',
}

barky = {
	'animal': 'dog',
	'owner': 'dana',
}

pets = [spiky, slinky, barky]

for pet in pets:
	print(f"{pet['owner'].title()}\'s pet is a {pet['animal']}.")