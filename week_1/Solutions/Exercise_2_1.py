#  Exercise 2
# The function count_to_n should print the numbers 0 through n (exclusive).
# The code in this example fails to run. Why is this?

def count_to_n(number: int) -> None:
    counter = 0
    # The definition of a while loop should end with a colon
    while counter < number:
        print(counter)
        counter += 1


count_to_n(5)
