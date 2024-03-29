from flask import Flask
from flask_peewee.db import Database
from .utils.registry import configure_modules
from flask_peewee.admin import Admin
from flask_peewee.auth import Auth

app = Flask(__name__, template_folder='../templates', static_folder='../lib')
app.config
app.config.from_object('application.settings')
db = Database(app)


auth = Auth(app, db)
admin = Admin(app, auth)

configure_modules(app)

admin.setup()

__all__ = ['app', 'db', 'admin', 'auth']