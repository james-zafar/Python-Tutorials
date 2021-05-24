# Exercise 6
# Following on from exercise 5, in this exercise we will make use of
# the create_basket to update the stock system and compute profit.

# Task 1: Add a call that calls process_transaction with a basket created
#   by create_basket and can stores the return value in a variable called
#   total_profit and re-assigned products to use the updated DataFrame.

# Task 2: The process_transaction functions fails the assertion check, meaning
#   the profit variable is not a float. Can you fix this?

# Task 3: The profit appears to be incorrect for most orders, can you spot why
#   this is?

# Task 4: Implement a check to ensure the quantity of a given product can not be
#   below 0. If the quantity ordered would take the stock_quantity below 0, change
#   the quantity ordered to be equal to stock_quantity.

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


def process_transaction(products: pd.DataFrame, basket: List[Tuple[str, int]]) -> Tuple[pd.DataFrame, float]:
    profit = 0.
    for product, quantity in basket:
        product_info = products[products.name == product]
        profit = (float(product_info.sell_price) - float(product_info.cost_price)) * quantity
        products.loc[products['name'] == product, 'stock_quantity'] -= quantity

    assert type(profit) == float
    return products, profit


def main():
    products = pd.read_csv('exercise_5.csv')
    basket = create_basket(products)
    products, total_profit = process_transaction(products, basket)



main()
