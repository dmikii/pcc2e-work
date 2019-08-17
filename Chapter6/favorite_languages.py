favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is, {language}.")

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
# Looping through keys is default behavior when looping through a dictionary.
# So this would work too: for name in favorite_languages:	
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
#for language in favorite_languages.values():
# This will loop through the dictionary
# and print all values, even with duplicates. Use a set to identify unique items:
for language in set(favorite_languages.values()):
	print(language.title())

poll_takers = ['jen', 'edward', 'braef', 'gilcus']

for name in poll_takers:
	if name in favorite_languages:
		print(f"Hi {name.title()}, thank you for taking the poll.")
	else:
		print(f"Hi {name.title()}, please take the poll.")