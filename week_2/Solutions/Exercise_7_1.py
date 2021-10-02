# Exercise 7
# A simple function called add_one() should to add the
# element `1` to a new list or append `1` to an existing
# list if one is passed as an argument to the function
# as return the resulting list. If we call the function
# multiple times we expect to get multiple lists of length
# 1 back as the return value but that is not the case, why?


def add_one(input_list):
    input_list.append(1)
    return input_list


# Expected output: [1]
print(add_one([]))
# Expected output: [3, 4, 1]
print(add_one([3, 4]))
# Expected output: [1]
print(add_one([]))
# Expected output: [1]
print(add_one([]))
