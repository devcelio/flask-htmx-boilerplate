from application import db
import peewee as pee
from application import auth
from application.base.models import TimestampableMixin, UUIDModelMixin

class User(auth.User):
    pass

class Client(TimestampableMixin, UUIDModelMixin, db.Model):
    first_name = pee.CharField(max_length=255)
    last_name = pee.CharField(max_length=255)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
