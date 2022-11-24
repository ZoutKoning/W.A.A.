import requests
from requests.auth import HTTPBasicAuth

#parameter: zip: zip code inputed by the user
#returns: array in the form of ["city,state", "latitude", "longitude"]
def getCoords(zip):
    #temp example 
    zip = 29020 
    #parameters for api calls
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
        #puts data into array
        coords = (city_state, zipData['data']['latitude'], zipData['data']['longitude'])
        return coords
    else:   
        print("Error: Unable to fetch geo data")


