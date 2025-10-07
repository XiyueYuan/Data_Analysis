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
4. `Group_by` and `.to_string()`

*Oct. 6th, 2025, Central Time*
```python
#.to_string(index = False) can hide the index when print
print(df_price.sort_values(by = 'price_change_percentage_24h', ascending = False).to_string(index = False))

# Here is the result of the top twenty market_cap coins ranked by its price change within 24 hours, we will group them next
"""
id  current_price  price_change_percentage_24h percent_str
         chainlink      23.470000                      8.77464      8.775%
          dogecoin       0.265569                      5.52504      5.525%
       binancecoin    1223.920000                      4.80099      4.801%
           cardano       0.874644                      4.62363      4.624%
          ethereum    4680.640000                      4.15790      4.158%
     wrapped-steth    5687.410000                      4.15296      4.153%
      staked-ether    4677.380000                      4.04258      4.043%
wrapped-beacon-eth    5047.120000                      3.99535      3.995%
           stellar       0.407960                      2.56475      2.565%
      figure-heloc       0.997579                      2.26664      2.267%
               sui       3.620000                      2.03777      2.038%
            solana     232.280000                      1.71081      1.711%
              tron       0.346613                      1.68025       1.68%
       avalanche-2      30.520000                      1.64116      1.641%
   wrapped-bitcoin  124927.000000                      1.46572      1.466%
           bitcoin  124922.000000                      1.38116      1.381%
            ripple       2.990000                      1.03929      1.039%
       ethena-usde       1.000000                      0.06717      0.067%
            tether       1.000000                      0.00299      0.003%
          usd-coin       0.999705                     -0.00576     -0.006%
"""
# categories by bin
bins = [0, 1, 10, 100, 1000, 10000, 300000]
labels = ['<1', '1-10', '10-100', '100-1000', '1000-10000', '>10000']

# pd.cut to group 
df['price_group'] = pd.cut(df['current_price'], bins = bins, labels = labels, right = False)

# group by prices
for group_name, group_data in df.groupby('price_group'):
    print(f"\n{group_name}:")
    print(group_data[['id', 'current_price']].to_string(index=False))
"""

<1:
          id  current_price
    usd-coin       0.999805
    dogecoin       0.267271
        tron       0.347048
     cardano       0.877330
     stellar       0.409170
figure-heloc       0.997579

1-10:
         id  current_price
     ripple          3.000
     tether          1.000
ethena-usde          1.001
        sui          3.630

10-100:
         id  current_price
  chainlink          23.68
avalanche-2          30.51

100-1000:
    id  current_price
solana         232.91

1000-10000:
                id  current_price
          ethereum        4696.35
       binancecoin        1222.36
      staked-ether        4692.53
     wrapped-steth        5705.00
wrapped-beacon-eth        5068.03

>10000:
             id  current_price
        bitcoin       125024.0
wrapped-bitcoin       125081.0
"""
```
