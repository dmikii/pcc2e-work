prompt = ("\nTell me something, and I will repeat it back to you:")
prompt += "\nEnter 'quit' to end the program. "

# This code block has a while loop to check for quit, and will not echo quit when it ends.

# message = ""
# while message != 'quit':
# 	message = input(prompt)
	
# 	if message != 'quit':
# 		print(message)

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)