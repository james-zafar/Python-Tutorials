# Exercise 7
# Following on from exercise 5 and 6, we will enhance our stock management
# system by adding the ability to order products that are out of stock. For
# this exercise we will use an additional csv file to help us predict sales.
# 'sales.csv' provides the sales per day of a given product over the last 14
# days.

# Task 1: Implement the predict_sales function. It should take the mean of
#   the sales for each product over the last 14 days, and return a new Series
#   object with 2 columns, the product name in the first column, and the second
#   column labelled "sales" which contains the average sales rounded upwards to
#   the closest integer (i.e. apply ceil to the column).
#   Do not worry if you can not do this - this is more complex than anything we
#   have covered so far. Feel free to look at the solution, or for some general
#   tips, think about how we have been applied loc with multiple arguments in
#   other places already, and think about how we can use the mean and apply
#   functions to achieve the desired result.

# Task 2: Implement the order_stock function. This function will be called only
#   after all orders for that day have been processed. To determine whether or not
#   to order stock, we should aim to have at least 2 days worth stock available in
#   the store. We will assume that anything ordered will arrive the next day and
#   immediately add it to our inventory. The function should do the following:
#   For each product, check if the stock_quantity is >= predicted_sales * 2 for
#   that product, if not order a sufficient quantity based on the case_size column
#   to ensure at least predicted_sales * 2 quantity is available. For example, if
#   the stock_quantity is 2, predicted_sales * 2 = 20 and case_size = 6, we should
#   order an additional 24 units as stock must be ordered in full cases.

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
        if int(product_info.stock_quantity) < quantity:
            quantity = int(product_info.stock_quantity)
        profit += (float(product_info.sell_price) - float(product_info.cost_price)) * quantity
        products.loc[products['name'] == product, 'stock_quantity'] -= quantity

    assert type(profit) == float
    return products, profit


def predict_sales(sales: pd.DataFrame) -> pd.Series:
    # TODO: Implement this function
    ...


def order_stock(products: pd.DataFrame, prediction_data: pd.Series) -> pd.DataFrame:
    # TODO: Implement this function...
    ...


def main():
    products = pd.read_csv('exercise_7.csv')
    basket = create_basket(products)
    products, total_profit = process_transaction(products, basket)
    sales = pd.read_csv('sales.csv')
    predicted_sales = predict_sales(sales)
    products = order_stock(products, predicted_sales)


main()
