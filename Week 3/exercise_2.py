# Exercise 2
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


def get_api_key() -> str:
    return input('Enter your API key (optional): ') or '195e511a55f0f4767b72'


def get_api_data(api_key: str) -> dict:
    data = requests.get(f'https://free.currconv.com/api/v7/convert?q=GBP_USD&compact=ultra&date=2021-03-15&endDate=2021-03-22&apiKey={api_key}')
    return data.text


def process_data(data: dict) -> None:
    df = pd.DataFrame(data)
    max_value = df['GBP_USD'].max()
    min_value = df['GBP_USD'].min()
    print('The worst exchange rate:\n', min_value)
    print('The best exchange rate:\n', max_value)


def main() -> None:
    api_key = get_api_key()
    data = get_api_data(api_key)
    process_data(data)


main()
