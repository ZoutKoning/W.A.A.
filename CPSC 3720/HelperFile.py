import datetime
from QuoteAPI_1 import *
import json

class Helper:
    def __init__(self):
        self.QDict = {}
        self.counter = 0

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

h = Helper()  
h.overWriteFile()
print(h.getQuoteDict())