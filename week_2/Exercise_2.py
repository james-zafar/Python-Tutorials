from typing import Union

# Exercise 2
# We would like to be able to compute simple and compound
# interest on a given sum of money to compute which one yields
# a higher return. The maximum interest rates are defined as global variables
# but may be changed by the user. If the user provides an interest rate
# which is greater than the maximum interest rate then then the
# interest rate provided by the user should be ignored.

# Extension: Can you format the result to print to 2 decimal places?

# Further extension: Can you write a function to report to the user whether simple or
# compound interest yields a higher return for a set amount of money and time period
# using the maximum possible interest rates?


# Maximum simple interest rate is 6%
max_simple_interest = 0.06

# Maximum compound interest rate is 4%
max_compound_interest = 0.04


def calculate_simple_interest(starting_amount: Union[int, float], interest_rate: float, years: int) -> float:
    return starting_amount + (starting_amount * interest_rate * years)


def calculate_compound_interest(starting_amount: Union[int, float], interest_rate: float, years: int) -> float:
    return starting_amount * ((1 + interest_rate) ** years)


# Expected output: 1123.6
print(calculate_simple_interest(1060, 0.10, 1))
# Expected output: 1690.0
print(calculate_simple_interest(1300, 0.10, 5))
# Expected output: 1040.0
print(calculate_compound_interest(1000, 0.10, 1))
# Expected output: 6083.264512000001
print(calculate_compound_interest(5000, 0.10, 5))
