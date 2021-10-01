# Exercise 5 Solution 1
# We can read products using the read_csv function provided by Pandas.
# For the create basket function, we can use either numpy.random or Random
# from the standard library. If you have used the Random module, see
# exercise_5_2.py for the solution.
# To generate the basket, we can iterate in the range (0, no_products), and
# on each iteration use np.random.choice to select a random element of a given
# input list. In this case the input list is the column "name" from the products
# data frame. We can then select a quantity by using the np.random.randint(low, high)
# function, and append the result as a tuple to a list which we will return at the end.
import pandas as pd
import numpy as np
from typing import List, Tuple


def create_basket(products: pd.DataFrame) -> List[Tuple[str, int]]:
    no_products = np.random.randint(1, len(products['name']))
    products_selected = []
    for i in range(no_products):
        product = np.random.choice(products['name'])
        quantity = np.random.randint(1, 5)
        products_selected.append((product, quantity))

    return products_selected


def main():
    products = pd.read_csv('exercise_5.csv')


main()
