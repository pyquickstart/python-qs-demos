import os
import requests
from dotenv import load_dotenv

load_dotenv()

coingecko_api_key = os.getenv("COINGECKO_API_KEY")

# retrieving a single price

currency = "USD"
coin = "bitcoin"
url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies={currency}&ids={coin}&x_cg_demo_api_key={coingecko_api_key}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    price = data["bitcoin"]["usd"]
    print(f"The current price of {coin.capitalize()} is {price} {currency}")
else:
    print("Could not get any data.")

# retrieving multiple prices and currencies in the same request

coins = ["bitcoin", "ethereum"]
currencies = ["USD", "GBP"]
base_url = "https://api.coingecko.com/api/v3/simple/price"
qs = f"?vs_currencies={','.join(currencies)}&ids={','.join(coins)}&x_cg_demo_api_key={coingecko_api_key}"
response = requests.get(base_url + qs)  # the '+' operator concatenates two strings

if response.status_code == 200:
    data = response.json()
    for coin in data.keys():  # the keys of the response JSON are the coins
        for currency in data[
            coin
        ].keys():  # each coin key has a JSON object with the currencies as keys
            price = data[coin][currency]
            print(
                f"The current price of {coin.capitalize()} in {currency.upper()} is {price}"
            )
else:
    print("Could not get any data.")