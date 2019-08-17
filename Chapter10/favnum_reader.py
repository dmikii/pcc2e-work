import json

filename = 'favnum.json'
with open(filename) as f:
	fav_num = json.load(f)

print(fav_num)