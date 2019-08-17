cities = {
	'Poik': {
		'country': 'pikanga',
		'population': 40000,
		'fact': 'perspicacious',
		},
	'Glimby': {
		'country': 'goravia',
		'population': 100000,
		'fact': 'gleaming',
		},
	'Fereenko': {
		'country': 'Framilton',
		'population': 75000,
		'fact': 'forensic',
		}
}

for city, info in cities.items():
	print(f"\nCity: {city.title()}")

	country = info['country']
	pop = info['population']
	fact = info['fact']

	print(f"\tCountry: {country.title()}")
	print(f"\tPopulation: {pop}")
	print(f"\tFact: {fact.title()}")