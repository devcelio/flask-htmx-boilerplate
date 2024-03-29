from application import app, auth
from getpass import getpass
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def prompt(label, validators=None, hide=False, confirm=False):
    get_input = input if not hide else getpass
    validators = validators or []

    def inner_value_confirm(value, confirm):
        if confirm:
            confirm = get_input(f'Confirm {label}: ')
            if confirm == value:
                return value
            else:
                return None
        return value
    
    while value := get_input(f'{label}: '):
        value = inner_value_confirm(value, confirm)
        if value is None:
            print(f'Different {label} values.')
            continue
        if not validators:
            return value
        if all(map(lambda validate: validate(value), validators)):
            return value
        print(f"Invalid {label}")


def run():
    username = prompt("Username")
    email = prompt("Email", [is_valid_email])
    password = prompt("Password", hide=True, confirm=True)

    admin = auth.User(username=username, email=email, admin=True, active=True)
    admin.set_password(password)
    admin.save()
    print("Admin user created successfully")

if __name__ == '__main__':
    run()