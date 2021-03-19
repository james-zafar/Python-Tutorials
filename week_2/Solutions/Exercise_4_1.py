# Exercise 4
# Given a set of grades stored in a dictionary where the keys represent
# the subject and values represent the grades we would like to know in
# which subject the lowest and highest grades were achieved.

# Extension: Try to enhance this implementation to print the grade
# achieved as well as the subject itself.

# Further extension: Write a function that shows all of the grades that are
# at least 70.


def compute_min(grades: dict) -> float:
    return min(grades, key=grades.get)


def compute_max(grades: dict) -> float:
    return max(grades, key=grades.get)


input_grades = {'math': 80, 'Science': 40, 'English': 62, 'Computer science': 87}
min_subject = compute_min(input_grades)
max_subject = compute_max(input_grades)
min_grade, max_grade = None, None
for subject, grade in input_grades.items():
    if subject == min_subject:
        min_grade = grade
    if subject == max_subject:
        max_grade = grade

print('Min grade:', min_subject, min_grade)
print('Max grade:', max_subject, max_grade)

# Solution for further extension
for grade in input_grades:
    if input_grades[grade] > 70:
        print(grade, ':', input_grades[grade])
