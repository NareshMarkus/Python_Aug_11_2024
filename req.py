# terminal: pip insall requests
'''
import requests
url = "https://www.onlinekhabar.com/smtm/home/trending"

r = requests.get(url=url)
if r.status_code == 200:
    print(r.json())
    print(r.text())
else:
    print("Something went wrong")
'''


'''
url = "https://www.onlinekhabar.com/smtm/home/trending"

r = requests.get(url=url)
if r.status_code == 200:
  data = r.json()
  
  for i in data['response']:
    print(f"ticker_name = {i['ticker_name']} \t ticker = {i['ticker']} \t latest_price = {i['latest_price']}")
else:
  print("Something went wrong")
''' 

import requests
import datetime
url = "https://www.onlinekhabar.com/smtm/home/trending"
token = "7356830909:AAFzKSWN6WB80mCh9W687HAYzEcTwzaaE_0"
chat_id = "-1002345767590"
tele_url = f"https://api.telegram.org/bot{token}/sendMessage" 

print(datetime.datetime.now())
r = requests.get(url=url)
if r.status_code == 200:
  response = r.json()
  result = response['response']
  
  for stock in result:
    data = f"{stock['ticker_name']} : {stock['ticker']} : {stock['latest_price']}"
    payload = {
        "chat_id": chat_id,
        "text": data,
        "parse_mode": "HTML",
    }
    r = requests.post(tele_url, data=payload)
else:
  print("Something went wrong")