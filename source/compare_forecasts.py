import argparse
import open_weather_map_api as weather


def main():
    parser = argparse.ArgumentParser(description="Compare weather forecasts between two cities.")
    parser.add_argument("city1", type=str, help="The first city.")
    parser.add_argument("city2", type=str, help="The second city.")
    args = parser.parse_args()
    compare_forecasts(args.city1, args.city2)


def compare_forecasts(city1, city2, period='day', total_days=5):
    # Validation
    valid_periods = ['day', 'eve', 'max', 'min', 'morn', 'night']
    if period not in valid_periods:
        raise ValueError('Period is not one of the acceptable values')
    if total_days <= 0:
        raise ValueError('total_days must be a positive integer')
    print("Weather forecast comparison between {} and {}:".format(city1, city2))
    city1_weather = weather.get_weather_by_city(city1, total_days)
    city2_weather = weather.get_weather_by_city(city2, total_days)
    report = create_report(city1_weather, city2_weather, period=period, total_days=total_days)
    for line in report:
        print line


def create_report(city1_weather, city2_weather, period, total_days):
    output = []
    city1_name = city1_weather["city"]["name"]
    city2_name = city2_weather["city"]["name"]
    for day in range(total_days):
        city1_temp = city1_weather["list"][day]["temp"][period]
        city2_temp = city2_weather["list"][day]["temp"][period]
        city1_desc = city1_weather["list"][day]["weather"][0]["description"]
        city2_desc = city2_weather["list"][day]["weather"][0]["description"]
        output.append("Day " + str(day + 1) + ":")
        output.append(generate_temp_output(city1_name, city1_temp, city2_name, city2_temp))
        output.append(generate_description_output(city1_name, city1_desc, city2_name, city2_desc))
    return output


def generate_temp_output(city1_name, city1_temp, city2_name, city2_temp):
    temp_difference = abs(city1_temp - city2_temp)
    if city1_temp == city2_temp:
        output = city1_name + " and " + city2_name + \
              " will both have the same temperature (" + str(city1_temp) + "C)."
    elif city1_temp > city2_temp:
        output = city1_name + " (" + str(city1_temp) + "C) will be " + \
              str(temp_difference) + "C warmer than " + city2_name + " (" + str(city2_temp) + "C)."
    elif city1_temp < city2_temp:
        output = city1_name + " (" + str(city1_temp) + "C) will be " + \
              str(temp_difference) + "C cooler than " + city2_name + " (" + str(city2_temp) + "C)."
    return output


def generate_description_output(city1_name, city1_desc, city2_name, city2_desc):
    # Modify 'sky is clear' description to make output more readable
    if city1_desc == 'sky is clear':
        city1_desc = 'clear sky'
    if city2_desc == 'sky is clear':
        city2_desc = 'clear sky'

    # Generate output
    if city1_desc == city2_desc:
        output = city1_name + " and " + city2_name + \
              " will both have " + city1_desc + "."
    else:
        output = city1_name + " will have " + city1_desc + ", but " + \
              city2_name + " will have " + city2_desc + "."
    return output


if __name__ == "__main__":
    main()
