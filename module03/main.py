# functions
import datetime

def create_transaction(coin, amount, buy, timestamp, notes):
    transaction = {
        "coin": coin,
        "amount": amount,
        "buy": buy,
        "timestamp": timestamp,
        "notes": notes,
    }

    return transaction

transaction = create_transaction("bitcoin", 0.5, True, datetime.date(2026, 2, 20))
print(transaction["coin"])      # bitcoin

transactions = []
transactions.append(create_transaction("bitcoin", 0.5, True, datetime.date(2026, 2, 20), "Note one"))
transactions.append(create_transaction("ethereum", 1.1, True, datetime.date(2026, 2, 21), "Note two"))
transactions.append(create_transaction("bitcoin", 0.25, False, datetime.date(2026, 2, 22), "Note three"))

def display_transaction(transaction):
    coin = transaction["coin"]
    amount = transaction["amount"]
    action = "Bought" if transaction["buy"] else "Sold"
    formatted_timestamp = transaction["timestamp"].strftime('%b. %e, %Y')
    notes = transaction["notes"] if "notes" in transaction else "No notes found"

    print(f"Transaction on {formatted_timestamp}")
    print(f"{action} {amount} of {coin}")
    print(f"Notes: {notes}")
    print("")

for transaction in transactions:
    display_transaction(transaction)

def create_transaction(coin, amount, buy, notes):
    transaction = {
        "coin": coin,
        "amount": amount,
        "buy": buy,
        "notes": notes,
        "timestamp": datetime.date.today(),
    }

    return transaction

def create_transaction(coin, amount, buy=True, notes=None):
    transaction = {
        "coin": coin,
        "amount": amount,
        "buy": buy,
        "timestamp": datetime.date.today()
    }

    if notes is not None:
        transaction["notes"] = notes

    return transaction

transaction = create_transaction("bitcoin", 0.5)
transaction = create_transaction("bitcoin", 0.25, False)
transaction = create_transaction("bitcoin", 0.25, False, "Selling one quarter bitcoin")
transaction = create_transaction("bitcoin", 0.5, notes="Buying one half a bitcoin")
transaction = create_transaction(amount=0.5, buy=True, notes="Buying one half a bitcoin", coin="bitcoin")

