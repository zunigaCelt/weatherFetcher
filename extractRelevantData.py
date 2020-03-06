import fetchLocationData as fetch
import pytemperature as temp

def extract () :

    locationData = fetch.locationData()

    weatherData = {}

    weatherData["cityName"] = locationData["name"]
    weatherData["windSpeed"] = locationData["wind"]["speed"]
    weatherData["currentTemp"] = temp.k2c(locationData["main"]["temp"])
    weatherData["maxTemp"] = temp.k2c(locationData["main"]["temp_max"])
    weatherData["minTemp"] = temp.k2c(locationData["main"]["temp_min"])

    print(weatherData)