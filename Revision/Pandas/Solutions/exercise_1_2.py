# Exercise 1 Solution 2
# Here we will re-write the solution used in exercises_1_1.py to not
# use any global variables.
# Note: if you are running a Python version of <= 3.8 you may see some
# some errors when running this solution. If this is the case for you,
# then try removing the following:
# Line 14, remove "-> list[tuple]"
# Line 26, remove ": list[tuple]"

from typing import Optional

import numpy as np


def generate_customers() -> list[tuple]:
    customers = []
    np.random.seed(1)
    for i in range(10):
        customer_id = np.random.randint(1000000, 99999999)
        average_spend = round(np.random.uniform(0.01, 200, [1])[0], 2)
        customers.append((customer_id, average_spend))

    return customers


def find_customer(customers: list[tuple], customer_id: int) -> Optional[float]:
    customer_ids = [customer[0] for customer in customers]
    try:
        customer_idx = customer_ids.index(customer_id)
    except ValueError:
        print(f'Customer \'{customer_id}\' not found.')
        return

    return customers[customer_idx][1]


def main() -> None:
    customers = generate_customers()
    average_spend = find_customer(customers, 93688513)
    assert average_spend == 37.26
    average_spend = find_customer(customers, 73809355)
    assert average_spend == 88.7
    average_spend = find_customer(customers, 123456)
    assert average_spend is None


main()
