import requests
import pandas as pd

urls = 'https://api.coingecko.com/api/v3/coins/bitmarket_chart'
params = {
    'vs_currency': 'cny',
    'days': 30
}
response = requests.get(urls, params = params)
data = response.json()
print(data)
