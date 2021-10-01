# Exercise 3 - Solution

import matplotlib.pyplot as plt
import numpy as np


def gen_random_data(n_points) -> tuple[np.array, np.array]:
    x = np.linspace(-10, 10, n_points)
    y = np.random.pareto(2, size=n_points)
    return x, y


def main() -> None:
    n_points = int(input('How many points would you like to generate? ')) or 250
    graph_type = input('Would you like to produce a line or scatter graph? ') or 'scatter'
    x, y = gen_random_data(n_points)
    if graph_type == 'line':
        plt.plot(x, y, 'purple')
    else:
        plt.scatter(x, y, color='g')
    plt.title('Random scatter plot')
    plt.savefig('exercise_3.jpg')


main()
