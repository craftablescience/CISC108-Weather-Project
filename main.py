from cisc108 import assert_equal
from openweathermap import *

print(make_request(q="Pittsburgh"))

def kelvin_to_celcius(degrees: float)->float:
    return degrees-273

def celcius_to_farenheit(degrees: float)->float:
    return (degrees*1.8)+32

assert_equal(celcius_to_farenheit(32.0), 89.6)
assert_equal(celcius_to_farenheit(-32.0), -25.6)
assert_equal(kelvin_to_celcius(500), 227)



def if_snowing(weather_set: dict)-> bool:
    return "snow" in weather_set

assert_equal(if_snowing({'coord': {'lon': 140.2167, 'lat': 39.65}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'base': 'stations', 'main': {'temp': 274.67, 'feels_like': 267.86, 'temp_min': 274.67, 'temp_max': 274.67, 'pressure': 1008, 'humidity': 74, 'sea_level': 1008, 'grnd_level': 1005}, 'visibility': 2667, 'wind': {'speed': 10.92, 'deg': 285, 'gust': 17.16}, 'snow': {'1h': 0.22}, 'clouds': {'all': 100}, 'dt': 1638388040, 'sys': {'country': 'JP', 'sunrise': 1638394899, 'sunset': 1638429336}, 'timezone': 32400, 'id': 2110608, 'name': 'Wada', 'cod': 200}
), True)
assert_equal(if_snowing({'coord': {'lon': -79.9959, 'lat': 40.4406}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 284.68, 'feels_like': 284.29, 'temp_min': 282.68, 'temp_max': 286.42, 'pressure': 1005, 'humidity': 92}, 'visibility': 8047, 'wind': {'speed': 0.89, 'deg': 233, 'gust': 7.6}, 'rain': {'1h': 1.62}, 'clouds': {'all': 90}, 'dt': 1638812611, 'sys': {'type': 2, 'id': 2008550, 'country': 'US', 'sunrise': 1638793749, 'sunset': 1638827610}, 'timezone': -18000, 'id': 5206379, 'name': 'Pittsburgh', 'cod': 200}
), False)
assert_equal(if_snowing({'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 282.23, 'feels_like': 282.23, 'temp_min': 280.43, 'temp_max': 283.89, 'pressure': 1020, 'humidity': 47}, 'visibility': 10000, 'wind': {'speed': 0.89, 'deg': 179, 'gust': 2.68}, 'clouds': {'all': 1}, 'dt': 1638388045, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638360113, 'sunset': 1638394211}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
), False)

def if_raining(weather_set: dict)-> bool:
    return "rain" in weather_set

assert_equal(if_raining({'coord': {'lon': 140.2167, 'lat': 39.65}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'base': 'stations', 'main': {'temp': 274.67, 'feels_like': 267.86, 'temp_min': 274.67, 'temp_max': 274.67, 'pressure': 1008, 'humidity': 74, 'sea_level': 1008, 'grnd_level': 1005}, 'visibility': 2667, 'wind': {'speed': 10.92, 'deg': 285, 'gust': 17.16}, 'snow': {'1h': 0.22}, 'clouds': {'all': 100}, 'dt': 1638388040, 'sys': {'country': 'JP', 'sunrise': 1638394899, 'sunset': 1638429336}, 'timezone': 32400, 'id': 2110608, 'name': 'Wada', 'cod': 200}
), False)
assert_equal(if_raining({'coord': {'lon': -79.9959, 'lat': 40.4406}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 284.68, 'feels_like': 284.29, 'temp_min': 282.68, 'temp_max': 286.42, 'pressure': 1005, 'humidity': 92}, 'visibility': 8047, 'wind': {'speed': 0.89, 'deg': 233, 'gust': 7.6}, 'rain': {'1h': 1.62}, 'clouds': {'all': 90}, 'dt': 1638812611, 'sys': {'type': 2, 'id': 2008550, 'country': 'US', 'sunrise': 1638793749, 'sunset': 1638827610}, 'timezone': -18000, 'id': 5206379, 'name': 'Pittsburgh', 'cod': 200}
), True)
assert_equal(if_raining({'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 282.23, 'feels_like': 282.23, 'temp_min': 280.43, 'temp_max': 283.89, 'pressure': 1020, 'humidity': 47}, 'visibility': 10000, 'wind': {'speed': 0.89, 'deg': 179, 'gust': 2.68}, 'clouds': {'all': 1}, 'dt': 1638388045, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638360113, 'sunset': 1638394211}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
), False)