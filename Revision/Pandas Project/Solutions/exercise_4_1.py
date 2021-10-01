# Exercise 4
# Note: This file contains the solution for Tasks 1, 2 and 3. If you did
# not manage to complete Task 3, refer to exercise_4_2.py for solutions to
# tasks 1 and 2.

# We have a new function compute_times, which takes a set of x_values for
# which we will compute data for and compare the NumPy and Python sum functions
# for computing the sums with that number of elements. This function uses
# the same for loop seen in the original exercise, but returns the results
# to the caller instead of calling plot_data directly. This is because the
# compute_times function is self contained; it need not know anything about
# the data it is using, it can complete its task of recording the computation
# times and return those to the caller. Having small chunks of code with a
# specific purpose is generally considered good practise.
# We have implemented plot_data to create a line plot of the NumPy and Python
# times. The brief did not specify what type of plot to produce, any plot that
# is sensible is acceptable here. We add an x label, y label, title and legend
# as per the brief and save the image to a file.
# The main function has been changed slightly to call compute_times with each
# of the two lists provided in the brief, and call plot_data with each set of
# results to produce two plots.

from timer import timer
import numpy as np
import matplotlib.pyplot as plt


@timer
def np_sum(numbers: np.array) -> float:
    return np.sum(numbers)


@timer
def py_sum(numbers: list[int]) -> int:
    return sum(numbers)


def plot_data(x: list[int], np_y: list[float], py_y: list[float], file_name: str) -> None:
    plt.figure()
    plt.plot(x, np_y, label='NumPy Times', color='g')
    plt.plot(x, py_y, label='Python Times', color='r')
    plt.xlabel('Number of input elements')
    plt.ylabel('Execution time (ms)')
    plt.title('Comparison of the execution time of np.sum() and sum()')
    plt.legend()
    plt.savefig(file_name)


def compute_times(x_values: list) -> tuple[list[float], list[float]]:
    numpy_values = []
    python_values = []
    for value in x_values:
        numbers = np.random.randn(value)
        _, np_time = np_sum(numbers)
        _, py_time = py_sum(numbers.tolist())
        numpy_values.append(np_time)
        python_values.append(py_time)

    return numpy_values, python_values


def main():
    x_values = [1, 5, 10, 20, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000,
                      12500, 15000]
    x_values_large = [25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 250000, 300000, 350000, 400000,
                      450000, 500000]

    numpy_values, python_values = compute_times(x_values)
    plot_data(x_values, numpy_values, python_values, 'exercise_4_small.jpg')

    numpy_values, python_values = compute_times(x_values_large)
    plot_data(x_values_large, numpy_values, python_values, 'exercise_4_large.jpg')


main()
