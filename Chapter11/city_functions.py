def get_formatted_city(city, country, population=''):
	"""Generate a neatly formatted city name."""
	if population:
		city_name = f"{city}, {country} - population {population}"
	else:
		city_name = f"{city}, {country}"
	return city_name.title()