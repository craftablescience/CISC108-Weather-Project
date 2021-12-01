from cisc108 import assert_equal
from openweathermap import *

def kelvin_to_celcius(degrees: float)->float:
    return degrees-273

def celcius_to_farenheit(degrees: float)->float:
    return (degrees*1.8)+32

assert_equal(celcius_to_farenheit(32.0), 89.6)
assert_equal(celcius_to_farenheit(-32.0), -25.6)
assert_equal(kelvin_to_celcius(500), 227)
