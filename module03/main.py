# dictionaries

import datetime

transaction = {
    "coin": "bitcoin",
    "amount": 0.5,
    "buy": True,
    "timestamp": datetime.date(2026, 2, 20),
}

transaction_2 = {
    "coin": "ethereum",
    "amount": 1.1,
    "buy": True,
    "timestamp": datetime.date(2026, 2, 21),
}

print(f"{transaction['amount']} of {transaction['coin']}")  # 0.5 of bitcoin

transaction["amount"] = 0.6
transaction["notes"] = "A transaction for a Bitcoin purchase"
del transaction["notes"]

print(transaction["notes"])     # raises KeyError

notes_exist = "notes" in transaction    # False

if "notes" in transaction:
    print(transaction["notes"])
else:
    print("The transaction has no notes")

# lists

transactions = [transaction, transaction_2]

transaction_3 = {
    "coin": "bitcoin",
    "amount": 0.25,
    "timestamp": datetime.date(2026, 2, 22),
    "buy": False # sell
}

transactions.append(transaction_3)

first_transaction = transactions[0]
second_transaction = transactions[1]

if 1 < len(transactions):
    transaction = transactions[1]
    print(transaction["coin"])
else:
    print("Transaction not found")

# exception handling

try:
    transaction = transactions[1]
    print(transaction["coin"])
except IndexError:
    print("Transaction not found")

try:
    print(transaction["notes"])
except KeyError:
    print("Transaction has no notes")


# loops

for transaction in transactions:
    print(transaction["coin"])

for transaction in transactions:
    formatted_timestamp = transaction["timestamp"].strftime("%b. %e, %Y")
    coin = transaction["coin"]
    amount = transaction["amount"]
    action = "Bought" if transaction["buy"] else "Sold"
    notes = transaction["notes"] if "notes" in transaction else "No notes found"

    print(f"Transaction on {formatted_timestamp}")
    print(f"{action} {amount} of {coin}")
    print(f"Notes: {notes}")

try:
    transaction = transactions[1]
    formatted_timestamp = transaction["timestamp"].strftime("%b. %e, %Y")
    coin = transaction["coin"]
    amount = transaction["amount"]
    action = "Bought" if transaction["buy"] else "Sold"
    notes = transaction["notes"] if "notes" in transaction else "No notes found"

    print(f"Transaction on {formatted_timestamp}")
    print(f"{action} {amount} of {coin}")
    print(f"Notes: {notes}")
except IndexError:
    print("Transaction not found")

