import requests
import json

location = 29670
url = "https://aerisweather1.p.rapidapi.com/observations/" + str(location)

headers = {
    "X-RapidAPI-Key": "f125d5bbc2msh34f2dee4a686e61p1cd73bjsnfadff23586d3",
    "X-RapidAPI-Host": "aerisweather1.p.rapidapi.com"
}
try: 
    response = requests.request("GET", url, headers=headers)
    result = response.json()
except:
    result = "Error: requesting GET api."
    
    
json_object = json.dumps(result, indent=4)
wf = open("Current.json", "w")
wf.write(json_object)
