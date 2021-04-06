# Exercise 1
# We would like to find the days on which the exchange rate from GBP to
# USD was best and worst for a given time period. The user should provide
# an API key so that we can fetch the data from the API and then process it.
# We will put the resulting data in a Pandas DataFrame. The output should be
# the row of the data frame representing the date so should display the date,
# column title and exchange rate.

# Extension: Could we enhance this to allow the user to input what currencies
# they would like to compare?

# Further extension: Can you add some code to handle unexpected responses from
# the API to prevent data processing errors later on?

# NB: If you do not have an API key you may skip the stage where asked for user
# input (press enter leaving the input blank) and one will be provided for you.


import pandas as pd
import requests


def get_api_key():
    return input('Enter your API key (optional): ') or '195e511a55f0f4767b72'


def get_currencies():
    from_currency = input('Enter the currency to convert from (optional): ').upper() or 'GBP'
    to_currency = input('Enter the currency to convert to (optional): ').upper() or 'USD'
    return f'{from_currency}_{to_currency}'


def get_api_data(api_key, currency):
    data = requests.get(f'https://free.currconv.com/api/v7/convert?q={currency}&compact=ultra&date=2021-03-15&endDate=2021-03-22&apiKey={api_key}')
    if data.status_code != 200:
        raise TypeError(
            f'Failed to retrieve data from the server. Server responded with {data.status_code}, {data.reason}')
    return data.json()


def process_data(data, currency):
    df = pd.DataFrame(data)
    max_value = df[currency].max()
    min_value = df[currency].min()
    print('The worst exchange rate:\n', df.loc[df[currency] == min_value])
    print('The best exchange rate:\n', df.loc[df[currency] == max_value])


def main():
    api_key = get_api_key()
    currency = get_currencies()
    data = get_api_data(api_key, currency)
    process_data(data, currency)


main()
