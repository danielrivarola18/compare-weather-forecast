import unittest
from source import compare_forecasts


class TestCompareForecastsMethods(unittest.TestCase):

    def test_generate_description_output(self):
        city1 = 'Toronto'
        city2 = 'Cleveland'
        # Verify output for the same description
        result = compare_forecasts.generate_description_output(city1, 'light rain', city2, 'light rain')
        expected = city1 + ' and ' + city2 + ' will both have light rain.'
        self.assertEqual(result, expected)

        # Verify output for different descriptions
        result = compare_forecasts.generate_description_output(city1, 'few clouds', city2, 'light rain')
        expected = city1 + ' will have few clouds, but ' + city2 + ' will have light rain.'
        self.assertEqual(result, expected)

        # Verify description is replaced from 'sky is clear' to 'clear sky'
        result = compare_forecasts.generate_description_output(city1, 'sky is clear', city2, 'sky is clear')
        expected = city1 + ' and ' + city2 + ' will both have clear sky.'
        self.assertEqual(result, expected)

    def test_generate_temp_output(self):
        city1 = 'Toronto'
        city2 = 'Cleveland'
        # Verify output for the same temperature
        result = compare_forecasts.generate_temp_output(city1, 20, city2, 20)
        expected = city1 + ' and ' + city2 + ' will both have the same temperature (20C).'
        self.assertEqual(result, expected)

        # Verify output for when City1 has a lower temperature than City2
        result = compare_forecasts.generate_temp_output(city1, 18, city2, 21)
        expected = city1 + ' (18C) will be 3C cooler than ' + city2 + ' (21C).'
        self.assertEqual(result, expected)

        # Verify output for when City1 has a higher temperature than City2
        result = compare_forecasts.generate_temp_output(city1, 21, city2, 18)
        expected = city1 + ' (21C) will be 3C warmer than ' + city2 + ' (18C).'
        self.assertEqual(result, expected)

    def test_create_report(self):
        period = "night"
        days = 2
        city1_weather = {u'city': {u'name': u'Toronto'}, u'list': []}
        city1_weather[u'list'].append({u'temp': {period: 18}, u'weather': [{u'description': u'clear sky'}]})
        city1_weather[u'list'].append({u'temp': {period: 21}, u'weather': [{u'description': u'scattered clouds'}]})
        city2_weather = {u'city': {u'name': u'Salzburg'}, u'list': []}
        city2_weather[u'list'].append({u'temp': {period: 21}, u'weather': [{u'description': u'rain'}]})
        city2_weather[u'list'].append({u'temp': {period: 18}, u'weather': [{u'description': u'light rain'}]})
        expected = [
            'Day 1:',
            'Toronto (18C) will be 3C cooler than Salzburg (21C).',
            'Toronto will have clear sky, but Salzburg will have rain.',
            'Day 2:',
            'Toronto (21C) will be 3C warmer than Salzburg (18C).',
            'Toronto will have scattered clouds, but Salzburg will have light rain.'
        ]
        result = compare_forecasts.create_report(city1_weather, city2_weather, period, days)
        self.assertListEqual(result, expected)

    def test_compare_forecasts(self):
        city1 = 'Toronto'
        city2 = 'Cleveland'
        # Verify error appears for invalid period
        with self.assertRaises(ValueError):
            compare_forecasts.compare_forecasts(city1, city2, period='fake')
        # Verify error appears for missing input
        with self.assertRaises(TypeError):
            compare_forecasts.compare_forecasts(city1)
        with self.assertRaises(TypeError):
            compare_forecasts.compare_forecasts()
        # Verify error appears for invalid total_days
        with self.assertRaises(ValueError):
            compare_forecasts.compare_forecasts(city1, city2, total_days=0)
        with self.assertRaises(ValueError):
            compare_forecasts.compare_forecasts(city1, city2, total_days=-1)


if __name__ == '__main__':
    unittest.main()
