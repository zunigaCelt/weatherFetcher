import requests
import json

def locationData(zipcode) :
    api_key = "d162193b8277fb5e968036cafad58144"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "zip=" + zipcode + ",us&appid=" + api_key

    response = requests.get(complete_url)

    locationData = response.json()

    return locationData
