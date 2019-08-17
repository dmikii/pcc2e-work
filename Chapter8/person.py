def build_person(first_name, last_name, age=None): # age is optional parameter, set to None as placeholder.
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
#if function call includes value for age, it will be stored in the dictionary
musician = build_person('jimi', 'hendrix', age=27)
print(musician)