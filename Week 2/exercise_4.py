# Exercise 4
# Given a set of grades stored in a dictionary where the keys represent
# the subject and values represent the grades we would like to know in
# which subject the lowest and highest grades were achieved.

# Extension: Try to enhance this implementation to print the grade 
# achieved as well as the subject itself.

# Further extension: Write a function that shows all of the grades that are
# at least 70.

def compute_min(grades: dict) -> float:
    return min(grades)


def compute_max(grades: dict) -> float:
    return max(grades)


input_grades = {'math': 80, 'Science': 40, 'English': 62, 'Computer science': 87}
print('Min grade:', compute_min(input_grades))
print('Max grade:', compute_max(input_grades))
