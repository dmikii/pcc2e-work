def build_profile(first, last, **user_info): 	# Double asterisks before a parameter 
												# causes Python to create an empty dictionary.
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

user_profile = build_profile('ken', 'd\'amico', location='raleigh', age=48, hobby='learning')
print(user_profile)