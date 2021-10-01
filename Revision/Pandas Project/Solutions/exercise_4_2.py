# Exercise 4
# Note: This file contains the solution for Tasks 1 and 2 only. If you
# managed to complete all 3 tasks, refer to exercise_4.py for the solutions.

# A detailed explanation of the solution can be found in exercise_4.py

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


def main():
    x_values = [1, 5, 10, 20, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000,
                      12500, 15000]

    numpy_values = []
    python_values = []
    for value in x_values:
        numbers = np.random.randn(value)
        _, np_time = np_sum(numbers)
        _, py_time = py_sum(numbers.tolist())
        numpy_values.append(np_time)
        python_values.append(py_time)

    plot_data(x_values, numpy_values, python_values, 'exercise_4.jpg')


main()
