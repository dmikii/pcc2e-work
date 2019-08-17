def make_car(make, model, **car_info):
	"""Build a dictionary containing everything we know about a car."""
	car_info['manufacturer'] = make
	car_info['car_model'] = model
	return car_info

finished_car = make_car('toyota', 'corolla', color='silver', transmission='manual', doors=2)
print(finished_car)
