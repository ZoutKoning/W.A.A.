import requests
import json

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
        try:
            result = filterResponse(response)
        except:
            result = "Exception: filtering and retrieving cretain values from the GET response "
    except:
        result = "Error: requesting GET api."
    
    return result 

def filterResponse(response):
    resp_json = response.json()
    key = "success"
    if key in resp_json:
        bl_success = resp_json["success"]
        if (bl_success == True):
            #filter out response below meaning get rid unnecessary details. 
            res = {
                #Current Weather Description (Sunny/Rainy/ETC)
                "current weather": resp_json["response"]["ob"]["weather"],
                #Current Temperature 
                "current Temp (F)": resp_json["response"]["ob"]["tempF"],
                "current Temp (C)": resp_json["response"]["ob"]["tempC"]
            }
        else:
            res = resp_json["error"]["description"]
    else:
        res = resp_json["message"]
    return res