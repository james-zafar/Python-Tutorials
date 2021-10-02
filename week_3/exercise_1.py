import numpy as np

# Exercise 1
# Implement each of the functions below, following the specification provided in each function.
# You can ensure your solution is correct by running the file and verifying that all of the
# test cases pass


def get_all_even_numbers(arr: np.array) -> np.array:
    # Return a NumPy array containing all of the even numbers from the input array
    pass


def replace_all_multiples_of_4(arr: np.array) -> np.array:
    # Replace all multiples of 4 in the input array with -1 and return the resulting array
    pass


def get_with_constraints(arr: np.array, lower_bound: int, upper_bound: int) -> np.array:
    # Return a NumPy array containing all of the numbers in the original array that are
    # greater than or equal to the lower bound and less than or equal to the upper bound
    pass


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
