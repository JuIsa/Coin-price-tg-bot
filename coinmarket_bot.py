import json
import config
from requests import Request, Session

def check(msg):
  url =   "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
  headers  = {
    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY': config.coinapi 
  }
  
  session = Session()
  session.headers.update(headers)
  crypto_token = msg
  # indx = crypto_token.index(' ')+1
  # print(f"{indx}, {len(crypto_token)}")
  # crypto_token = crypto_token[indx:len(crypto_token)]

  crypto_token = crypto_token.upper()
  print(crypto_token)
  parameters = {
    'symbol':crypto_token,
    'convert': 'USD'
  }

  response = session.get(url, params= parameters)
  print(json.loads(response.text))
  err = json.loads(response.text)['status']['error_code']
  if err == 0:
    price = (json.loads(response.text)['data'][crypto_token]['quote']['USD']['price'])
    price = round(price,2)
    print(price)

    price = round(price,2)
  else:
    price =  'не правильный токен'
  return price