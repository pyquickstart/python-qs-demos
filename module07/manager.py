import datetime
import os
from collections import Counter
from typing import Annotated

import requests
import typer
from dotenv import load_dotenv
from peewee import Model, TextField, FloatField, BooleanField, DateField, SqliteDatabase

load_dotenv()

app = typer.Typer()
coingecko_api_key = os.getenv("COINGECKO_API_KEY")
db = SqliteDatabase("portfolio.db")


class CryptoTransaction(Model):
    coin = TextField()
    amount = FloatField()
    buy = BooleanField(default=True)
    timestamp = DateField(default=datetime.date.today)
    notes = TextField(null=True)

    def __str__(self):
        return f"<CryptoTransaction {self.coin} | {self.amount} | {'buy' if self.buy else 'sell'}>"

    class Meta:
        database = db


db.connect()
db.create_tables([CryptoTransaction], safe=True)


def get_current_price(coins, currency):
    base_url = "https://api.coingecko.com/api/v3/simple/price"
    qs = f"?vs_currencies={currency}&ids={','.join(coins)}&x_cg_demo_api_key={coingecko_api_key}"
    response = requests.get(base_url + qs)
    if response.status_code == 200:
        return response.json()
    else:
        typer.echo("Could not get price data.")
        return {}


@app.command("add")
def create_transaction(
    coin: str,
    amount: float,
    sell: Annotated[bool, typer.Option("--sell")] = False,
    notes: str = None,
):
    CryptoTransaction.create(coin=coin, amount=amount, buy=not sell, notes=notes).save()
    typer.echo(
        f"Added transaction: {'Bought' if not sell else 'Sold'} {amount} {coin.capitalize()}"
    )


@app.command("show")
def view_portfolio(currency: Annotated[str, typer.Option("--currency", "-c")] = "usd"):
    coin_amounts = Counter()

    for transaction in CryptoTransaction.select():
        if transaction.buy:
            coin_amounts[transaction.coin] += transaction.amount
        else:
            coin_amounts[transaction.coin] -= transaction.amount

    typer.echo("Current Portfolio:")
    price_data = get_current_price(list(coin_amounts.keys()), currency)
    for coin in price_data:
        price = price_data[coin][currency]
        amount = coin_amounts[coin]
        value = amount * price
        typer.echo(
            f"\t{amount} {coin.capitalize()}, Current Value: {value:.2f} {currency.upper()}"
        )


if __name__ == "__main__":
    app()
