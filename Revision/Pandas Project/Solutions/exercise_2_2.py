# Exercise 2 Solution 2
# If you are not comfortable with list slicing, you could also achieve
# the same results using a for loop. In this solution we use the function
# slice_array which takes as inputs, the original list and the maximum
# length of the new list. In this function we iterate over the list,
# appending each element to a new list until we reach the maximum list
# length, at which point break from the loop and return the new list.

import matplotlib.pyplot as plt


def slice_array(original: list, max_len: int) -> list:
    new_array = []
    for idx, element in enumerate(original):
        if idx == max_len:
            break
        new_array.append(element)

    return new_array


def main():
    math_marks = [10, 92, 49, 89, 100, 80, 60, 66, 50, 44, 99]
    science_marks = [35, 79, 79, 48, 50, 88, 32, 66, 20, 77]
    no_of_valid_students = min(len(math_marks), len(science_marks))
    math_marks = slice_array(math_marks, no_of_valid_students)
    science_marks = slice_array(science_marks, no_of_valid_students)

    plt.scatter(science_marks, math_marks, color='g')
    plt.title('Scatter Plot of math vs science marks')
    plt.xlabel('Science Mark')
    plt.ylabel('Math Mark')
    plt.savefig('Exercise_2.jpg')


main()
