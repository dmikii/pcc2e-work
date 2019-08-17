import json

prompt = input("What is your favorite number? ")

filename = 'favnum.json'
with open(filename, 'w') as f:
	json.dump(prompt, f)