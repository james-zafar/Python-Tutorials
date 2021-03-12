# Exercise 5
#  It is not possible to calculate the square root of a negative number
# In this code it results in an error. What input validation could we implement
# to prevent this error from occurring?

import math


def calculate_square_root(number: float) -> float:
    return math.sqrt(number)


calculate_square_root(16)
calculate_square_root(4)
calculate_square_root(-4)
