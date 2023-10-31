# Add some extra variables and operations on those variables in the program
# from the previous question to ensure that you understand what is going on and how it works.
# Save this program as p13p5.py.


# Program to illustrate scoping in Python
def f(x):
    """Function that adds 1 to its argument and prints it out""" 
    print("In function f:")
    x += 1
    y = 1
    z = 0
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return y

x, y, z = 5, 10, 15
print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
z = f(x)
print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)