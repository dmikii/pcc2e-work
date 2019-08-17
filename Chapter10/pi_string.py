filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	# pi_string += line.rstrip()
	pi_string += line.strip() # strip will remove extra whitespace from left side of each line.

print(pi_string)
print(len(pi_string))

# Note - when Python reads from a text file, it interprets all text as a string.
# So when reading in a number, it needs to be converted to an integer using int(),
# or to a float using float().