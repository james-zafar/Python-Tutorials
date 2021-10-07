# Exercise 3
# The inputs are printed in the wrong order. The expected output is
#  Name: {name}
# Email: {email}
# Postcode: {postcode}

def print_details(name: str, email: str, postcode: str) -> None:
    print('Name: ', name)
    print('Email:', email)
    print('Postcode:', postcode)


def get_user_details() -> None:
    name = input('Enter your name: ')
    email = input('Enter your email address: ')
    postcode = input('Enter your postcode: ')
    print_details(email, name, postcode)


get_user_details()
