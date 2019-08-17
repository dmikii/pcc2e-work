prog_bands = ['Yes', 'Genesis', 'Rush', 'ELP']
print(prog_bands)

print(prog_bands[0].title())
print(prog_bands[2])
print(f"My favorite prog band used to be {prog_bands[2]}.")

prog_bands.append('King Crimson')
print(prog_bands)

prog_bands.insert(1, 'Dream Theater')
print(prog_bands)

del prog_bands[1]
print(prog_bands)

popped_band = prog_bands.pop()
print(prog_bands)

print(sorted(prog_bands))

prog_bands.reverse()
print(prog_bands)

length = len(prog_bands)
print(length)

