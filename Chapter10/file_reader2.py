filename = 'pi_digits.txt'

with open(filename) as file_object: # common convention to assign filename to a variable.
	for line in file_object:
		print(line.rstrip()) # rstrip method removes extra blank lines.

with open(filename) as file_object:
	lines = file_object.readlines() # this method takes each line from the file and
									# stores it in a list. This allows access to a
									# file's contents outside of the with block.
for line in lines:
	print(line.rstrip())