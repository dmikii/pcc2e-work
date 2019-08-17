guest_list = ['William Shakespeare', 'David Bowie', 'Stephen Hawking']

message1 = f"Please join me for dinner, {guest_list[0]}."
message2 = f"Hey, {guest_list[1]}, it would be cool if you could join me for dinner."
message3 = f"Dear {guest_list[2]}, please join me for dinner."
print(message1)
print(message2)
print(message3)

print(f"\nAh, {guest_list[1]} can't make it.")

guest_list[1] = 'Prince'

message4 = f"\nPlease join me for dinner, {guest_list[0]}."
message5 = f"Hey, {guest_list[1]}, it would be cool if you could join me for dinner."
message6 = f"Dear {guest_list[2]}, please join me for dinner."
print(message4)
print(message5)
print(message6)

print(f"\nHey {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}, looks like we found a bigger table, so I'm inviting more people!")

guest_list.insert(0, 'Madeline Miller')
guest_list.insert(2, 'Jenny Lewis')
guest_list.append('Grace Hopper')

message7 = f"\nFormal dinner invite for {guest_list[0]}!"
message8 = f"Formal dinner invite for {guest_list[1]}!"
message9 = f"Formal dinner invite for {guest_list[2]}!"
message10 = f"Formal dinner invite for {guest_list[3]}!"
message11 = f"Formal dinner invite for {guest_list[4]}!"
message12 = f"Formal dinner invite for {guest_list[5]}!"

print(message7)
print(message8)
print(message9)
print(message10)
print(message11)
print(message12)

print(f"I am inviting {len(guest_list)} guests to dinner.")

# print("\nWhoops, looks like we're not going to get the big table after all, just room for 2 people now :(")

# popped_guest = guest_list.pop()
# print(f"\nSorry {popped_guest}, I can't invite you after all!")

# popped_guest = guest_list.pop()
# print(f"\nSorry {popped_guest}, I can't invite you after all!")

# popped_guest = guest_list.pop()
# print(f"\nSorry {popped_guest}, I can't invite you after all!")

# popped_guest = guest_list.pop()
# print(f"\nSorry {popped_guest}, I can't invite you after all!")

# print(f"\nDon't worry, you're still invited {guest_list[0]}!")
# print(f"\nDon't worry, you're still invited {guest_list[1]}!")

# del guest_list[-1]
# del guest_list[-1]
# print(guest_list)

