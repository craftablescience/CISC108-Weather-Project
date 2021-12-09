from cisc108 import assert_equal
from openweathermap import *

print(make_request(q="Boise"))

def kelvin_to_celsius(degrees: float)->float:
    '''
    Converts degrees kelvin to degrees celsius

    :param degrees:
    Degrees in kelvin
    :return: float
    Degrees in celsius
    '''
    return degrees-273

def celsius_to_fahrenheit(degrees: float)->float:
    '''
    Converts degrees celsius to degrees fahrenheit

    :param degrees:
    Degrees in celsius
    :return: float
    Degrees in fahrenheit
    '''
    return (degrees*1.8)+32

assert_equal(celsius_to_fahrenheit(32.0), 89.6)
assert_equal(celsius_to_fahrenheit(-32.0), -25.6)
assert_equal(kelvin_to_celsius(500), 227)



def if_snowing(weather_set: dict)-> bool:
    '''
    Takes in a dictionary from the website and from there searches through the keys to determine if snowing is True or False

    :param weather_set:
    The set of data from the web API
    :return: bool
    Whether it is snowing or not
    '''
    return "snow" in weather_set

assert_equal(if_snowing({'coord': {'lon': 140.2167, 'lat': 39.65}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'base': 'stations', 'main': {'temp': 274.67, 'feels_like': 267.86, 'temp_min': 274.67, 'temp_max': 274.67, 'pressure': 1008, 'humidity': 74, 'sea_level': 1008, 'grnd_level': 1005}, 'visibility': 2667, 'wind': {'speed': 10.92, 'deg': 285, 'gust': 17.16}, 'snow': {'1h': 0.22}, 'clouds': {'all': 100}, 'dt': 1638388040, 'sys': {'country': 'JP', 'sunrise': 1638394899, 'sunset': 1638429336}, 'timezone': 32400, 'id': 2110608, 'name': 'Wada', 'cod': 200}
), True)
assert_equal(if_snowing({'coord': {'lon': -79.9959, 'lat': 40.4406}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 284.68, 'feels_like': 284.29, 'temp_min': 282.68, 'temp_max': 286.42, 'pressure': 1005, 'humidity': 92}, 'visibility': 8047, 'wind': {'speed': 0.89, 'deg': 233, 'gust': 7.6}, 'rain': {'1h': 1.62}, 'clouds': {'all': 90}, 'dt': 1638812611, 'sys': {'type': 2, 'id': 2008550, 'country': 'US', 'sunrise': 1638793749, 'sunset': 1638827610}, 'timezone': -18000, 'id': 5206379, 'name': 'Pittsburgh', 'cod': 200}
), False)
assert_equal(if_snowing({'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 282.23, 'feels_like': 282.23, 'temp_min': 280.43, 'temp_max': 283.89, 'pressure': 1020, 'humidity': 47}, 'visibility': 10000, 'wind': {'speed': 0.89, 'deg': 179, 'gust': 2.68}, 'clouds': {'all': 1}, 'dt': 1638388045, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638360113, 'sunset': 1638394211}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
), False)

def if_raining(weather_set: dict)-> bool:
    '''
    Takes in a dictionary from the website and from there searches through the keys to determine if raining is True or False

    :param weather_set:
    The set of data from the web API
    :return: bool
    Whether it is raining or not
    '''
    return "rain" in weather_set

assert_equal(if_raining({'coord': {'lon': 140.2167, 'lat': 39.65}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'base': 'stations', 'main': {'temp': 274.67, 'feels_like': 267.86, 'temp_min': 274.67, 'temp_max': 274.67, 'pressure': 1008, 'humidity': 74, 'sea_level': 1008, 'grnd_level': 1005}, 'visibility': 2667, 'wind': {'speed': 10.92, 'deg': 285, 'gust': 17.16}, 'snow': {'1h': 0.22}, 'clouds': {'all': 100}, 'dt': 1638388040, 'sys': {'country': 'JP', 'sunrise': 1638394899, 'sunset': 1638429336}, 'timezone': 32400, 'id': 2110608, 'name': 'Wada', 'cod': 200}
), False)
assert_equal(if_raining({'coord': {'lon': -79.9959, 'lat': 40.4406}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 284.68, 'feels_like': 284.29, 'temp_min': 282.68, 'temp_max': 286.42, 'pressure': 1005, 'humidity': 92}, 'visibility': 8047, 'wind': {'speed': 0.89, 'deg': 233, 'gust': 7.6}, 'rain': {'1h': 1.62}, 'clouds': {'all': 90}, 'dt': 1638812611, 'sys': {'type': 2, 'id': 2008550, 'country': 'US', 'sunrise': 1638793749, 'sunset': 1638827610}, 'timezone': -18000, 'id': 5206379, 'name': 'Pittsburgh', 'cod': 200}
), True)
assert_equal(if_raining({'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 282.23, 'feels_like': 282.23, 'temp_min': 280.43, 'temp_max': 283.89, 'pressure': 1020, 'humidity': 47}, 'visibility': 10000, 'wind': {'speed': 0.89, 'deg': 179, 'gust': 2.68}, 'clouds': {'all': 1}, 'dt': 1638388045, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638360113, 'sunset': 1638394211}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
), False)


def clothes_by_temp(degrees: float)-> str:
    '''
    Converts a temperature (in fahrenheit) into a list of clothing that is appropriate for that weather

    :param degrees:
    The given degrees (in fahrenheit)
    :return: str
    Appropriate clothing for the given temperature
    '''
    if degrees < 35:
        cold_weather = ["long sleeve", "pants", "scarf", "gloves", "hat", "boots", "sweatshirt"]
        return cold_weather
    elif 35 < degrees < 55:
        cooler_weather = ["jacket", "sweatshirt", "long sleeve", "pants", "sneakers"]
        return cooler_weather
    elif 55 < degrees < 70:
        warm_weather = ["t-shirt", "pants", "sneakers"]
        return warm_weather
    else:
        hot_weather = ["tank top", "shorts", "dress", "flip flops"]
        return hot_weather

assert_equal(clothes_by_temp(2), ["long sleeve", "pants", "scarf", "gloves", "hat", "boots", "sweatshirt"])
assert_equal(clothes_by_temp(45), ["jacket", "sweatshirt", "long sleeve", "pants", "sneakers"])
assert_equal(clothes_by_temp(60), ["t-shirt", "pants", "sneakers"])
assert_equal(clothes_by_temp(80), ["tank top", "shorts", "dress", "flip flops"])

def find_weather_location(location: str)-> dict:
    '''
    Takes in a given location from the user and produces a weather dictionary using the API

    :param location:
    A location given by the user
    :return: dict
    A dictionary of weather of the given location

    '''
    location_weather = make_request(q=location)
    return location_weather

def feels_like_temperature(weather_set: dict) -> float:
    '''
    This function finds what temperature it feels like in kelvin from a given dictionary of weather features

    :param weather_set:
    The set of data from the web API

    :return: float:
    A float that represents the temperature in Kelvin
    '''
    temp = weather_set["main"]["feels_like"]
    return temp

assert_equal(find_weather_location("Pittsburgh"), {'coord': {'lon': -79.9959, 'lat': 40.4406}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 271.95, 'feels_like': 270.3, 'temp_min': 270.73, 'temp_max': 273.4, 'pressure': 1023, 'humidity': 64}, 'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 236, 'gust': 3.13}, 'clouds': {'all': 1}, 'dt': 1638898231, 'sys': {'type': 2, 'id': 2008550, 'country': 'US', 'sunrise': 1638880203, 'sunset': 1638914006}, 'timezone': -18000, 'id': 5206379, 'name': 'Pittsburgh', 'cod': 200}
)
assert_equal(find_weather_location("Newark"), {'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 278.48, 'feels_like': 275.08, 'temp_min': 276.6, 'temp_max': 280.21, 'pressure': 1021, 'humidity': 45}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 310}, 'clouds': {'all': 75}, 'dt': 1638898345, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638878858, 'sunset': 1638912556}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
)
assert_equal(find_weather_location("Boise"), {'coord': {'lon': -116.2035, 'lat': 43.6135}, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 275.48, 'feels_like': 275.48, 'temp_min': 273.64, 'temp_max': 277.86, 'pressure': 1020, 'humidity': 87}, 'visibility': 3219, 'wind': {'speed': 0.45, 'deg': 295, 'gust': 0.89}, 'clouds': {'all': 90}, 'dt': 1638898070, 'sys': {'type': 2, 'id': 2043419, 'country': 'US', 'sunrise': 1638889500, 'sunset': 1638922094}, 'timezone': -25200, 'id': 5586437, 'name': 'Boise', 'cod': 200}
)
assert_equal(feels_like_temperature({'coord': {'lon': -79.9959, 'lat': 40.4406}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 271.95, 'feels_like': 270.3, 'temp_min': 270.73, 'temp_max': 273.4, 'pressure': 1023, 'humidity': 64}, 'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 236, 'gust': 3.13}, 'clouds': {'all': 1}, 'dt': 1638898231, 'sys': {'type': 2, 'id': 2008550, 'country': 'US', 'sunrise': 1638880203, 'sunset': 1638914006}, 'timezone': -18000, 'id': 5206379, 'name': 'Pittsburgh', 'cod': 200}
), 270.3)
assert_equal(feels_like_temperature({'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 278.48, 'feels_like': 275.08, 'temp_min': 276.6, 'temp_max': 280.21, 'pressure': 1021, 'humidity': 45}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 310}, 'clouds': {'all': 75}, 'dt': 1638898345, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638878858, 'sunset': 1638912556}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
), 275.08)
assert_equal(feels_like_temperature({'coord': {'lon': -116.2035, 'lat': 43.6135}, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 275.48, 'feels_like': 275.48, 'temp_min': 273.64, 'temp_max': 277.86, 'pressure': 1020, 'humidity': 87}, 'visibility': 3219, 'wind': {'speed': 0.45, 'deg': 295, 'gust': 0.89}, 'clouds': {'all': 90}, 'dt': 1638898070, 'sys': {'type': 2, 'id': 2043419, 'country': 'US', 'sunrise': 1638889500, 'sunset': 1638922094}, 'timezone': -25200, 'id': 5586437, 'name': 'Boise', 'cod': 200}
), 275.48)