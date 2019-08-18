from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D8 dice.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
# results = []
# for roll_num in range(500000):
# 	result = die_1.roll() + die_2.roll()
# 	results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

# Analyze the results.
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
#	frequency = results.count(value)
#	frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2, max_result+1)]

#Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1} # Each config option is stored as an entry in a dictionary.
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 50000 times',
		xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html') # Dictionary for data and layout objects.

