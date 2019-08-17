import json

filename = 'favnum.json'
try:
	with open(filename) as f:
		fav_num = json.load(f)
except FileNotFoundError:
	fav_num = input("What is your favorite number? ")
	with open(filename, 'w') as f:
		json.dump(fav_num, f)
		print(f"We'll remember your favorite number as {fav_num}!")
else:
	print(f"Your favorite number is {fav_num}, right?")