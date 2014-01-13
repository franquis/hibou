from peewee import *

db = SqliteDatabase('../databases/production.sqlite')
#db = MySQLDatabase('nac2', host="localhost", user="root", passwd="bonjour")


class HibouModel(Model):
    class Meta:
        database = db

class User(HibouModel):
	firstname = CharField()
	lastname = CharField()
	email = CharField()
	password = CharField()
	role = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)

class Client(HibouModel):
	name = CharField()
	description = CharField(null=True)
	client = ForeignKeyField(User, null=True)
	client_secret = CharField(max_length=55, unique=True, index=True)
	is_confidential = BooleanField()
	_redirect_uris = CharField(null=True)
	_default_scopes = CharField(null=True)

class Grant(HibouModel):
	user = ForeignKeyField(User, cascade=True)
	client = ForeignKeyField(Client)
	code = CharField(max_length=255, index=True)
	redirect_uri = CharField()
	expires = DateTimeField()
	_scopes = CharField()

class Token(HibouModel):
	client = ForeignKeyField(Client)
	user = ForeignKeyField(User)
	token_type = CharField()
	access_token = CharField(max_length=255, unique=True)
	refresh_token = CharField(max_length=255, unique=True)
	expires = DateTimeField()
	_scopes = CharField()