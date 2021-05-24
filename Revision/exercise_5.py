# Exercise 5
# Note the next few exercises must be completed sequentially.
# The goal of the next few exercises is to build a stock management system.
# This exercise introduces the problems and defined various functions that we
# will implement in stages. The end goal is to have a system that can predict
# sales based and process orders based on stock availability.

# In this exercise we will set up the problem by reading and exploring the dataset.

# Task 1: Read 'exercise_5.csv' into a variable in the main function and explore the
# data to get a better idea of what you will be working with.

# Task 2: Implement a function which can create a basket of random items to be ordered
# along with the quantity being ordered that follows this specification:
#   - The number of unique products ordered should be equal to no_products.
#   - The products for the order should be randomly selected from the lit of all products
#     in the original dataframe.
#   - The quantity ordered for each product should be 1 <= quantity <= 5
#   - The result should be returned as a list of tuples, for example:
#     [('Bread', 2), ('Water', 5)], where the product is a string, and the quantity is an
#     integer.
import pandas as pd
import numpy as np
from typing import List, Tuple


def create_basket(products: pd.DataFrame) -> List[Tuple[str, int]]:
    no_products = np.random.randint(1, len(products['name']))


def main():
    #TODO: Implement this
    ...


main()
