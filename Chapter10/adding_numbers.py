print("Give me two numbers to add. ")
first_number = input("First number: ")
second_number = input("Second number: ")

try:
	sum_numbers = int(first_number) + int(second_number)
	print(f"The sum of the two numbers is {sum_numbers}.")
except ValueError:
	print(f"You can't add a number and a word!")