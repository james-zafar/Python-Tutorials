# Exercise 2
# In this exercise we will read a list of products that a shop
# sells from a CSV file. The CSV contains 3 columns "product",
# "price" and "tax". "tax" is Y or N, if Y then 20% tax should
# be added to the original price.
# The function compute_total() will select 3 products at random
# from the store and should output the total price after tax.

# Extension: Can you add a function that is optional and asks the
# user if they would like to add a product to the store?

import numpy as np
import pandas as pd


def read_products() -> pd.DataFrame:
    return pd.read_csv('../products.csv')


def select_random_product(products_df: pd.DataFrame) -> pd.Series:
    return products_df.iloc[np.random.randint(0, len(products_df))]


def compute_total(products_df: pd.DataFrame) -> None:
    total_price = 0
    for i in range(3):
        rand_product = select_random_product(products_df)
        if rand_product['tax'] == 'Y':
            total_price += float(rand_product['price'][1:]) * 1.2
        else:
            total_price += float(rand_product['price'][1:])
        print(f'Added 1 of {rand_product["product"]} to basket @ price {rand_product["price"]}. '
              f'Tax payable? {rand_product["tax"]}')

    print(f'The total cost of the order is: £{total_price}')


def add_new_item(products_df: pd.DataFrame):
    add_item = input('Would you like to add a new product to the store? ')
    if add_item.lower() == 'n' or not add_item:
        return
    product_name = input('Enter the product name: ')
    product_price = round(float(input('Enter the product price: £')), 2)
    product_price = ''.join(['£', str(product_price)])
    tax = input('Is tax payable on this product? ').upper()
    while len(tax) != 1 or (tax != 'Y' and tax != 'N'):
        print('Tax must be Y/N')
        tax = input('Is tax payable on this product? ').upper()
    final_product = {'product': product_name, 'price': product_price, 'tax': tax}
    products_df = products_df.append(final_product, ignore_index=True)
    print(products_df)
    products_df.to_csv('../products.csv', index=False)
    print('Product has been added to the store')


def main() -> None:
    df = read_products()
    compute_total(df)
    add_new_item(df)


main()
