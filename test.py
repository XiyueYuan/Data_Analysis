import requests
import pandas as pd
import matplotlib as mp

r = requests.get("https://api.coingecko.com/api/v3/coins/markets",
                 params={"vs_currency": "usd", "per_page": 10, "page": 1})
df = pd.DataFrame(r.json())
# print(df.columns)
row = [f'mkcp_no.{i}' for i in range(1, len(df) + 1)]
print(row)
df_price = pd.DataFrame(r.json(), index = row)[['id', 'current_price', 'price_change_percentage_24h']]
df_price['percent_str'] = df_price['price_change_percentage_24h'].round(3).astype('str') + '%'
print(df_price.sort_values(by = 'price_change_percentage_24h', ascending = False))
