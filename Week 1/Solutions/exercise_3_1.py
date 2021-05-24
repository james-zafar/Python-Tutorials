# Exercise 3
# The inputs are printed in the wrong order. The expected output is
#  Name: {name}
# Email: {email}
# Postcode: {postcode}

def print_details(name: str, email: str, postcode: str):
    print('Name: ', name)
    print('Email:', email)
    print('Postcode:', postcode)


def get_user_details():
    name = input('Enter your name: ')
    email = input('Enter your email address: ')
    postcode = input('Enter your postcode: ')
    # It is important to ensure the arguments you pass to a function
    # are in the correct order. print_details() expects (name, email, postcode)
    # but we originally passed (email, name, postcode)
    print_details(name, email, postcode)


get_user_details()
