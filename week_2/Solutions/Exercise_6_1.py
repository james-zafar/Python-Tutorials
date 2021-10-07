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


def sort_input(unsorted_dict: dict[str, float]) -> list[str]:
    return sorted(unsorted_dict, key=unsorted_dict.get, reverse=True)


def print_sorted_input(unsorted_dict: dict[str, float]) -> None:
    sorted_products = sort_input(unsorted_dict)
    for product in sorted_products:
        print('Name:', product, 'Price:', unsorted_dict[product])


def get_user_input() -> dict[str, float]:
    items = {}
    while True:
        name = input('Enter product name: ')
        price = float(input('Enter product price: '))
        items[name] = price
        cont = input('Enter another product? ')
        if cont.lower().startswith('n'):
            return items


products = get_user_input()
print_sorted_input(products)
