import requests

# got API Info/code from https://api-ninjas.com/api/quotes

def getQuote():
  category = ''
  api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
  response = requests.get(api_url, headers={'X-Api-Key': 'iQcGzv21kmZDS8B9wGDU4A==NcJpG9qVKQrx0wkz'})

  if response.status_code == requests.codes.ok:
    resp_json = response.json()
    qDict = resp_json[0]
  else:
    qDict = {
      "quote": "Error: Using Quote API with the GET request",
      "author": " ",
      "category": " "
    }
    
  return qDict


