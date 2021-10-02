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
    return pd.read_csv('products.csv')


def select_random_product(products_df: pd.DataFrame) -> pd.Series:
    return products_df.iloc[np.random.randint(0, len(products_df))]


def compute_total(products_df: pd.DataFrame) -> None:
    total_price = 0
    for i in range(3):
        rand_product = select_random_product(products_df)
        total_price += rand_product['price']
        print(f'Added 1 of {rand_product["product"]} to basket @ price {rand_product["price"]}. '
              f'Tax payable? {rand_product["tax"]}')

    print(f'The total cost of the order is: £{total_price}')


def main() -> None:
    df = read_products()
    compute_total(df)


main()
