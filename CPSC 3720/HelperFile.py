# Written by Vedant Patel

import datetime
from QuoteAPI_1 import *
import json
from ForecastWeatherAPI import filterResponse
from CurrentWeatherAPI import filterCurrResponse
from pathlib import Path

# helper class for to call upon when needed to use the helper functions.
class Helper:
    def __init__(self):
        self.QDict = {}
        self.counter = 0
        self.icon = ""
        self.blVal = True
        self.dictList = ""
        self.fp = Path(__file__).with_name('file.json')
    
    # sets the forecast dict list. 
    def setDictList(self, dictL):
        self.dictList = dictL
    # returns the forecast dict list.
    def getDictList(self):
        return self.dictList
    
    # sets the boolean first call variable which use to determine 
    # whether it is the first API call of the app by the user.
    def set_blFirstCall(self, bl_val):
        self.blVal = bl_val
    # returns the boolean first call 
    def get_blFirstCall(self):
        return self.blVal
    
    # sets the weather icon for the current weather. 
    def setWeatherIcon(self, weatherIcon):
        self.icon = weatherIcon
    # returns the weather icon for the current weather
    def getWeatherIcon(self):
        return self.icon

    # sets the quote json dict variable from the file.json
    # whenever it is updated usually first time the user opens the app for the day
    def setQuoteDict(self, dict):
        self.QDict = dict
    # returns the quote json dict variable
    def getQuoteDict(self):
        return self.QDict

    # sets the count. The count is used to monitor how many API calls are made for the day
    # stops it if it goes over 100. 
    def setCount(self, num):
        self.counter = num
    # returns the count
    def getCount(self):
        return self.counter

    # used to over write the file.json file with new/default info
    # date, count and the quote dict value.
    def overWriteFile(self):
        quoteDict = getQuote()
        self.setQuoteDict(quoteDict)
        x = datetime.datetime.now()
        date = x.strftime("%m-%d-%Y")
        Dict = {
            "date": str(date),
            "count": 0,
            "Quote of the day": quoteDict
        }
        wfile = open(self.fp, "w")
        json_object = json.dumps(Dict, indent=4)
        wfile.write(json_object)
        wfile.close()
    
    # used to update the count in the file.json to keep monitoring it 
    # throughout the day.
    def updateCount(self):
        rf = open(self.fp, "r")
        jsonDict = json.load(rf)
        val = jsonDict["count"]
        jsonDict["count"] = val + 1
        self.setCount(int(jsonDict["count"]))
        json_object = json.dumps(jsonDict, indent=4)
        wf = open(self.fp, "w")
        wf.write(json_object)
        wf.close()
        rf.close()

    # used when the user the opens the app. this func gets the quote info
    # from the file.json for quote of the day. 
    def openningApp(self):
        f = open(self.fp, "r")
        x = datetime.datetime.now()
        date = x.strftime("%m-%d-%Y")
        jsonDict = json.load(f)
        if (jsonDict["date"] != date):
            self.overWriteFile()
        else:
            self.setQuoteDict(jsonDict["Quote of the day"])
        f.close()
        
    # use for formatting current weather info into well formatted string.
    def formatCurrWeather(self, Dict):
        formatStr = "Current weather: " + str(Dict["current weather"])
        formatStr = formatStr + "\nCurrent Temp(F): " + str(Dict["current Temp (F)"])
        formatStr = formatStr + "\nHumidity: " + str(Dict["humidity"])
        formatStr = formatStr + "\nWind Speed(MPH): " + str(Dict["windMPH"])
        formatStr = formatStr + "\nPrecip(IN): " + str(Dict["precipIN"])
        return formatStr
        
    # use for formatting forecast weather info into well formatted string.
    def formatForecastWeather(self, Dict):
        formatStr = "Current weather: " + str(Dict["weather"])
        formatStr = formatStr + "\nHi/Low(F): " + str(Dict["maxF"]) + "/" + str(Dict["minF"])
        formatStr = formatStr + "\nFeels like(F): " + str(Dict["feelslikeF"])
        return formatStr
    
    # this func is just for testing out how the current weather info looks in the app
    # without having to call APIs every time since it uses example response json file.
    def testCurr(self):
        f = open("Current.json", "r")
        jsonDict = json.load(f)
        res = filterCurrResponse(jsonDict)
        return res

    # this func is just for testing out how the forecast weather info looks in the app
    # without having to call APIs every time since it uses example response json file.
    def testForecast(self):
        f = open("Forecast.json", "r")
        jsonDict = json.load(f)
        res = filterResponse(jsonDict)
        return res