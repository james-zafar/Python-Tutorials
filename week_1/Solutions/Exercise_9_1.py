# Exercise 9
#  The function multiply_by_two should multiply all of the elements in
# input_list by 2 and print the resulting list. Currently the function is
# stuck in an infinite loop, why is this?

def multiply_by_two(input_list: list):
    # Initialise multiple_list to be a new empty list
    # In the original problem multiple_list was a pointer to input_list meaning
    # whenever we appended a new value to multiple_list we are also changing
    # the value of input_list
    multiple_list = []
    for i in input_list:
        multiple_list.append(i * 2)

    print(multiple_list)


multiply_by_two([1, 2, 3, 4, 5])
