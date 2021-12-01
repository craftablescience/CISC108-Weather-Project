import requests
from pprint import pprint
import json

key = ""
try:
    with open("secrets.json") as file:
        key = json.load(file)["apiKey"]
except FileNotFoundError:
    print("""Please create a secrets.json file with the following format:

{
    "apiKey": "your-api-key-here"
}
""")
    exit(1)

base_url = "https://api.openweathermap.org/data/2.5/weather"
city_id = input("Enter a city: ")
weather_data = requests.get(base_url + "?q=" + city_id + "&appid=" + key).json()
pprint(weather_data)

def kelvin_to_celcius(degrees: int)->int:
    return degrees-273

def celcius_to_farenheit(degrees: int)->int:
    return (degrees*1.8)+32