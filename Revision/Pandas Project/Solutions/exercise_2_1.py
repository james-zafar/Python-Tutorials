# Exercise 2 Solution 1
# We can compute the maximum number of students that took both tests by
# taking the min of the length of both lists. We can then use list slicing
# to remove any additional elements to ensure the arrays are of the same
# length before we plot them. In the solution below we only slice the array
# only if the length exceeds no_of_valid_students. This is to prevent
# pointless slicing. It is also acceptable to replace lines 19 and 20 with
# math_marks = math_marks[:no_of_valid_students]
# science_marks = science_marks[:no_of_valid_students]


import matplotlib.pyplot as plt


def main():
    math_marks = [10, 92, 49, 89, 100, 80, 60, 66, 50, 44, 99]
    science_marks = [35, 79, 79, 48, 50, 88, 32, 66, 20, 77]
    no_of_valid_students = min(len(math_marks), len(science_marks))
    math_marks = math_marks if len(math_marks) <= no_of_valid_students else math_marks[:no_of_valid_students]
    science_marks = science_marks if len(science_marks) <= no_of_valid_students else science_marks[:no_of_valid_students]
    plt.scatter(science_marks, math_marks, color='g')
    plt.title('Scatter Plot of math vs science marks')
    plt.xlabel('Science Mark')
    plt.ylabel('Math Mark')
    plt.savefig('Exercise_2.jpg')


main()
