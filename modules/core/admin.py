from application import admin
from .models import User
from flask_peewee.admin import ModelAdmin

class UserAdmin(ModelAdmin):
    pass

admin.register(User)