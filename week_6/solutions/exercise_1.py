# Exercise 1 - Solution


import matplotlib.pyplot as plt
import pandas as pd


def read_file(file_name) -> pd.DataFrame:
    return pd.read_csv(file_name)


def generate_plot(data: pd.DataFrame) -> None:
    plt.plot(data['investment'], data['return'])
    plt.title('Return on investment calculator')
    plt.xlabel('Value of investment')
    plt.ylabel('Return on investment')
    plt.savefig('exercise_1.jpg')


def main():
    data = read_file('../exercise_1.csv')
    generate_plot(data)


main()
