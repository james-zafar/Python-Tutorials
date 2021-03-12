# Exercise 6
# A user would like to create a menu of products. Each product is
# stored as part of a dictionary where the keys are the names of
# each product and the value is the price. When the user has finished
# entering products we should sort the products based on their price such
# that the most expensive product is printed first.

# Extension: Can we print the resulting dictionary in a more human friendly way?
# For example...
# | Product | Price |
# +=========+=======+
# | Water   | 1.00  |
# +---------+-------+
# | Bread   | 0.96  |
# +=========+=======+

def sort_input(unsorted_dict: dict):
    return sorted(unsorted_dict)


def get_user_input():
    items = {}
    while True:
        name = input('Enter product name: ')
        price = float(input('Enter product price: '))
        items[name] = price
        cont = input('Enter another product? ')
        if cont.lower().startswith('n'):
            return items


products = get_user_input()
sorted_input = sort_input(products)
print(sorted_input)
