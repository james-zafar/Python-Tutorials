# Exercise 2 - Solution

from typing import Union

import requests


class CurrencyConverter:
    def __init__(self, currency: str, base_url: str = 'https://open.er-api.com/v6/latest'):
        self.exchange_rates = None
        endpoint = f'{base_url}/{currency.upper()}'
        self.fetch_exchange_rates(endpoint)

    def fetch_exchange_rates(self, endpoint: str) -> None:
        response = requests.get(endpoint)
        if response.status_code == 400:
            raise ValueError('Error: The requested currency was not found')

        self.exchange_rates = response.json()['rates']

    def convert_to(self, currency: str, amount: Union[int, float]) -> float:
        exchange_rate = self.exchange_rates.get(currency.upper(), 0)
        return round(amount * exchange_rate, 2)


def main():
    validConverter = CurrencyConverter('USD')
    print(f'100 USD in GBP is: £{validConverter.convert_to("GBP", 100):.2f}')


main()
