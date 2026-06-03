import datetime
from peewee import Model, TextField, FloatField, BooleanField, DateField, SqliteDatabase

db = SqliteDatabase("porfolio.db")

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

if __name__ == "__main__":
    db.connect()
    db.create_tables([CryptoTransaction])

    CryptoTransaction.create(coin="bitcoin", amount=0.5, notes="Initial purchase")
    CryptoTransaction.create(coin="ethereum", amount=1.1)
    CryptoTransaction.create(coin="bitcoin", amount=0.25, buy=False)

    for transaction in CryptoTransaction.select():
        print(transaction)