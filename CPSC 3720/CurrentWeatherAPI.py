import requests

#

def getWeatherAPI(location_info):
    # location could use "zipcode", "latitude,longitude", "city,state" or "city,country"
    location = location_info
    url = "https://aerisweather1.p.rapidapi.com/observations/" + str(location)

    headers = {
        "X-RapidAPI-Key": "f125d5bbc2msh34f2dee4a686e61p1cd73bjsnfadff23586d3",
        "X-RapidAPI-Host": "aerisweather1.p.rapidapi.com"
    }
    try: 
        response = requests.request("GET", url, headers=headers)
        result = filterResponse(response)
    except:
        result = "Error: requesting GET api."
    
    return result 
    
def filterResponse(response):
    resp_json = response.json()
    bl_success = resp_json["success"]
    res = []
    if (bl_success == True):
        #filter out response below meaning get rid unnecessary details. 
        res = {
            "weather": resp_json["weather"] 
        }
    else:
        res = resp_json
    
    return res