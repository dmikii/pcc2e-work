print("Give me two numbers to add.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		sum_numbers = int(first_number) + int(second_number)
	except ValueError:
		print(f"You can't add a number and a word!")
	else:
		print(f"The sum of the two numbers is {sum_numbers}.")