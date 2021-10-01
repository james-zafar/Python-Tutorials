# Exercise 4
# In this exercise we will compare np.sum() and sum to see which is quicker
# in terms of computation time. The functions to compute the sum of a list
# of numbers is defined for you, these functions have  two return values.
# The first is the sum of the input list, the second is the execution time
# in ms. The second return value comes from the @timer decorator - you do
# not need to worry about how this is implemented, but if you are interested
# checkout the timer.py file.

# The plot_data() function should generate the plots given some data and save
# a plot, with the relevant labels (x, y axis, title, legend, etc.) to a file.
# main() currently contains a list of input numbers and a for loop that iterates
# in the range 0 through 49. This for loop is incorrect and will need fixing.

# Task 1: Fix the for loop in main() so that it iterates over x_values_small(),
# generates N numbers from a normal distribution in a list, where N is the number
# at index i of x_values_small, and appends the times to a list to be plotted later.

# Task 2: Implement the plot_data function, plotting both the Python and NumPy times,
# with the relevant labels (see above) and save the plot to the file with the specified
# name. Also add a call to this function from main.

# Task 3: Can you generalise this implementation to work on more than one dataset? For
# example, say I want to visualise the difference in computation time on larger datasets?
# Change your implementation to generate multiple plots for different datasets, without
# adding additional for loops. Use the list below as a secondary input and test that your
# code can generate two visualisations, saving them both with different file names.
# x_values_large = [25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 250000,
#                   300000, 350000, 400000, 450000, 500000]

# NOTE: timer.py MUST be in the same directory as this file when you run it.

from timer import timer
import numpy as np


@timer
def np_sum(numbers: np.array) -> float:
    return np.sum(numbers)


@timer
def py_sum(numbers: list[int]) -> int:
    return sum(numbers)


def plot_data(x: list[int], np_y: list[float], py_y: list[float], file_name: str) -> None:
    ...


def main():
    x_values = [1, 5, 10, 20, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000,
                      12500, 15000]
    for i in range(50):
        _, np_time = np_sum([1])
        _, py_time = py_sum([1])


main()
