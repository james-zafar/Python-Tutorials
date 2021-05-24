# Exercise 3
# Customer Management system
# The goal of this exercise is to give an example of writing clean,
# concise code. Customers are stored as a CSV called 'exercise_4.csv'.
# The first time you run this program that file will not exist - it
# will be created an populated for you. There are 4 options the user
# can choose to amend or view customer data.
# Read the below code to understand what it is doing and complete the
# exercises below. Some functions have comments to signify that they
# should not be edited, this means you should be able to complete all
# exercises without changing anything in these functions.

# (I) If the user provides no input when prompted the program should call
# the save_data() function and exit, but it doesn't. Can you fix this?
# (II) Complete the add_customer() function
# (III) Enhance the print_average() function following the specification
# provided in the function body

import string

import numpy as np
import pandas as pd


def save_data(df: pd.DataFrame) -> None:
    # DO NOT EDIT
    df.to_csv('exercise_3.csv', index=False)


def generate_customer_id():
    # DO NOT EDIT
    return ''.join([np.random.choice(list(string.digits)) for _ in range(8)])


def generate_customer_data() -> pd.DataFrame:
    # DO NOT EDIT
    customers_df = pd.DataFrame()
    for i in range(10):
        customer_id = generate_customer_id()
        average_spend = round(np.random.uniform(0.01, 200, [1])[0], 2)
        customer_type = np.random.choice(['standard', 'prime', 'vip'])
        shops_online = np.random.choice(['Y', 'N'])
        customers_df = customers_df.append({'customer_id': customer_id, 'customer_type': customer_type,
                                            'average_spend': average_spend, 'online': shops_online}, ignore_index=True)

    return customers_df


def print_options():
    # DO NOT EDIT
    options = ['1 - Print average spend', '2 - Print customer summary',
               '3 - Add new customer', '4 - Remove customer']
    print(*options, sep='\n')


def get_user_input():
    # DO NOT EDIT
    return input('Enter an option (skip to exit): ') or -1


def read_data(file_name: str = 'exercise_3.csv') -> pd.DataFrame:
    # DO NOT EDIT
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        return generate_customer_data()


def print_average(customers: pd.DataFrame) -> pd.DataFrame:
    print(f'The average spend of all customers is £{round(customers.average_spend.mean(), 2)}')
    # TODO:
    #  Generate a random normally distributed number.
    #  If the number is > 0.54 increase ALL values in the average_spend column
    #  by 2%. If the number is > 0.96 increase ALL values in the average_spend
    #  column by 6%, else decrease ALL values by 3%.
    return customers


def print_summary(customers: pd.DataFrame) -> pd.DataFrame:
    print('Total number of customers:', len(customers))
    print('Total number of prime customers:', len(customers[customers.customer_type == 'prime']))
    print('Total number of VIP customers:', len(customers[customers.customer_type == 'vip']))
    print('Total number of online customers:', len(customers[customers.online == 'Y']))
    customers['customer_type'] = np.random.permutation(customers['customer_type'].values)
    customers['online'] = np.random.permutation(customers['online'].values)
    return customers


def add_customer(customers: pd.DataFrame) -> pd.DataFrame:
    # TODO: Implement this function
    #  The user should provide:
    #    - an average spend rounded to 2 decimal places
    #    - A customer type which must be either standard, prime or vip
    #    - A Y/N option to specify whether the customer is online only
    #    - If any input is invalid it should be requested again in a loop until valid input is provided
    #  A customer ID should be generated via the generate_customer_id() function
    #  The new customer should be appended to the customers df and the new updated df returned
    return customers


def remove_customer(customers: pd.DataFrame) -> pd.DataFrame:
    user_id = input('Enter the customer ID you would like to remove: ')
    if customers[customers['customer_id'].isin([user_id])].empty:
        print(f'Error, no customer exists with the ID \'{user_id}\'')
        return customers
    return customers[customers.customer_id != user_id]


def main() -> None:
    customers_df = read_data()
    functions_dict = {1: print_average, 2: print_summary, 3: add_customer, 4: remove_customer}
    loop_count = 0
    while True:
        if loop_count % 3 == 0:
            print_options()
        user_input = int(get_user_input())
        try:
            customers_df = functions_dict[user_input](customers_df)
        except KeyError:
            print(f'The option \'{user_input}\' is not a valid choice, to exit leave input field blank.')

        loop_count += 1


main()
