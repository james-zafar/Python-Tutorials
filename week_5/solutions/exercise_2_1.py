# Exercise 2
# We generate some random values from a pareto distribution using
# a=2. We would like to visualise the data by plotting it on a
# scatter graph.
# (I) The code raises a ValueError when it is run, can you fix this?
# (II) Note the code currently produces a line graph instead of a
# scatter graph, make the necessary changes to produce a scatter graph
# (III) It would be useful if we could add some additional functionality
# that allows the user to choose between a line and a scatter graph and also
# specify the number of points to generate, can you make the necessary changes
# to allow this?

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
    plt.savefig('exercise_2.jpg')


main()
