# Exercise 7 Solution 1
# To implement Task 1 we have made use of the loc function.
# sales.loc[:, sales.columns != 'name'].mean(axis=1).apply(np.ceil)
# Here we are applying loc to the sales DataFrame, selecting everything to
# start with by specifying :, then selecting every column other than the 'name'
# column, then computing the row wise mean (axis=1) - remember the NumPy tutorial
# where we discussed the meaning of axis. And then using the apply function to
# apply the ceil function to every value.
# We then concatenate the name column we initially remove, the new means, and again
# concatenate the rows, and also specify a keys arguments that sets the column titles.

# Task 2
# For task 2 we iterate over the rows (iterrows), and for each row compare the available
# stock to the prediction sales from the prediction_data dataframe. If we need to order
# additional stock we compute the quantity to order as per the specification provided.

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
    means = sales.loc[:, sales.columns != 'name'].mean(axis=1).apply(np.ceil)
    return pd.concat([sales['name'], means], axis=1, keys=['name', 'sales'])


def order_stock(products: pd.DataFrame, prediction_data: pd.Series) -> pd.DataFrame:
    for _, row in products.iterrows():
        available_quantity = int(row.stock_quantity)
        required_quantity = int(prediction_data.loc[prediction_data['name'] == row['name'], 'sales'])
        if available_quantity < (required_quantity * 2):
            case_size = int(row.case_size)
            order_quantity = np.ceil(((required_quantity * 2) - available_quantity) / case_size) * case_size
            products.loc[products['name'] == row['name'], 'stock_quantity'] += int(order_quantity)

    return products


def main():
    products = pd.read_csv('exercise_7.csv')
    basket = create_basket(products)
    products, total_profit = process_transaction(products, basket)
    sales = pd.read_csv('sales.csv')
    predicted_sales = predict_sales(sales)
    products = order_stock(products, predicted_sales)


main()
