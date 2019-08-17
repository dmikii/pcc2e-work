filename = 'guest_book.txt'

prompt = "\nWhat is your name? "
prompt += "\nEnter 'quit' when done. "

while True:
	name = input(prompt)

	if name == 'quit':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(f"{name} has been added to the guest book.\n")

