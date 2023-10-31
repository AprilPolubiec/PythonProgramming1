length = 232008.36
pi = 3.1415927
# • The area of a square with side of that length
area_square = length * length
print('Area of square =', area_square)

# • The volume of a cube with side of that length
volume_cube = length * length * length
print('Volume of cube =', volume_cube)

# • The area of a circle with diameter of that length
diameter = length
radius = diameter / 2 # 116004.18
area_circle = pi * (radius**2)
print('Area of circle =', area_circle)

# • The volume of a sphere with diameter of that length
vol_sphere = (4/3) * pi * radius**3
print('Volume of sphere =', vol_sphere)


# • The volume of a cylinder with diameter of that length and side of that length
vol_cylinder = pi * radius**2 * length
print('Volume of cylinder =', vol_cylinder)
