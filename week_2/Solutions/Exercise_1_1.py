# Exercise 1
# The function sort_data should sort a given list of data.
# It should return the sorted list to the caller and should
# be able to handle lists of mixed data types e.g. string, int


def sort_data(input_data: list) -> list:
    # input_data = [float(i) for i in input_data]
    for idx, element in enumerate(input_data):
        input_data[idx] = float(element)
    return sorted(input_data)


print(sort_data([1, 6, 7, 3, 9, 29]))
print(sort_data([1, '7', '9', 11, 99, '35']))
print(sort_data(['13', '17.9', 17, '9', '2', 0, '17.05']))
