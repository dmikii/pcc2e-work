filename = 'programming.txt'

with open(filename, 'w') as file_object: 	# 'w' argument opens the file in write mode.
											# options are r, w, a, r+. with no arguments,
											# read-only is default.
											# write mode will erase contents of file before
											# returning the write file object, so be careful
											# with existing files.
											# Only strings can be written to a text file in Python.
											# To store numerical data, use str() function to convert.
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can be run in a browser.\n")