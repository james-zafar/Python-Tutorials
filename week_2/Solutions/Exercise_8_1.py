# Exercise 8
# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.
# We would like to find all of the circular prime numbers below 2,500

from math import sqrt


def is_prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    square_root = int(sqrt(number)) + 1
    for divisor in range(3, square_root, 2):
        if number % divisor == 0:
            return False
    return True


def get_rotations(number):
    number_as_list = [int(i) for i in str(number)]
    output = []
    for i in range(len(number_as_list)):
        output.append(number_as_list[i:] + number_as_list[:i])
    return output


def is_circular_prime(number):
    number_rotations = get_rotations(number)
    for num in number_rotations:
        if not is_prime(int(''.join(str(i) for i in num))):
            return False

    return True


def main():
    circular_primes = []
    for i in range(5001):
        if is_circular_prime(i):
            circular_primes.append(i)
    print(circular_primes)


main()
