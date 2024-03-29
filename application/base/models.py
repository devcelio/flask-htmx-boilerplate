import peewee as pee
from datetime import datetime
from application import db

class UUIDModelMixin(db.Model):
    id = pee.UUIDField(primary_key=True)

    class Meta:
        abstract = True

class TimestampableMixin(db.Model):
    created_at = pee.DateTimeField(default=datetime.now)
    updated_at = pee.DateTimeField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
    
    class Meta:
        abstract = True