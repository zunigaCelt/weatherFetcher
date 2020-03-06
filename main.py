import requests
import json

api_key = "d162193b8277fb5e968036cafad58144"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

zip_code = str(input("Enter your zip code: "))

complete_url = base_url + "zip=" + zip_code + ",us&appid=" + api_key

response = requests.get(complete_url)

x = response.json()
