from cisc108 import assert_equal
from openweathermap import *

print(make_request(q="Charleston"))

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
assert_equal(if_snowing({'coord': {'lon': 108.2208, 'lat': 16.0678}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 293.14, 'feels_like': 293.49, 'temp_min': 292.18, 'temp_max': 293.14, 'pressure': 1017, 'humidity': 88}, 'visibility': 8000, 'wind': {'speed': 0, 'deg': 0}, 'clouds': {'all': 75}, 'dt': 1638388254, 'sys': {'type': 1, 'id': 9306, 'country': 'VN', 'sunrise': 1638399573, 'sunset': 1638440025}, 'timezone': 25200, 'id': 1583992, 'name': 'Turan', 'cod': 200}
), False)
assert_equal(if_snowing({'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 282.23, 'feels_like': 282.23, 'temp_min': 280.43, 'temp_max': 283.89, 'pressure': 1020, 'humidity': 47}, 'visibility': 10000, 'wind': {'speed': 0.89, 'deg': 179, 'gust': 2.68}, 'clouds': {'all': 1}, 'dt': 1638388045, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638360113, 'sunset': 1638394211}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
), False)

def if_raining(weather_set: dict)-> bool:
    return "rain" in weather_set

assert_equal(if_raining({'coord': {'lon': 140.2167, 'lat': 39.65}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'base': 'stations', 'main': {'temp': 274.67, 'feels_like': 267.86, 'temp_min': 274.67, 'temp_max': 274.67, 'pressure': 1008, 'humidity': 74, 'sea_level': 1008, 'grnd_level': 1005}, 'visibility': 2667, 'wind': {'speed': 10.92, 'deg': 285, 'gust': 17.16}, 'snow': {'1h': 0.22}, 'clouds': {'all': 100}, 'dt': 1638388040, 'sys': {'country': 'JP', 'sunrise': 1638394899, 'sunset': 1638429336}, 'timezone': 32400, 'id': 2110608, 'name': 'Wada', 'cod': 200}
), False)
assert_equal(if_raining({'coord': {'lon': 108.2208, 'lat': 16.0678}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 293.14, 'feels_like': 293.49, 'temp_min': 292.18, 'temp_max': 293.14, 'pressure': 1017, 'humidity': 88}, 'visibility': 8000, 'wind': {'speed': 0, 'deg': 0}, 'clouds': {'all': 75}, 'dt': 1638388254, 'sys': {'type': 1, 'id': 9306, 'country': 'VN', 'sunrise': 1638399573, 'sunset': 1638440025}, 'timezone': 25200, 'id': 1583992, 'name': 'Turan', 'cod': 200}
), True)
assert_equal(if_raining({'coord': {'lon': -74.1724, 'lat': 40.7357}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 282.23, 'feels_like': 282.23, 'temp_min': 280.43, 'temp_max': 283.89, 'pressure': 1020, 'humidity': 47}, 'visibility': 10000, 'wind': {'speed': 0.89, 'deg': 179, 'gust': 2.68}, 'clouds': {'all': 1}, 'dt': 1638388045, 'sys': {'type': 2, 'id': 2003689, 'country': 'US', 'sunrise': 1638360113, 'sunset': 1638394211}, 'timezone': -18000, 'id': 5101798, 'name': 'Newark', 'cod': 200}
), False)

assert_equal(if_raining({'coord': {'lon': -123.1193, 'lat': 49.2497}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 284.73, 'feels_like': 284.35, 'temp_min': 283.69, 'temp_max': 287.03, 'pressure': 1017, 'humidity': 92}, 'visibility': 10000, 'wind': {'speed': 1.79, 'deg': 119, 'gust': 5.81}, 'clouds': {'all': 90}, 'dt': 1638388087, 'sys': {'type': 2, 'id': 2011597, 'country': 'CA', 'sunrise': 1638373612, 'sunset': 1638404213}, 'timezone': -28800, 'id': 6173331, 'name': 'Vancouver', 'cod': 200}
), True)
