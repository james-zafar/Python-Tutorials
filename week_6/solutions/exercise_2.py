# Exercise 2 - Solution


import matplotlib.pyplot as plt
import pandas as pd


def read_file(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name)


def fill_na(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(method='ffill')


def generate_plot(df: pd.DataFrame) -> None:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    for column in df.columns[1:]:
        ax.plot(df['investment'], df[column], label=column)
    plt.xlabel('Starting investment')
    plt.ylabel('Total return')
    plt.legend()
    plt.xlim(xmin=0.0)
    plt.ylim(ymin=0.0)
    fig.savefig('exercise_1.jpg', bbox_inches='tight', pad_inches=0.5)


def main() -> None:
    data = read_file('../exercise_2.csv')
    data = fill_na(data)
    generate_plot(data)


main()
