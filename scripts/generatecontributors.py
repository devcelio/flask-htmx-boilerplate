from application import app, auth
from faker import Faker
from modules.core.models import Client

fake = Faker()

def run():
    amount = int(input("Amount to generate: "))

    for _ in range(amount):
        Client.create(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
if __name__ == '__main__':
    run()