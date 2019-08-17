def make_sandwich(*ingredients):
	print("\nHere's the items in your sandwich:")
	for ingredient in ingredients:
		print(f"- {ingredient}")

make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('grilled cheese')
make_sandwich('chicken', 'mozzarella')