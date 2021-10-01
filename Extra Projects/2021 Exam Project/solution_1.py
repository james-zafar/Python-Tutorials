import pandas as pd
import matplotlib.pyplot as plt


DAYS = {
    1.0: "Monday",
    2.0: "Tuesday",
    3.0: "Wednesday",
    4.0: "Thursday",
    5.0: "Friday",
    6.0: "Saturday",
    7.0: "Sunday",
}


def get_average_spend(data: pd.DataFrame) -> None:
    avg_spend = data['total_spend'].mean()
    print(f'Average spend is: £{avg_spend:.2f}')


def average_spend_by_day(data: pd.DataFrame) -> None:
    group_by_day = data.groupby(['week_day'])
    averages_by_day = group_by_day['total_spend'].mean().to_frame()
    averages_by_day.reset_index(inplace=True)
    averages_by_day.plot(x='week_day', y='total_spend')
    plt.xlabel('Day of the week')
    plt.ylabel('Average spend (GBP)')
    plt.savefig('Exercise_2.jpg', bbox_inches='tight', pad_inches=0.5)

    highest_avg_spend = averages_by_day.iloc[averages_by_day['total_spend'].argmax()]
    print(f'Highest average spend was £{highest_avg_spend["total_spend"]:.2f}, which was on'
          f' {DAYS.get(highest_avg_spend["week_day"])}')

    lowest_avg_spend = averages_by_day.iloc[averages_by_day['total_spend'].argmin()]
    print(f'Lowest average spend was £{lowest_avg_spend["total_spend"]:.2f}, which was on'
          f' {DAYS.get(lowest_avg_spend["week_day"])}')


def air_temp_correlation(data: pd.DataFrame) -> None:
    correlation = data['total_spend'].corr(data['air_temperature'])
    if correlation < 0:
        print('There is a negative correlation between total spend and air temperature')
    elif correlation == 0:
        print('There is no correlation between total spend and air temperature')
    else:
        print('There is some positive correlation between total spend and air temperature')

    data.plot(kind='scatter', x='air_temperature', y='total_spend')
    plt.xlabel('Air temperature')
    plt.ylabel('Total spend (GBP)')
    plt.title('Plot showing the correlation between air temperature and total spend')
    plt.savefig('Exercise_3.jpg', bbox_inches='tight', pad_inches=0.5)


def main() -> None:
    shopping_data = pd.read_csv('ShoppingData.csv')
    get_average_spend(shopping_data)
    average_spend_by_day(shopping_data)
    air_temp_correlation(shopping_data)


main()
