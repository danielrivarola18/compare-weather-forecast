import unittest
from source import open_weather_map_api


class TestOpenWeatherMapApiMethods(unittest.TestCase):

    def test_invalid_inputs(self):
        city = 'Toronto'
        # Verify error when day is less than or equal to 0
        with self.assertRaises(ValueError):
            open_weather_map_api.get_weather_by_city(city, -1)
        with self.assertRaises(ValueError):
            open_weather_map_api.get_weather_by_city(city, 0)
        # Verify error when querying for a city that does not exist
        result = open_weather_map_api.get_weather_by_city('fake')
        self.assertEqual(result["message"], 'city not found')
        self.assertEqual(result["cod"], '404')

    def test_missing_inputs(self):
        with self.assertRaises(TypeError):
            open_weather_map_api.get_weather_by_city()

    def test_default_values(self):
        # Verify optional days input is set to 5 by default
        city = 'Toronto'
        default_days = 5
        result = open_weather_map_api.get_weather_by_city(city)
        result_list = result["list"]
        self.assertEqual(default_days, len(result_list))

    def test_input_city_matches_response(self):
        city = 'Toronto'
        result = open_weather_map_api.get_weather_by_city(city)
        result_city = result["city"]["name"]
        self.assertEqual(city, result_city)

    def test_count_matches_expected_days(self):
        city = 'Toronto'
        days = 3
        result = open_weather_map_api.get_weather_by_city(city, days)
        result_list = result["list"]
        self.assertEqual(days, len(result_list))


if __name__ == '__main__':
    unittest.main()
