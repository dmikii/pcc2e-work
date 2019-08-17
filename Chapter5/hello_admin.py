usernames = ['speth', 'gronki']

for user in usernames:
	if user == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {user}, thank you for logging in again.")

if usernames:
	for user in usernames:
		print(f"Hello {user}.")
else:
	print("We need to find some users!")