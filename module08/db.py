import datetime

from peewee import (
    BooleanField,
    DateField,
    SqliteDatabase,
    Model,
    CharField,
    FloatField,
    TextField,
)

db = SqliteDatabase("module08.sqlite")


class CryptoTransaction(Model):
    coin = CharField()
    amount = FloatField()
    buy = BooleanField(default=True)
    timestamp = DateField(default=datetime.date.today)
    notes = TextField(null=True)

    class Meta:
        database = db


db.connect()
db.create_tables([CryptoTransaction])
