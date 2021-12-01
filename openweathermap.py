import json
import requests


def api_key() -> str:
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
    return key


def make_request(**kwargs) -> dict:
    url = "https://api.openweathermap.org/data/2.5/weather?appid=" + api_key()
    for arg in kwargs:
        url += "&" + arg + "=" + kwargs[arg]
    return requests.get(url).json()
