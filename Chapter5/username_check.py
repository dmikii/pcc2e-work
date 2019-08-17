current_users = ['fred', 'keisha', 'andy', 'ellyn', 'jordan']

new_users = ['bobby', 'Andy', 'Ellyn', 'sam', 'chantel']

for user in new_users:
	if user.lower() in current_users:
		print('This username is already taken. Please enter a new username.')
	else:
		print('This username is available.')