# Exercise 4
# Given the radius of a sphere we should be able to calculate its volume using
# v = (4 / 3) * pi * r^3, where r > 0
#  What input validation can we implement to prevent the user for entering a negative radius?

from math import pi


def volume_of_sphere(radius: float) -> float:
    radius = abs(radius)
    return (4.0 / 3.0) * pi * (radius ** 3)


print(volume_of_sphere(5))
print(volume_of_sphere(-1))
