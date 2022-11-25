# WEATHER API 
#*
# 
# *#

import requests
from requests.auth import HTTPBasicAuth

request = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
weather=request.json()
#print(weather)

longitude = weather['longitude']
#print(longitude)
latitude = weather['latitude']
timezone = weather['timezone']
hourlyUnits = (weather['hourly_units'])
print(hourlyUnits)