from car import Car, ElectricCar 	# Import multiple classes from a module by
									# separating them with a comma.

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

import car # Imports an entire module.

my_beetle = car.Car('volkswagen', 'beetle', 2019) # using module_name.ClassName syntax
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# To import every class from a module:
#	from module_name import *

# Not recommended:
# 1. Unclear which classes are being used from the module.
# 2. Leads to confusion with names in the file.

# Better to use module_name.ClassName syntax from above.

# Can also use aliases:
# from electric_car import ElectricCar as EC
# my_tesla = EC('tesla', 'roadster', 2019)