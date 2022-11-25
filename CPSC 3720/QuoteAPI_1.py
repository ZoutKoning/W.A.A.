import requests

def getQuote():
  category = ''
  api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
  response = requests.get(api_url, headers={'X-Api-Key': 'iQcGzv21kmZDS8B9wGDU4A==NcJpG9qVKQrx0wkz'})
  quoteDict = []
  if response.status_code == requests.codes.ok:
    quoteDict = response.text
  else:
    quoteDict = []
  
  return quoteDict

