favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	'jakey': ['javascript'],
}

for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print(f"\n{name.title()}'s favorite languages are:")
	else:
		print(f"\n{name.title()}'s favorite language is:")
	
	for language in languages:
		print(f"\t{language.title()}")