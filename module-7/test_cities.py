#Cindy Hernandez
#mod 7.2
#12/1/24



import unittest
from city_functions import format_city_country

class TestCityCountryFunction(unittest.TestCase):
    """Test the format_city_country function."""

    def test_city_country(self):
        """Test if the function returns the correct city, country string."""
        result = format_city_country('Santiago', 'Chile')
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
