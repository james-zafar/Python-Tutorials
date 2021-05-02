# Mathematical expression interpreter
# Solution 3

import re
from typing import Callable, Union
from warnings import warn


def do_arithmetic(x: str, y: str, func: Callable):
    """
    Since we work on strings from the input/regex, this function makes it easier to call any operator function by doing
        the type casting for us. This allows for cleaner code.
    """
    return str(func(float(x), float(y)))


def add(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    return x + y


def sub(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    return x - y


def div(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    return x / y


def mul(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    return x * y


def calc_parentheses(expr: str) -> str:
    start_idx = []
    idx = 0
    while idx < len(expr):
        if expr[idx] == '(':
            start_idx.append(idx)
            idx += 1
            continue
        elif expr[idx] == ')':
            start = start_idx.pop()
            expr = expr.replace(expr[start: idx + 1], eval_expr(expr[start + 1:idx]))
            idx += 1
        else:
            idx += 1
    return expr


def eval_expr(expr: str) -> str:
    expr_func_mapping = {
        '+': add,
        '-': sub,
        '/': div,
        '*': mul
    }

    calculated_expr = expr.replace(' ', '')
    # This is not necessary, but prevents unnecessary repeated function calls.
    if '(' in expr:
        calculated_expr = calc_parentheses(calculated_expr)

    # These are not very clean since they try to recognise decimal numbers. Otherwise it would be simple...
    # The verbose version is provided for the first regex, the others follow an identical pattern.
    # We split into 4 separate regex expressions so we can check for operations one at a time and in the correct order.
    # Groups are returned in the following form:
    '''
    r = re.search(div_pat, '3.4/-4.5')
    r.groups()
    ('3.4', '.4', '/', '-4.5', '.5')    '''
    div_pat = re.compile(r'''
    (^-?\d+(\.\d+)?\w?)  # Number/decimal on left side of operator. Returns two groups. Int part and decimal part.
    (/)  # Operator
    (-?\d+(\.\d+)?\w?)  # Number/decimal on right side of operator. Returns two groups. Int part and decimal part.
    ''', re.VERBOSE)

    mul_pat = re.compile(r'(-?\d+(\.\d+)?\w?)(\*)(-?\d+(\.\d+)?)')
    add_pat = re.compile(r'(-?\d+(\.\d+)?\w?)(\+)(-?\d+(\.\d+)?\w?)')
    sub_pat = re.compile(r'(-?\d+(\.\d+)?\w?)(-)(-?\d+(\.\d+)?\w?)')

    operator_pats = [div_pat, mul_pat, add_pat, sub_pat]

    # Account for order of operations
    for pat in operator_pats:
        if len(calculated_expr) <= 2:
            break
        finished = False
        while not finished:
            try:
                pattern_search = re.search(pat, calculated_expr)
                x, _, op, y, _ = pattern_search.groups()
                result = do_arithmetic(x, y, expr_func_mapping[op])
                if pattern_search.start() > 0 and x[0] == '-' and float(result) > 0:
                    result = ''.join(['+', result])

                calculated_expr = calculated_expr.replace(''.join([x, op, y]), result)
            # No matches on regex so current operation is not in expression. Move on.
            except AttributeError:
                finished = True
    return calculated_expr


def test_interpreter():
    test_equations = {'1 + 1': '2.0', '1 - 1': '0.0', '1 * 4': '4.0',
                      '4 / 2': '2.0', '(4 * 6)/ 3': '8.0', '((4*9) / 3) * 2': '24.0',
                      '(11 * 0) / 10': '0.0', '1.25 * 2': '2.5', '11 / 4': '2.75',
                      '(10 * 100) / 2': '500.0', '6 - (4)': '2.0',
                      '15 /3*5+10': '35.0', '10/10 * 100 - 20 + 6': '86.0',
                      '10*0.5': '5.0', '0.5 * 6 - (3 / 2) + 10 * 2': '21.5',
                      '6 + -(4)': '2.0', '(10 * 10) * -1': '-100.0', '-10-10': '-20.0'}
    failed_tests = 0
    for equation, result in test_equations.items():
        actual_result = None
        try:
            actual_result = eval_expr(equation)
            if not isinstance(actual_result, str):
                actual_result = str(actual_result)
                warn(f'The final result should be returned as a string, not {type(actual_result).__name__}!',
                     UserWarning, stacklevel=2)
            assert actual_result == result
        except AssertionError:
            failed_tests += 1
            print(f'Test case Failed. Expected {equation} to evaluate to {result} but instead got {actual_result}')
    print(f'Ran {len(test_equations)} tests with a {(1 - (failed_tests / len(test_equations))) * 100: .4}% success rate')


test_interpreter()