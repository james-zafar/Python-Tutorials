# Exercise 2
# There are two arrays storing the marks for some students from
# a math and science test. The code below fails with a ValueError:
# ValueError: x and y must be the same size
# If the arrays are of differing length, we assume that some students
# only attends one of the two tests, and as such should not appear in
# this plot. The indices of each array correspond to the same student,
# i.e. index 0 in math_marks and index 0 in the science_marks array
# correspond to the same student, meaning if the arrays are of differing
# lengths, we can ignore the end of the larger array.
#
# (I) Can you fix the ValueError?
# (II) The code currently plots a line graph which is not ideal. Can you
#   change this to create a scatter plot, which plots green points with
#   the relevant labels for the x and y axes, as well as an appropriate title?

import matplotlib.pyplot as plt


def main():
    math_marks = [10, 92, 49, 89, 100, 80, 60, 66, 50, 44, 99]
    science_marks = [35, 79, 79, 48, 50, 88, 32, 66, 20, 77]
    plt.plot(science_marks, math_marks, color='g')
    plt.savefig('Exercise_2.jpg')


main()
