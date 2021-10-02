import numpy as np

# Exercise 1 - Solution


def get_all_even_numbers(arr: np.array) -> np.array:
    return arr[arr % 2 == 0]


def replace_all_multiples_of_4(arr: np.array) -> np.array:
    arr[arr % 4 == 0] = -1
    return arr


def get_with_constraints(arr: np.array, lower_bound: int, upper_bound: int) -> np.array:
    # Solution 1:
    # return np.where((arr >= lower_bound) & (arr <= upper_bound))[0]
    # Solution 2:
    # return np.where(np.logical_and(arr >= lower_bound, arr <= upper_bound))[0]
    # Solution 3:
    return arr[(arr >= lower_bound) & (arr <= upper_bound)]


def run_tests():
    # Test get_all_even_numbers
    test_array = np.arange(20)
    result = get_all_even_numbers(test_array)
    expected = np.arange(0, 20, 2)
    assert np.array_equal(result, expected), f'Error: get_all_even_numbers should have returned {expected}, ' \
                                             f'but instead returned {result} when given an input of {test_array}'

    # test replace_all_multiples_of_4
    expected = np.array([-1, 1, 2, 3, -1, 5, 6, 7, -1, 9, 10, 11, -1, 13, 14, 15, -1, 17, 18, 19])
    result = replace_all_multiples_of_4(test_array)
    assert np.array_equal(result, expected), f'Error: Expected replace_all_multiples_of_4 to return {expected} ' \
                                             f'for input {test_array}, but instead got {result}'

    # test get_with_constraints
    test_array = np.arange(20)
    result = get_with_constraints(test_array, 5, 11)
    expected = np.arange(5, 12)
    assert np.array_equal(result, expected), f'Error: Expected get_with_constraints to return {expected} for input {test_array},' \
                                             f'but instead got {result}'


run_tests()
