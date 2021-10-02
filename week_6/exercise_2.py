# Exercise 2
# We would like to plot some data read from a CSV. The data
# will be read into a Pandas data frame. The data frame consist
# of 4 columns: 'investment' which denotes the starting amount,
# and 'year 1' through 'year 3' representing the return on investment
# from the 3 different investment options.
# Some data is missing from the CSV and like the previous exercise the
# resulting plot will have holes in it.
# (I) Can you plot each column so that we end up with 3 lines, one for
# year 1, year 2 and year 3?
# (II) Can you find a way to fill the  missing values by using the
# last valid observation?

# Extension: Note the lines do not start from the bottom left corner of
# the plot. Can you find a way to fix this?


import matplotlib.pyplot as plt
import pandas as pd


def read_file(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name)


def generate_plot(df: pd.DataFrame) -> None:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.plot(df['investment'], df['year 1'], label='year 1')
    plt.xlabel('Starting investment')
    plt.ylabel('Total return')
    plt.legend()
    fig.savefig('exercise_1.jpg', bbox_inches='tight', pad_inches=0.5)


def main() -> None:
    data = read_file('exercise_2.csv')
    generate_plot(data)


main()
