filename = 'alice.txt'

try:
	with open(filename, encoding='utf-8') as f: # Using variable f to represent the file object.
											# Also using encoding argument to match encoding.
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")