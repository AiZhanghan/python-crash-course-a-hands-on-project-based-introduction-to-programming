import unittest

from city_functions import get_formated_city_name


class CityTestCase(unittest.TestCase):
    '''测试city_functions.py'''
    def test_city_country(self):
        '''能够正确地处理像Santiago, Chile这样的城市吗？'''
        formetted_city_name = get_formated_city_name('santiago', 'chile')
        self.assertEqual(formetted_city_name, 'Santiago, Chile')

    def test_city_country_population(self):
        '''
        能够正确地处理像Santiago, Chile - population 5000000这样的城市吗？
        '''
        formatted_city_name = get_formated_city_name('santiago',
            'chile', 5000000)
        self.assertEqual(formatted_city_name, 
            'Santiago, Chile - population 5000000')
            

unittest.main()
