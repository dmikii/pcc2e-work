favorite_places = {
	'blinky': ['blookaville', 'boilty'],
	'spekto': ['ham'],
	'jolephus': ['jenira', 'totankus'],
	'croisty': ['curriga', 'doipang', 'ainchainka'],
}

for name, places in favorite_places.items():
	if len(places) > 1:
		print(f"\n{name.title()}'s favorite places are:")
	else:
		print(f"\n{name.title()}'s favorite place is:")

	for place in places:
		print(f"\t{place.title()}")