# Exercise 8
# ADD A SOLUTION DESCRIPTION HERE...

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

    print(f'\nThe total profit for the period is: £{total_profit:.2f}\n')

    return products


def update_price(products: pd.DataFrame) -> pd.DataFrame:
    product = input('Which product would you like to update? ')
    if not products['name'].isin([product]).any():
        print(f'Product {product} is not a known product name.')
        return products

    new_price = round(float(input('Enter the new price for this product: £')), 2)
    products.loc[products['name'] == product, 'sell_price'] = new_price

    return products


def add_product(products: pd.DataFrame) -> pd.DataFrame:
    name = input('Enter the product name: ')
    cost = round(float(input('Enter the cost price: £')), 2)
    sell = round(float(input('Enter the sell price: £')), 2)
    case_size = input('Enter the case size: ')
    shelf_life = np.random.randint(0, 30)
    quantity = np.random.randint(0, 99)
    product_dict = {'name': name, 'cost_price': cost, 'sell_price': sell, 'case_size': case_size,
                    'stock_quantity': quantity, 'shelf_life': shelf_life}
    products = products.append(product_dict, ignore_index=True)

    return products.reset_index()


def exit_store(products: pd.DataFrame, sales_data: pd.Series) -> None:
    products.to_csv('exercise_7.csv')
    sales_data.to_csv('sales.csv')


def main() -> None:
    products = pd.read_csv('exercise_7.csv')
    sales = pd.read_csv('sales.csv')
    predicted_sales = predict_sales(sales)
    print('Welcome to the stock management system.')
    while True:
        print('0 - Run the store for 5 days, \n1 - Update the price of a product',
              '\n2 - Add a new product\n3 - Save the current state and exit')
        user_input = int(input('Choose an operation: '))
        if user_input == 0:
            products = run_store(products, predicted_sales)
        elif user_input == 1:
            products = update_price(products)
        elif user_input == 2:
            products = add_product(products)
        elif user_input == 3:
            exit_store(products, predicted_sales)
            break
        else:
            print(f'The option \'{user_input}\' does not correspond to any supported operation.')


main()
