# compare-weather-forecast

# Setup Instructions
1. Run `pip install requests`

# Run Instructions

### Run Tests
On project root, run one of the following tests

`Compare Forecast Tests`
```
python -m unittest -v tests.test_compare_forecasts
```

`Open Weather Map API Tests`
```
python -m unittest -v tests.test_open_weather_map_api
```

### Run compare_forecasts program
1. Navigate to `/source` folder
2. `python compare_forecasts.py [city1] [city2]`

# Additional compare_forecasts information

This script takes in two city names as input and outputs the differences in
weather between the cities over the next 5 days.

Usage example:
```
python compare_forecasts.py Toronto Cleveland
```
Output example:
```
 Weather forecast comparison between Toronto and Cleveland:

 Day 1:
 Toronto (18C) will be 3C cooler than Cleveland (21C).
 Toronto will have clear sky, but Cleveland will have rain.

 Day 2:
 Toronto (21C) will be 3C warmer than Cleveland (18C).
 Toronto will have scattered clouds, but Cleveland will have light rain.

 Day 3:
 Toronto and Cleveland will both have the same temperature (20C).
 Toronto and Cleveland will both have light rain.

 Day 4:
 Toronto (18C) will be 3C cooler than Cleveland (21C).
 Toronto and Cleveland will both have light rain.

 Day 5:
 Toronto and Cleveland will both have the same temperature (17C).
 Toronto will have scattered clouds, but Cleveland will have light rain.
```