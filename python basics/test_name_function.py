# -- coding: utf-8 --

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''
    test name_function.py
    '''

    def test_first_last_name(self):
        '''
        if correctly handle the name like "Janis Joplin"
        '''
        formatted_name = get_formatted_name('Janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main