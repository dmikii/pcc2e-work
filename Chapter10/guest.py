filename = 'guest.txt' # If file doesn't exist already, it will be created when opened & written to.

name = input("What is your name? ")

with open(filename, 'w') as file_object:
	file_object.write(f"The first guest is {name}.")