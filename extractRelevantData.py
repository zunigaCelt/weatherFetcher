import fetchLocationData as fetch
import pytemperature as temp

def relevantData () :

    locationData = fetch.locationData()

    weatherData = {}

    weatherData["cityName"] = locationData["name"]
    weatherData["windSpeed"] = locationData["wind"]["speed"]
    weatherData["currentTemp"] = temp.k2f(locationData["main"]["temp"])
    weatherData["maxTemp"] = temp.k2f(locationData["main"]["temp_max"])
    weatherData["minTemp"] = temp.k2f(locationData["main"]["temp_min"])

    print(weatherData)

    return weatherData

relevantData()