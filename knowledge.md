### Knowledge
```python
import requests
import pandas as pd
import matplotlib as mp
```
##### API
1. __*The Structure of an API URL*__
```mathematica
Root URL + EndPoint + Query Parameters
```
Example: 
`https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currecncy=usd&days=30`

Part | Meaning | Example
---| ---| ---|
Root URL | The main base of the API | https://api.coingecko.com/api/v3/
Endpoint | The specific kind of data you want | coins/bitcoin/market_chart
Query Parameters | The options you specify | vs_currency=usd&days=30

2. __*Endpoint Table for easy use*__

| Purpose | Endpoint | Example | Description |
|----------|-----------|----------|--------------|
| List all supported coins | `/coins/list` | [coins/list](https://api.coingecko.com/api/v3/coins/list) | Returns every coin ID, symbol, and name |
| Get details for one coin | `/coins/{id}` | [coins/bitcoin](https://api.coingecko.com/api/v3/coins/bitcoin) | Market cap, supply, description, links |
| Get market data for coins | `/coins/markets` | `/coins/markets?vs_currency=usd&ids=bitcoin,ethereum` | Current price, market cap, volume, and change |
| Historical price chart | `/coins/{id}/market_chart` | `/coins/bitcoin/market_chart?vs_currency=usd&days=30` | Price, market cap, and volume for the last N days |
| Historical data for one date | `/coins/{id}/history` | `/coins/bitcoin/history?date=01-01-2023&localization=false` | Price info on a specific date |
| Supported currencies | `/simple/supported_vs_currencies` | [supported_vs_currencies](https://api.coingecko.com/api/v3/simple/supported_vs_currencies) | Lists all supported fiat currencies (usd, eur, cny, etc.) |

3. __*Step to check the Data from API*__
```python
import requests
import pandas as pd

# import necessary packages
# requests -> request webs

# step1: input urls & request it
urls = 'https://api.coingecko.com/api/v3/coins/list'
response = requests.get(urls)

# step2: convert the requested texts to json 
data = response.json()

# step3: convert it to dataframe
df = pd.DataFrame(data)

bitcoin = df[df['id'] == 'bitcoin']
```
Example: 
- check the price_change_percentage in the past 24 hours

*Oct. 5th, 2025, Central Time*
```python
r = requests.get("https://api.coingecko.com/api/v3/coins/markets",
                 params={"vs_currency": "usd", "per_page": 10, "page": 1})

df = pd.DataFrame(r.json())
# print(df.columns)

row = [f'mkcp_no.{i}' for i in range(1, len(df) + 1)]
# mkcp = market cap

df_price = pd.DataFrame(r.json(), index = row)[['id', 'current_price', 'price_change_percentage_24h']]
df_price['percent_str'] = df_price

['price_change_percentage_24h'].round(3).astype('str') + '%'

print(df_price.sort_values(by = 'price_change_percentage_24h', ascending = False))

"""
Output: 
                      id  current_price  price_change_percentage_24h percent_str
mkcp_no.8       dogecoin       0.256308                      2.75860      2.759%
mkcp_no.6         solana     230.660000                      1.89106      1.891%
mkcp_no.3         ripple       3.000000                      1.63835      1.638%
mkcp_no.5    binancecoin    1164.120000                      1.11040       1.11%
mkcp_no.9   staked-ether    4519.390000                      1.10751      1.108%
mkcp_no.2       ethereum    4522.730000                      1.06744      1.067%
mkcp_no.1        bitcoin  123191.000000                      1.04099      1.041%
mkcp_no.10          tron       0.341652                      0.46302      0.463%
mkcp_no.7       usd-coin       0.999703                     -0.01020      -0.01%
mkcp_no.4         tether       1.000000                     -0.02857     -0.029%
"""
```