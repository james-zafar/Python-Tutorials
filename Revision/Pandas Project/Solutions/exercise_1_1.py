# Exercise 1 Solution 1
# A simple solution to this problem would be to change the behaviour of
# the generate_customers function. Line 24 of the original exercises:
#  customers = []
# creates a locally scoped variable called customers, which means when
# we append to customers inside the function, we are appending to the
# local variable customers - the global variable customers remains
# unchanged. Instead we could replace this line with
# global customers
# to reference the global variable customers. Let's see in the next
# solution how we can re-write this code without any global variables.

from typing import Optional

import numpy as np

customers = []


def generate_customers() -> None:
    np.random.seed(1)
    global customers
    for i in range(10):
        customer_id = np.random.randint(1000000, 99999999)
        average_spend = round(np.random.uniform(0.01, 200, [1])[0], 2)
        customers.append((customer_id, average_spend))


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
