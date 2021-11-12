# -- coding: utf-8 --

import unittest
from city_functions import get_city_country

class cityTestCase(unittest.TestCase):
    def test_city_country(self):
        get_cities_str = get_city_country('santiago','chile','5000000')
        self.assertEqual(get_cities_str,'santiago, chile - population 5000000')

unittest.main