import flask

from flask_script import Manager

from application import app

manager = Manager(app)

@manager.command
def create_tables():
    print("Creating tables...")

if __name__ == "__main__":
    manager.run()