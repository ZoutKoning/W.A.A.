import requests

def forecastWeatherAPI(location_info):
    # location could use "zipcode", "latitude,longitude", "city,state" or "city,country"
    location = location_info
    url = "https://aerisweather1.p.rapidapi.com/forecasts/" + str(location)

    headers = {
        "X-RapidAPI-Key": "f125d5bbc2msh34f2dee4a686e61p1cd73bjsnfadff23586d3",
        "X-RapidAPI-Host": "aerisweather1.p.rapidapi.com"
    }
    # receives api response and sends it to be filtered
    #catches common errors 
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
            fullForecast = []
            # filters min/max temps, feels like temp and the weather description
            for i in range (len(resp_json['response'][0]['periods'])):
                #pulls string time from  json
                strdatetime = resp_json['response'][0]['periods'][i]['dateTimeISO']
                #splits the new information at the T
                strdate = strdatetime.split("T")
                #the following lines 37-44 pull the desired information from the json dictionary and sore them in their respective variables
                #they are stored in a listed dictionary, hence the nested [] to find the desired info 
                res = {
                    'time': strdate[0],
                    "minC": resp_json['response'][0]['periods'][i]['minTempC'],
                    "maxC": resp_json['response'][0]['periods'][i]['maxTempC'],
                    "minF": resp_json['response'][0]['periods'][i]['minTempF'],
                    "maxF": resp_json['response'][0]['periods'][i]['maxTempF'],
                    "feelslikeC": resp_json['response'][0]['periods'][i]['feelslikeC'],
                    "feelslikeF": resp_json['response'][0]['periods'][i]['feelslikeF'],
                    'weather': resp_json['response'][0]['periods'][i]['weatherPrimary'],
                    
                }
                fullForecast.append(res)
        else:
            fullForecast = resp_json["error"]["description"]
    else:
        fullForecast = resp_json["message"]
    return fullForecast
