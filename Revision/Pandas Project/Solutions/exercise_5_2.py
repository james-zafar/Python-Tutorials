# Exercise 5 Solution 2
# This solution shows how Exercise 5 can be solved using the random module
# from the standard library. Refer to exercise_4.py for a more detailed
# explanation on the solution.

import pandas as pd
import random
from typing import List, Tuple


def create_basket(products: pd.DataFrame) -> List[Tuple[str, int]]:
    no_products = random.randint(1, len(products['name']))
    products_selected = []
    for i in range(no_products):
        product = random.choice(products['name'])
        quantity = random.randint(1, 5)
        products_selected.append((product, quantity))

    return products_selected


def main():
    products = pd.read_csv('exercise_5.csv')


main()
