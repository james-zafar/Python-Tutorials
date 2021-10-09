# Exercise 5
# In this exercise we will generate random customer data to
# add to a pandas DataFrame. We would like to get some
# statistics about the customer information that has been
# generated. For example the select_by_spend() function will
# print all customers who have an average spend about a given value.
# Can you implement the function get_customer_by_type()?

# Extension: Can you print the average spend of all customer combined?

# Further extension: Can you change the generate_customer_data() function
# to generate and return a DataFrame object?

import string

import numpy as np
import pandas as pd


def random_date_generator(start_date: str, max_range: int) -> np.datetime64:
    random_date = np.datetime64(start_date) + np.random.randint(0, max_range)
    return random_date


def generate_customer_data(count: int) -> list[dict]:
    customers = []
    for i in range(count):
        customer_id = ''.join([np.random.choice(list(string.ascii_letters)) for _ in range(10)])
        average_spend = np.random.uniform(0.01, 120, [1])[0]
        customer_type = np.random.choice(['standard', 'premium', 'exclusive'])
        date_joined = random_date_generator('2017-10-10', 1000)
        customers.append({'customer_id': customer_id, 'customer_type': customer_type,
                          'average_spend': average_spend, 'date_joined': date_joined})
    return customers


def select_by_spend(customers: pd.DataFrame, avg_spend: float) -> None:
    selected_custs = customers.loc[customers['average_spend'] >= avg_spend]
    print(f'The following customers have an average spend of greater than or equal to {avg_spend}')
    print(selected_custs)


def get_customer_by_type(customers: pd.DataFrame, cust_type: str) -> None:
    pass
    # TODO: This function should select all customers with the given
    #  "cust_type" and print their details.


def main() -> None:
    customers = generate_customer_data(10)
    customers_df = pd.DataFrame(customers)
    select_by_spend(customers_df, 60)
    get_customer_by_type(customers_df, 'exclusive')


main()
