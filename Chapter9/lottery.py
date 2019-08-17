from random import choice

lottery_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', 'A', 'B', 'C', 'D', 'E']
drawn_numbers = []

current_value = 1
while current_value <= 4:
	number = choice(lottery_numbers)
	drawn_numbers.append(number)
	current_value += 1

print(f"Your numbers are {', '.join(drawn_numbers)}.") # see syntax for join method


