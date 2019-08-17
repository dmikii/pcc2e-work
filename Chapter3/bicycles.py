bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

# Experimenting with f-string, index position, and formatting string method
#
# f-string usage:
#	1. f immediately before opening quotation mark
#	2. Braces - {} - around name/names of any variable to use inside the string

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)