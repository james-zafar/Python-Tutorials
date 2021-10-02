# Exercise 4
# We would like to plot some data on the stock price of Apple,
# Microsoft, and Facebook. The array "times" represents the
# time at which the stock was at the corresponding price in
# each of the stock arrays.
# (I) Can you add x markers to each data point in the plot and
# also add a legend using the stock names, i.e. APPL should be
# used to correspond to the line for the Apple stock.

# (II) Uncomment line 48 (the last line of the main function).
# If you have done part I correctly you should see 3 lines some
# with missing points. The function "fill_missing_points()" should
# locate any missing values in the input array and fill them by taking
# the average of the 4 closest points (2 either side of the missing
# value) and return the resulting array.

import matplotlib.pyplot as plt
import numpy as np

appl_price = [121.74, 122.12, 122.38, 121.85, 121.92, 121.51, 121.25, 121.24, 121.31,
              120.92, 121.23, 121.24, 121.30]
msft_price = np.array([236.68, 235.36, 235.39, np.NAN, 234.45, 233.93, 232.97,
                       232.46, np.NAN, 232.14, 232.52, 232.63, 232.28])
fb_price = np.array([285.94, 287.48, np.NAN, 287.45, 288.88, np.NAN, 286.58,
                     286.40, 286.36, 287.76, np.NAN, 286.88, 286.53])
times = ['09:30', '09:35', '09:40', '09:45', '09:50', '09:55', '10:00', '10:05',
         '10:10', '10:15', '10:20', '10:25', '10:30']


def fill_missing_points(data: np.array) -> np.array:
    return data


def make_plot(time_list: list, **kwargs) -> None:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    for stock_name, stock_price in kwargs.items():
        stock_price = fill_missing_points(stock_price)
        ax.plot(time_list, stock_price)
    plt.xlabel('Time (03/29/21)')
    plt.ylabel('Stock price')
    fig.savefig('exercise_4.jpg', bbox_inches='tight', pad_inches=0.5)


def main():
    make_plot(times, APPL=appl_price)
    # For part II of the exercise, uncomment the line below line
    # make_plot(times, APPL=appl_price, FB=fb_price, MSFT=msft_price)


main()
