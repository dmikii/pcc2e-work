glossary = {
	'list': 'Enclosed in square brackets',
	'tuple': 'Enclosed in parentheses', 
	'dictionary': 'Enclosed in curly brackets',
	'conditional_test': 'Evaluates to true or false',
	'range': 'Function that generates a series of numbers',
}

# print(f"List\n\t{glossary['list']}")
# print(f"Tuple\n\t{glossary['tuple']}")
# print(f"Dictionary\n\t{glossary['dictionary']}")
# print(f"Conditional Test\n\t{glossary['conditional_test']}")
# print(f"Range\n\t{glossary['range']}")

for word, definition in glossary.items():
	print(f"{word.title()}\n\t{definition}")

glossary['key-value pair'] = 'A set of values associated with each other.'
glossary['del'] = 'Removes a key-value pair in a dictionary when providing the key name.'
glossary['get method'] = 'Provide key name and set a default value to be returned if the key doesn\'t exist.'
glossary['sorted function'] = 'Sorts and loops keys in a particular order.'

for word, definition in glossary.items():
	print(f"{word.title()}\n\t{definition}")