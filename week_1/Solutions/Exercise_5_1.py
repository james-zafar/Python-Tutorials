# Exercise 5
# it is not possible to calculate the square root of a negative number
# In this code it results in an error. What input validation could we implement
# to prevent this error from occurring?

import math


def calculate_square_root(number: float) -> float:
    return math.sqrt(number)


# calculate_square_root(-4)


def main():
    while True:
        user_input = input('Enter a number, or enter N to exit: ')
        if user_input.lower() == 'n':
            break
        try:
            input_as_flaot = float(user_input)
            if input_as_flaot < 0:
                print('Error: It is not possible to compute the square root of a negative number!')
                continue
            print(f'The square root of {user_input} is {calculate_square_root(input_as_flaot)}')
        except ValueError:
            print(f'Error: \'{user_input}\' is not a number')


main()
