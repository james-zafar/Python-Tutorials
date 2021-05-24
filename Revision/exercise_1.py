# Exercise 1
# Customers is a global array of tuples which contain a customer ID and the
# customer's average spend. The format of each tuple is (customer_id, average_spend).
# A function generate_customers() will populate this global array with some data.
# The find_customer function will return the average spend for a given customer ID if
# the customer exists, or None if the customer does not exist. We will test that this
# function works by calling it from main with a series of assert statements to ensure
# the results we get back are correct. At the moment some of the assert statements fail,
# raising an unexpected AssertionError. Can you fix this?

# Extension: Globally scoped variables are generally not a good idea, and should be
# avoided where possible. Can you re-write this exercise to not use global variables?

from typing import Optional

import numpy as np

customers = []


def generate_customers() -> None:
    # Setting a seed ensures that the values generated are consistent.
    np.random.seed(1)
    customers = []
    for i in range(10):
        customer_id = np.random.randint(1000000, 99999999)
        average_spend = round(np.random.uniform(0.01, 200, [1])[0], 2)
        customers.append((customer_id, average_spend))
    print(customers)


def find_customer(customer_id) -> Optional[float]:
    customer_ids = [customer[0] for customer in customers]
    try:
        customer_idx = customer_ids.index(customer_id)
    except ValueError:
        print(f'Customer \'{customer_id}\' not found.')
        return

    return customers[customer_idx][1]


def main() -> None:
    generate_customers()
    average_spend = find_customer(93688513)
    assert average_spend == 37.26
    average_spend = find_customer(73809355)
    assert average_spend == 88.7
    average_spend = find_customer(123456)
    assert average_spend is None


main()
