# Mathematical expression interpreter
# Solution 2

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
            start_idx.append(idx + 1)
            idx += 1
            continue
        elif expression[idx] == ')':
            start = start_idx.pop()
            expression = expression.replace(expression[start - 1: idx + 1], interpreter(expression[start:idx]))
            idx = 0
            continue
        idx += 1
    return expression


def calculate_result(eqs: dict, mappings: dict, expression_mappings: dict) -> str:
    # Add an arbitrary key to map used values to
    mappings[float("inf")] = None
    math_operators = ['/', '*', '+', '-']
    for operation in math_operators:
        # We want to start with the last instance of the operator
        to_evaluate = sorted(eqs[operation], key=lambda x: x[1], reverse=True)
        for eq in to_evaluate:
            start, operator, end, keep_sign = eq[0], eq[1], eq[2], False
            x = ''.join([mappings[idx] for idx in range(start, operator) if mappings[idx] is not None])
            y = ''.join([mappings[idx] for idx in range(operator + 1, end + 1) if mappings[idx] is not None])
            # If there is a minus sign before the first number, include it
            if start > 0 and mappings[start - 1] == '-':
                x = ''.join([mappings[start - 1], x])
                start -= 1
                # Record that we may need to insert an operation later
                keep_sign = True
            # If the 'end' has already been mapped to a new value, we need to find where it is
            if y[-1:] in math_operators or mappings[end] is None:
                for idx in range(operator + len(y), len(mappings)):
                    if mappings[idx] is not None:
                        y = ''.join([y, mappings[idx]])
                        if mappings[idx] not in math_operators:
                            end = idx
                            break
            if mappings[operator] is None:
                operation = y[0]
                y = y[1:]
            res = expression_mappings[operation](float(x), float(y))
            # If we have noted we need to include an operation and the value is >0, insert one
            if keep_sign and res > 0.0:
                mappings[end] = ''.join(['+', str(res)])
            else:
                mappings[end] = str(res)
            # Add result to the end of the equation and map all other values to None
            for idx in range(start, end):
                mappings[idx] = mappings[float("inf")]
    final_answer = [ans for ans in mappings.values() if ans is not None]
    # This should never be true
    if len(final_answer) != 1:
        raise ArithmeticError('Error, too many non-null values to unpack in final answer')

    return final_answer[0]


def interpreter(expression: str) -> str:
    expression_dict = {'+': add, '-': sub, '/': div, '*': mul}
    expression = expression.replace(' ', '')
    if '(' in expression:
        expression = find_parentheses(expression)
    elif len(expression) == 2:
        return expression
    idx = 0
    equations = {'*': [], '-': [], '+': [], '/': []}
    expression_mappings = {idx: char for idx, char in enumerate(expression)}
    while idx < len(expression) - 1:
        eq_start = idx
        idx += 1
        while idx < len(expression) - 1 and expression[idx] not in expression_dict:
            idx += 1
        operator = idx
        operator_type = expression[idx]
        idx += 1
        if expression[idx] == '-':
            idx += 1
        while idx < len(expression) and expression[idx] not in expression_dict:
            idx += 1
        eq_end = idx - 1
        equations[operator_type].append((eq_start, operator, eq_end))
        if idx == len(expression):
            break
        idx = operator + 1
    res = calculate_result(equations, expression_mappings, expression_dict)
    return res


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