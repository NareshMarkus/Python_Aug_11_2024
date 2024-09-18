# terminal: pip insall requests
import requests
'''
url = "https://www.onlinekhabar.com/smtm/home/trending"

r = requests.get(url=url)
if r.status_code == 200:
    print(r.json())
else:
    print("Something went wrong")

a = r.json()

x = a['response'][0]['ticker']
print(x)
'''


'''
url = "https://www.onlinekhabar.com/smtm/home/trending"

r = requests.get(url=url)
if r.status_code == 200:
  response = r.json()
  result = response['response']
  
  for stock in result:
    print(f"{stock['ticker_name']} : {stock['ticker']} : {stock['latest_price']}")
else:
  print("Something went wrong")
'''


url = "https://www.onlinekhabar.com/smtm/home/trending"

r = requests.get(url=url)
if r.status_code == 200:
  data = r.json()
  
  for i in data['response']:
    print(f"ticker_name = {i['ticker_name']} \t ticker = {i['ticker']} \t latest_price = {i['latest_price']}")
else:
  print("Something went wrong")
