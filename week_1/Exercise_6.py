# Exercise 6
# When running main() we enter an infinite loop. A correct implementation would exit the loop
# when the user inputs 'N' or 'n'

def process_user(name: str, postcode: str, phone_number: str):
    print('Name:', name)
    print('Postcode:', postcode)
    print('Contact Number:', phone_number)


def main():
    while True:
        name = input('Enter your name: ')
        postcode = input('Enter your post code: ')
        phone_number = input('Enter a contact number: ')
        process_user(name, postcode, phone_number)
        add_again = input('Add another user? Y/N ').lower()
        if add_again == 'N':
            break


main()
