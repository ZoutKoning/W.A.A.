# ARIES WEATHER API (NEW)
import requests

def getWeatherAPI(location_info):
    # location could use zipcode, [latitude,longitude], [city,state], [city,country]
    location = location_info
    url = "https://aerisweather1.p.rapidapi.com/observations/" + str(location)

    headers = {
        "X-RapidAPI-Key": "f125d5bbc2msh34f2dee4a686e61p1cd73bjsnfadff23586d3",
        "X-RapidAPI-Host": "aerisweather1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)