import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_current_price(coins, currency="usd"):
    coingecko_api_key = os.getenv("COINGECKO_API_KEY")
    coin_ids = ",".join(coins)
    response = requests.get(
        f"https://api.coingecko.com/api/v3/simple/price?vs_currencies={currency}&ids={coin_ids}&x_cg_demo_api_key={coingecko_api_key}"
    )
    return response.json()
