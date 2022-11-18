#Cole Ramos Nov 18 2022
import requests
import urlopen
import json

#sets header in request to api 
headers = {
  'Accept': 'application/json'
}
#pulls 1 random quote from the api 
request = requests.get('https://goquotes-api.herokuapp.com/api/v1/random?count=1', headers=headers)

#this is confusing at first but to break it down, the data is in a dict{list[dict{}]}
#pulls desired data out of the dictionary 
quoteData = request.text
data = json.loads(quoteData)
quoteRandom = data['quotes']

#pulls further data out of the list that was stored in the above dict
#DICT IF YOU WANT TO PULL THIS 
display = quoteRandom[0]

#pulls from the dict that was stored in the list
quote = display['text']
author = display['author']

#concatenates 
#STRING IF YOU WANT TO PULL THIS 
fullOutput= '"'+quote+'"'+' -'+author

#test output, ignore thr 200 it just means the connect from url open worked
print(fullOutput)
