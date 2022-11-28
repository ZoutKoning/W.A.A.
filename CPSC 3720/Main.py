## this is the code file for the main function as well as the regular code to tie GUI with the APIs.

## Imports
from QuoteAPI_1 import *
from ZipAPI import *
from WeatherAPI import *



def Activities(code):
    ActivitiesList = []
    match code:
        case 0,1,2,3:
            #sunny
            dadsad
        case 51,53,55:
            #Drizzle
            fdsf
        case 61,63,65,80,81,82:
            #rainy
            dsad
        case 56,57,66,67:
            #freezing rain/drizzle
            sadsa
        case 71,73,75,77,85,86:
            #snowy
            faffsafs
        case 95,96,99:
            #Thunderstorm
            dsad
            
    return ActivitiesList

def main():
    # User input on the zipcode they want to search the weather on
    zipCode = input ("Enter your zipcode: ")
    
    ## Call Quote API and display the quote of the day
    quote = getQuote()
    
    ## Call the Zip API
    coords = getCoords(zipCode)
    
    ## Call Weather API to get weather
    
    ## Use the weather code to display the activities
    
    
    ## Let the user decide to redo the search or exit. 
    

if __name__ == "__main__":
    main()