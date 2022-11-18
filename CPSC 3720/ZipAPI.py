import requests
from requests.auth import HTTPBasicAuth

#parameter: zip: zip code inputed by the user
#returns: 2d int array contaning lat and long values. Length of array: 0 < len(array) < 4
def getCoords(zip):
    #temp example 
    zip = 29020 
    #parameters for api calls
    apiKey = "f9a6ad9cadc70a204ebd25e9e63fdf7a"
    email = "tirthp@g.clemson.edu"
    password = "hurricanehomies"
    radius = 10

    #invokes request to return a list of zip codes within the specified radius 
    zipList = requests.get("https://service.zipapi.us/zipcode/radius/" + str(zip) + "?X-API-KEY=" + str(apiKey) + "&radius=" + str(radius), auth=HTTPBasicAuth(email, password))   

    #extract the part we need
    zipList = zipList.json()
    if(zipList['status'] == False):
        print("Error: Unable to fetch radius data")
    zipList = zipList['data']
    
    coordList = []

    for i in range(len(zipList)):
        if i < 3: 
            zipData = requests.get("https://service.zipapi.us/zipcode/" + str(zipList[i]['ZipCode']) + "?X-API-KEY=" + str(apiKey) + "&fields=geolocation,population",
            auth=HTTPBasicAuth(email, password))
            zipData = zipData.json()
            if(zipData['status'] == True):
                city_state = str(zipData['data']['city']) + ", " + str(zipData['data']['state'])
                coords = (city_state, zipData['data']['latitude'], zipData['data']['longitude'])
                coordList.append(coords)
            else:   
                print("Error: Unable to fetch geo data")
        else:
            break

    return coordList