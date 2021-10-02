# Exercise 3
# Sum of triangular numbers.
# Triangular Number": any of the series of numbers (1, 3, 6, 10, 15, etc.)
# obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."
# [01]
# 02 [03]
# 04 05 [06]
# 07 08 09 [10]
# 11 12 13 14 [15]
# 16 17 18 19 20 [21]
# If 4 was given as an input, 20 should be returned. i.e. 1 + 3 + 6 + 10 = 20
# If a negative number is given as input, return 0.

# Task: Implement the compute_triangular_sum function as per the instructions
# above such that all test cases pass.
# HINT: Think about how we can derive a formula for computing the triangular number
# at level n


def compute_triangular_sum(level: int) -> int:
    return -1


def test_compute_triangular_sum() -> None:
    test_cases = {1: 1, 2: 4, -140: 0, 5: 35, 10: 220, 26: 3276, 50: 22100, 555: 28646510, 1000: 167167000, -1: 0}
    failed_tests = 0
    for input_, result in test_cases.items():
        try:
            actual_answer = compute_triangular_sum(input_)
            assert actual_answer == result
        except AssertionError:
            failed_tests += 1
            print(f'Test case Failed. Expected sum to level {input_} to be {result}, but got {actual_answer}')

    print(f'Ran {len(test_cases)} tests with a {(1 - (failed_tests / len(test_cases))) * 100: .4}% success rate')


test_compute_triangular_sum()
