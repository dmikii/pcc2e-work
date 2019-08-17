import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
	"""Test for 'city_functions.py'."""

	def test_city_country(self):
		"""Do names like 'Santiago, Chile' work?"""
		city_name = get_formatted_city('santiago', 'chile')
		self.assertEqual(city_name, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Do names like 'Santiago, Chile - population 5000000' work?"""
		city_name = get_formatted_city('santiago', 'chile', '5000000')
		self.assertEqual(city_name, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
	unittest.main()
