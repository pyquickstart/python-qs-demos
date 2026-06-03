from collections import Counter
from typing import Annotated

import typer

from db import CryptoTransaction
from coingecko import get_current_price
from rich import print
from rich.console import Console
from rich.table import Table
from rich.text import Text

app = typer.Typer()


@app.command("add")
def create_transaction(
    coin: str,
    amount: float,
    sell: Annotated[bool, typer.Option("--sell")] = False,
    notes: str = None,
):
    CryptoTransaction.create(coin=coin, amount=amount, buy=not sell, notes=notes).save()
    print(
        f"Added transaction: [blue]{'Bought' if not sell else 'Sold'}[/blue] [bold green]{amount}[/bold green] {coin.capitalize()}"
    )


@app.command("show")
def view_portfolio(currency: Annotated[str, typer.Option("--currency", "-c")] = "usd"):
    coin_amounts = Counter()

    for transaction in CryptoTransaction.select():
        if transaction.buy:
            coin_amounts[transaction.coin] += transaction.amount
        else:
            coin_amounts[transaction.coin] -= transaction.amount

    table = Table(title="Current Portfolio")
    table.add_column("Coin", style="cyan")
    table.add_column("Amount", style="green")
    table.add_column("Current Value", style="magenta")
    price_data = get_current_price(list(coin_amounts.keys()), currency)
    for coin in price_data:
        price = price_data[coin][currency]
        amount = coin_amounts[coin]
        value = amount * price
        table.add_row(coin.capitalize(), f"{amount}", f"{value:.2f} {currency.upper()}")

    console = Console()
    console.print(table)


@app.command("lookup")
def lookup_price(
    coin: str, currency: Annotated[str, typer.Option("--currency", "-c")] = "usd"
):
    price_data = get_current_price([coin], currency)
    output = Text("Price data for ")
    output.append(coin.capitalize(), style="blue")
    if coin in price_data:
        price = price_data[coin][currency]
        output.append(f" {price:.2f} {currency.upper()}", style="bold green")
    else:
        output.append(" not found", style="bold red")

    console = Console()
    console.print(output)

@app.command("history")
def view_history():
    table = Table(title="Transaction History")
    table.add_column("Date", style="cyan")
    table.add_column("Coin", style="blue")
    table.add_column("Amount", style="green")
    table.add_column("Type", style="magenta")
    table.add_column("Notes", style="yellow")

    for transaction in CryptoTransaction.select().order_by(CryptoTransaction.coin, CryptoTransaction.timestamp.desc()):
        date_str = transaction.timestamp.strftime("%Y-%m-%d")
        type_str = "Buy" if transaction.buy else "Sell"
        notes_str = transaction.notes if transaction.notes else ""
        table.add_row(date_str, transaction.coin.capitalize(), f"{transaction.amount}", type_str, notes_str)

    console = Console()
    console.print(table)


if __name__ == "__main__":
    app()
