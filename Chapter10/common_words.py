def count_common_words(filename):
	"""Count a common word in a file."""
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		# print(f"Sorry, the file {filename} does not exist.")
		pass
	else:
		# Count a common word in a file.
		total = contents.lower().count('the ')
		print(f"{filename} has {total} instances of the word 'the'.")

filenames = ['pride_and_prejudice.txt', 'ulysses.txt', 'baskervilles.txt']
for filename in filenames:
	count_common_words(filename)
	# print(f"{filename} has {total} words.")