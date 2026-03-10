import requests

stock_name = 'TSLA'
company_name = 'Tesla Inc'

Stock_endpoints = 'https://www.alphavantage.co/query'


stock_api_key = 'QI7Z41HCW4C5T5YS'

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=QI7Z41HCW4C5T5YS

stock_api_prameters = {
     'function': 'TIME_SERIES_DAILY',
     'symbol': 'TSLA',
     'apikey': 'QI7Z41HCW4C5T5YS'
 }

response = requests.get(url=Stock_endpoints, params=stock_api_prameters)
print(response.json())