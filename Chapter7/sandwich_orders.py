sandwich_orders = ['blt', 'pastrami', 'club', 'pastrami', 'grilled cheese']
finished_sandwiches = []

print("Sorry, but we're all out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"\n I made your {current_sandwich.title()} sandwich.")

	finished_sandwiches.append(current_sandwich)

print("\nHere's all the sandwiches you ordered:")
for sandwich in finished_sandwiches:
	print(sandwich.title())