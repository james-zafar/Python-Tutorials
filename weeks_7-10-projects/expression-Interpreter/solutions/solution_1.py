# Mathematical expression interpreter
# Exercise 1

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def mul(x, y):
    return x * y


def find_parentheses(expression) -> str:
    start_idx = []
    idx = 0
    while idx < len(expression):
        if expression[idx] == '(':
            start_idx.append(idx)
            idx += 1
            continue
        elif expression[idx] == ')':
            start = start_idx.pop()
            expression = expression.replace(expression[start: idx + 1], interpreter(expression[start + 1:idx]))
            idx += 1
        else:
            idx += 1
    return expression


def find_start(expression: str, operation_idx: int) -> tuple[int, bool]:
    while operation_idx != 0:
        operation_idx -= 1
        if expression[operation_idx] in ['/', '*', '+']:
            return operation_idx + 1, False
        elif expression[operation_idx] == '-' and operation_idx != 0:
            return operation_idx, True
    return 0, False


def interpreter(expression: str) -> str:
    expression_dict = {'+': add, '-': sub, '/': div, '*': mul}
    expression = expression.replace(' ', '')
    if '(' in expression:
        expression = find_parentheses(expression)
    elif len(expression) == 2:
        return expression
    for operator in ['/', '*', '+', '-']:
        idx = 0
        while idx < len(expression):
            if expression[idx] == operator and idx != 0:
                start_idx = idx
                operation = expression_dict[expression[idx]]
                idx += 1
                if expression[idx] == '-':
                    idx += 1
                while idx < len(expression) and expression[idx] not in expression_dict:
                    idx += 1
                start, preserve = find_start(expression, start_idx)
                result = operation(float(expression[start:start_idx]), float(expression[start_idx + 1: idx]))
                if preserve:
                    expression = expression.replace(expression[start: idx], ''.join([operator, str(result)]))
                else:
                    expression = expression.replace(expression[start: idx], str(result))
                idx = start
            else:
                idx += 1
    return expression


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
            actual_result = interpreter(equation)
            assert actual_result == result
        except AssertionError:
            failed_tests += 1
            print(f'Test case Failed. Expected {equation} to evaluate to {result} but instead got {actual_result}')
    print(f'Ran {len(test_equations)} tests with a {(1 - (failed_tests / len(test_equations))) * 100: .4}% success rate')


test_interpreter()