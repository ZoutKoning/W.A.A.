# Written by Vedant Patel

import datetime
from QuoteAPI_1 import *
import json
from ForecastWeatherAPI import filterResponse
from CurrentWeatherAPI import filterCurrResponse

class Helper:
    def __init__(self):
        self.QDict = {}
        self.counter = 0
        self.icon = ""
        self.blVal = True
        self.dictList = ""
    
    def setDictList(self, dictL):
        self.dictList = dictL
    
    def getDictList(self):
        return self.dictList
    
    def set_blFirstCall(self, bl_val):
        self.blVal = bl_val
        
    def get_blFirstCall(self):
        return self.blVal
    
    def setWeatherIcon(self, weatherIcon):
        self.icon = weatherIcon
    
    def getWeatherIcon(self):
        return self.icon

    def setQuoteDict(self, dict):
        self.QDict = dict

    def getQuoteDict(self):
        return self.QDict

    def setCount(self, num):
        self.counter = num

    def getCount(self):
        return self.counter

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
        wfile = open("file.json", "w")
        json_object = json.dumps(Dict, indent=4)
        wfile.write(json_object)
        wfile.close()
        
    def updateCount(self):
        rf = open("file.json", "r")
        jsonDict = json.load(rf)
        val = jsonDict["count"]
        jsonDict["count"] = val + 1
        self.setCount(int(jsonDict["count"]))
        json_object = json.dumps(jsonDict, indent=4)
        wf = open("file.json", "w")
        wf.write(json_object)
        wf.close()
        rf.close()

    def openningApp(self):
        f = open("file.json", "r")
        x = datetime.datetime.now()
        date = x.strftime("%m-%d-%Y")
        jsonDict = json.load(f)
        if (jsonDict["date"] != date):
            self.overWriteFile()
        else:
            self.setQuoteDict(jsonDict["Quote of the day"])
        f.close()
        
    def formatCurrWeather(self, Dict):
        formatStr = "Current weather: " + str(Dict["current weather"])
        formatStr = formatStr + "\nCurrent Temp(F): " + str(Dict["current Temp (F)"])
        formatStr = formatStr + "\nHumidity: " + str(Dict["humidity"])
        formatStr = formatStr + "\nWind Speed(MPH): " + str(Dict["windMPH"])
        formatStr = formatStr + "\nPrecip(IN): " + str(Dict["precipIN"])
        return formatStr
        
    def formatForecastWeather(self, Dict):
        formatStr = "Current weather: " + str(Dict["weather"])
        formatStr = formatStr + "\nHi/Low(F): " + str(Dict["maxF"]) + "/" + str(Dict["minF"])
        formatStr = formatStr + "\nFeels like(F): " + str(Dict["feelslikeF"])
        return formatStr
    
    def testCurr(self):
        f = open("Current.json", "r")
        jsonDict = json.load(f)
        res = filterCurrResponse(jsonDict)
        return res

    def testForecast(self):
        f = open("Forecast.json", "r")
        jsonDict = json.load(f)
        res = filterResponse(jsonDict)
        return res