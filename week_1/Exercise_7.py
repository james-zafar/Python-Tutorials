# Exercise 7
# To check is a number if prime we can check if any divisor up to the square root
# of the input number has a modulo of 0, if it does then the number is not prime.
# 2 is a valid prime number, but in this example an input of 2 returns False.
# Why is this?

import math


def is_prime(number: int) -> bool:
    if number <= 2:
        return False
    square_root = int(math.sqrt(number)) + 1
    for divisor in range(3, square_root, 2):
        if number % divisor == 0:
            return False
    return True


print(is_prime(11))
print(is_prime(16))
print(is_prime(2))
