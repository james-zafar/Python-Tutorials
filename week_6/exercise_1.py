# Exercise 1
# exercise_1.csv contains two columns, one labelled 'investment'
# and another labelled 'return' which shows the amount of money
# you will get back after a 1 year investment. We would like to plot
# this using matplotlib and save the contents to a file called
# "exercise_1.jpg". The current implementation does not save the plot.
# Why?

# Extension: Can you add labels to the x and y axis, giving them
# appropriate names and also give the plot a relevant title?


import matplotlib.pyplot as plt
import pandas as pd


def read_file(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name)


def generate_plot(data: pd.DataFrame) -> None:
    plt.plot(data['investment'], data['return'])


def main() -> None:
    data = read_file('exercise_1.csv')
    generate_plot(data)


main()
