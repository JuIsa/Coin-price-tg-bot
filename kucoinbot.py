from kucoin.client import Market

def check(tkn):
  client = Market(url='https://api.kucoin.com')
  fprice = client.get_fiat_price()
  tkn = tkn.upper()
  tknprice = fprice[tkn]
  return str(tknprice)

