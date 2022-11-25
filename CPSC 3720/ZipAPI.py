import requests
from requests.auth import HTTPBasicAuth

#parameter: zip: zip code inputed by the user
#returns: dict in the form of {"city_state", "latitude", "longitude"}
def getCoords(zip):
    #temp zip value for testing 
    #zip = 29020 
    #parameters for api calls
    # note: LIMIT 10 API CALLS PER HOUR. EACH RUN USES 1 CALL
    apiKey = "f9a6ad9cadc70a204ebd25e9e63fdf7a"
    email = "tirthp@g.clemson.edu"
    password = "hurricanehomies"

    #api call and format the data
    zipData = requests.get("https://service.zipapi.us/zipcode/" + str(zip) + "?X-API-KEY=" + str(apiKey) + "&fields=geolocation,population",
    auth=HTTPBasicAuth(email, password))
    zipData = zipData.json()
    
    #checks if api succeded
    if(zipData['status'] == True):
        #combines city and state into a string
        city_state = str(zipData['data']['city']) + ", " + str(zipData['data']['state'])
        #gets lat and long data 
        lat = zipData['data']['latitude']
        longt = zipData['data']['longitude']
        #creates dict with data
        coords =  {"city_state": city_state, "latitude": lat, "longitude": longt}
    else:   
        coords = {"Error": "Unable to fetch geo data"}  
    
    return coords