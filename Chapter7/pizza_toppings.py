prompt = ("\nPlease enter the pizza toppings you want on your pizza.")
prompt += ("\nWhen you're done, enter 'quit'. ")

# This code block quits when user types quit, but quit is displayed:
#
# while message != 'quit':
#	message = input(prompt)
#	print(message)


# This code block checks before displaying the message and only prints if it doesn't match the quit value:
#
# while message != 'quit':
# 	message = input(prompt)
#	
# 	if message != 'quit':
# 		print(message)


# This code block adds a flag to determine if the conditions match for it to be active:
#
# active = True
# while active:
# 	message = input(prompt)
#
# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)


# This code block adds a break statement to exit immediately without running additional code,
# regardless of the results of any conditional test.
while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print(f"OK, we'll add {topping} to your pizza!")