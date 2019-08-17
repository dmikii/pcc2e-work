rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'mississipi': 'united states of america',
}

for river, country in rivers.items():
	print(f"The {river.title()} river is in {country.title()}.")

for river in rivers.keys():
	print(river.title())

for country in rivers.values():
	print(country.title())