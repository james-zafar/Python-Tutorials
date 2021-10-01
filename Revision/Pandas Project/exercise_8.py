# Exercise 8
# We now have a fully functional stock management system...
# Let's now add some user interaction to make it more useful.

# Task 1: Add functionality to the main function that can call the correct
#   function based on the user input. 0 should call run_store, 1 should call
#   update_price, 2 should call add_product, 3 should call exit_store. Note if
#   the user enters "3" we should break out of the while loop after calling the
#   exit_store function.

# Task 2: Many of the new functions users can interact with have no
#   implementation yet. Implement the update_price, add_product, and exit_store
#   functions using the specification provided in each function.

from typing import List, Tuple

import numpy as np
import pandas as pd


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


def run_store(products: pd.DataFrame, sales_data: pd.Series) -> pd.DataFrame:
    total_profit = 0
    for i in range(5):
        basket = create_basket(products)
        products, profit = process_transaction(products, basket)
        total_profit += profit
        products = order_stock(products, sales_data)

    print(f'The total profit for the period is: £{total_profit:.2f}')

    return products


def update_price(products: pd.DataFrame) -> pd.DataFrame:
    # The user should be asked for a product name for which they would like to
    # update the price. After verifying that the product exists, the user should
    # be asked for a price (the input must be a valid float). You should then
    # update the products dataframe with the new price for the products specified.
    return products


def add_product(products: pd.DataFrame) -> pd.DataFrame:
    # The user should be asked for:
    #   - Produce name
    #   - Cost price
    #   - Sell price
    #   - Case size
    # Shelf life should be a randomly generated integer in the range 0 <= life <= 30
    # stock quantity should be a randomly generated integer in the range 0 <= qty <= 99
    # The new product should be added to "products".
    return products


def exit_store(products: pd.DataFrame, sales_data: pd.Series) -> None:
    # The contents of products and sales_data may have changed whilst the
    # user was interacting with your system. You should save the contents of
    # both dataframes to a CSV file. Products should be written to
    # 'exercise_7.csv' and sales_data should be written to 'sales.csv'
    # This function should not return anything.
    ...


def main() -> None:
    products = pd.read_csv('exercise_7.csv')
    sales = pd.read_csv('sales.csv')
    predicted_sales = predict_sales(sales)
    print('Welcome to the stock management system.')
    # while True:
    #     print('0 - Run the store for 5 days, \n1 - Update the price of a product\n',
    #           '2 - Add a new product\n 3 - Save the current state and exit')
    #     user_input = int(input('Choose an operation'))
    #     # TODO: Uncomment the above and call a function based on user input


main()
