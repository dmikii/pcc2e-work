def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f: # Using variable f to represent the file object.
													# Also using encoding argument to match encoding.
			contents = f.read()
	except FileNotFoundError:
		# print(f"Sorry, the file {filename} does not exist.") # This will report an exception that is visible.
		pass # This will fail silently and continue on. Can act as a placeholder to update later.
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

# Failing silently helps in cases where users don't need to know info they aren't looking for. If they are
# looking for/expecting sometihing, a message informing them why something wasn't found is helpful. 