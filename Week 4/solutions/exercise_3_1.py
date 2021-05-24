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
    df.to_csv('exercise_3.csv', index=False)


def generate_customer_id():
    return ''.join([np.random.choice(list(string.digits)) for _ in range(8)])


def generate_customer_data() -> pd.DataFrame:
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
    options = ['1 - Print average spend', '2 - Print customer summary',
               '3 - Add new customer', '4 - Remove customer']
    print(*options, sep='\n')


def get_user_input():
    return input('Enter an option (skip to exit): ') or -1


def read_data(file_name: str = 'exercise_3.csv') -> pd.DataFrame:
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        return generate_customer_data()


def print_average(customers: pd.DataFrame) -> pd.DataFrame:
    print(f'The average spend of all customers is £{round(customers.average_spend.mean(), 2)}')
    rand_no = np.random.randn()
    if rand_no > 0.54:
        customers['average_spend'] = customers['average_spend'] * 1.02
    elif rand_no > 0.95:
        customers['average_spend'] = customers['average_spend'] * 1.06
    else:
        customers['average_spend'] = customers['average_spend'] * 0.97
    customers['average_spend'] = customers.average_spend.round(2)
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
    avg_spend = round(float(input('Enter the customers average spend: ')), 2)
    customer_type = input('Enter the customer type (standard/prime/vip): ').lower()
    while customer_type not in ['standard', 'prime', 'vip']:
        print('Customer type is invalid.')
        customer_type = input('Enter the customer type (standard/prime/vip): ').lower()
    online = input('Is the customer an online only customer? (Y/N): ').upper()
    while online != 'N' and online != 'Y':
        print('Error response for customer is online only must be \'Y\' or \'N\'.')
        online = input('Is the customer an online only customer? (Y/N): ').upper()
    customer_id = generate_customer_id()

    return customers.append({'customer_id': customer_id, 'customer_type': customer_type,
                             'average_spend': avg_spend, 'online': online}, ignore_index=True)


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
        if user_input == -1:
            save_data(customers_df)
            break
        try:
            customers_df = functions_dict[user_input](customers_df)
        except KeyError:
            print(f'The option \'{user_input}\' is not a valid choice, to exit leave input field blank.')

        loop_count += 1


main()
