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

### Run Main
1. Navigate to `/source` folder
2. `python compare_forecasts.py [city1] [city2]`