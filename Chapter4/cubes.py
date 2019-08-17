cubes = []
for value in range(1, 11):
	cubes.append(value**3)

print(cubes)

# list comprehension

cubes = [value**3 for value in range(1, 11)]
print(cubes)

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[4:7])

print("The last three items in the list are:")
print(cubes[7:])
print(cubes[-3:])