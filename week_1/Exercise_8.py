# Exercise 8
# count_multiples should print the sum of multiples of 3 and 5 in the range n.
# For example if max_n is 9, the output should be (3 + 5 + 6 + 9) = 23
# The output for the examples below is incorrect. Why is this?

def count_multiples(max_n: int) -> None:
    sum_ = 0
    for i in range(max_n):
        if i % 3 == 0:
            sum_ += i
        if i % 5 == 0:
            sum_ += i
    print(f'Sum to {max_n}: {sum_}')


# Result should be 23
count_multiples(9)
# Result should be 60
count_multiples(16)
# Result should be 119
count_multiples(21)
