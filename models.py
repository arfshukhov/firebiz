from peewee import *

db = SqliteDatabase('database.db')


class Countries(Model):
    id = PrimaryKeyField()
    name = TextField(unique=True)
    alpha2 = TextField()
    alpha3 = TextField()
    region = TextField()

    class Meta:
        database = db
        db_table = "Countries"


class Users(Model):
    first_name = CharField(null=False)
    last_name = CharField(null=False)
    email = CharField(max_length=120, unique=True)
    password_hash = TextField()
    phone = CharField(max_length=20, unique=True)
    country_code = CharField(max_length=2)

    class Meta:
        database = db
        db_table = "Users"

