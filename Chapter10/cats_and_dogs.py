def show_contents(filename):
	"""Show the contents of a file."""
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		# print(f"Sorry, the file {filename} does not exist.")
		pass
	else:
		# Show the contents of the file.
		print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	show_contents(filename)