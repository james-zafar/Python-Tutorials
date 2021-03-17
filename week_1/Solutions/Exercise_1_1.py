# Exercise 1
# The function remove_first_element should remove the first element in a list
# and return the resulting list. The examples below show that the wrong element
# is being removed from the list, why is this?

# Extension: Are there any other ways we can remove the first element from a list?

def remove_first_element(input_list: list) -> list:
    # Note lists are 0 indexed in python
    del input_list[0]
    # Could also use:
    # return input_list[1:]
    return input_list


# Should remove 1
print(remove_first_element([1, 2, 3, 4, 5]))
