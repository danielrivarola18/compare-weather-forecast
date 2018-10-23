import requests
import urlparse

base_url = "http://api.openweathermap.org/data/2.5/forecast/daily?"
api_key = "fe9c5cddb7e01d747b4611c3fc9eaf2c"


def get_weather_by_city(city, cnt=5):
    if cnt <= 0:
        raise ValueError('Cnt must be a positive integer')
    # Return 5 day forecast
    path = "?q=" + city + "&mode=json&units=metric&cnt=" + str(cnt) + "&APPID=" + api_key
    url = urlparse.urljoin(base_url, path)
    response = requests.get(url=url)
    weather_data = response.json()
    return weather_data

