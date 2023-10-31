# Write a program that takes as input a single length (a float) and calculates the following:
# • The area of a square with side of that length
# • The volume of a cube with side of that length
# • The area of a circle with radius of that length
# • The volume of a sphere with radius of that length
# • The volume of a cylinder with radius of that length and side of that length
# Import the math module and use the constant math.pi for the value π.
# When the length is entered by the user, the program should check that it is non-negative. 
# If the length is negative, the message “Length must be >= 0. Please try again.” should be 
# printed out and the program should exit.

import math

length = float(input("Length: "))
if length > 0:
    pi = math.pi

    # • The area of a square with side of that length
    area_square = length * length
    print('Area of square =', area_square)

    # • The volume of a cube with side of that length
    volume_cube = length * length * length
    print('Volume of cube =', volume_cube)

    # • The area of a circule with radius of that length
    radius = length
    area_circle = pi * (radius**2)
    print('Area of circle =', area_circle)

    # • The volume of a sphere with radius of that length
    vol_sphere = (4/3) * pi * radius**3
    print('Volume of sphere =', vol_sphere)


    # • The volume of a cylinder with radius of that length and side of that length
    vol_cylinder = pi * radius**2 * length
    print('Volume of cylinder =', vol_cylinder)
else:
    print('Length must be >= 0. Please try again.')