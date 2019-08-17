age = input("\nEnter your age: ")
age = int(age)

if age < 3:
	print("Your ticket is free!")
elif age >= 3 and age <= 12:
	print("Your ticket will be $10.")
else:
	print("Your ticket will be $15.")