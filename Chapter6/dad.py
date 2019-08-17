dad_info = {
	'first_name': 'David',
	'last_name': 'D\'Amico',
	'age': 84,
	'city': 'Louisville',
}

nancy_info = {
	'first_name': 'Nancy',
	'last_name': 'Nickles',
	'age': 60,
	'city': 'Lewisburg',
}

steve_info = {
	'first_name': 'Steve',
	'last_name': 'D\'Amico',
	'age': 55,
	'city': 'Mebane',
}

people = [dad_info, nancy_info, steve_info]

for folks in people:
	print(f"{folks['first_name']} {folks['last_name']} is {folks['age']} years old, and lives in {folks['city']}.")

# print(f"Dad's name is {dad_info['first_name']} {dad_info['last_name']}. He is {dad_info['age']} and lives in {dad_info['city']}.")

