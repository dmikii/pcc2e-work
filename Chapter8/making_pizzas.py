import pizza

pizza.make_pizza(16, 'pepperoni') #syntax = module_name.function_name()
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# This syntax will import a specific function from a module:
# from module_name import function_name

from pizza import make_pizza

# Since the function was explicity imported, it can be called by name as usual.
make_pizza(13, 'twizzlers')

# This will import the function with an alias:

from pizza import make_pizza as mp

mp(40, 'brussel sprouts')

# Can also be done with modules:

import pizza as p

p.make_pizza(4, 'nanites')

# This syntax will import all functions in a module:
# Not recommended, best to import the desired function(s), or import the entire module.
from pizza import *

make_pizza(7, 'sausage')