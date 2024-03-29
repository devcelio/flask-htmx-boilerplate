DEBUG = True

SECRET_KEY = 'sssshhhh'
DATABASE = {
    'name': 'database.db',
    'engine': 'peewee.SqliteDatabase',
}

MODULES = [
    'modules.core',
    'modules.components',
]
