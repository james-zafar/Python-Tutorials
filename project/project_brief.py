# Mathematical expression interpreter
# This exercise will require you to write code that passes
# a series of test cases. Given some mathematical expression
# as a string we would like to evaluate it and return the
# answer as a float. Below is specification of what your
# solution should be able to do:
#   - It must be able to interpret + - * / correctly.
#   - It must be able evaluate parentheses correctly
#       - i.e. (10 * 2) + 4 should evaluate to 24.
#   - Operations should always be evaluated left to right and follow
#      mathematical conventions, i.e. parentheses evaluated first,
#      then /, then *, then +, and finally -
#   - You can assume the input will always be a valid expression.
#   - You must account for whitespace in the input expression, both
#      '1 + 1' and '1+ 1' are valid expression.
#   - You do not need to support any other operators, such as
#      modulo, integer division etc.
#   - Your solution should pass ALL test cases.
#   - Your final result should be returned by the interpreter
#      function but you are free to implement as many other functions
#      as you see fit.
#   - You do not need to implement any form of rounding on final answers.
#   - Your solution must use features from the standard library only.
#   - Do not edit the test_interpreter function.

# Extension: Can you enhance your solution to allow for negative numbers
# in the input? Note: You do not need to account for multiple negation
# of numbers e.g '3 + -4' should return -1.0 but '3 + -(-4)' is not valid.

def interpreter(expression: str) -> str:
    # TODO: Add your implementation here
    pass


def test_interpreter():
    test_equations = {'1 + 1': '2.0', '1 - 1': '0.0', '1 * 4': '4.0',
                      '4 / 2': '2.0', '(4 * 6)/ 3': '8.0', '((4*9) / 3) * 2': '24.0',
                      '(11 * 0) / 10': '0.0', '1.25 * 2': '2.5', '11 / 4': '2.75',
                      '(10 * 100) / 2': '500.0', '6 - (4)': '2.0',
                      '15 /3*5+10': '35.0', '10/10 * 100 - 20 + 6': '86.0',
                      '10*0.5': '5.0', '0.5 * 6 - (3 / 2) + 10 * 2': '21.5'}
    # For the extension add the following to the end of the dictionary above:
    # '6 + -(4)': '2.0', '(10 * 10) * -1': '-100.0'
    failed_tests = 0
    for equation, result in test_equations.items():
        actual_result = None
        try:
            actual_result = interpreter(equation)
            assert actual_result == result
        except AssertionError:
            failed_tests += 1
            print(f'Test case Failed. Expected {equation} to evaluate to {result} but instead got {actual_result}')
    print(f'Ran {len(test_equations)} tests with a {(1 - (failed_tests / len(test_equations))) * 100: .4}% success rate')


test_interpreter()
