# (a) Write a function that takes as its two arguments a number and a tolerance and, 
# using the technique exposed in lectures, returns an approximation of the square root
# of the number that is within the tolerance.

# Write function
# Input = num (float), tolerance (float)
# Output = approx(float)
def calculateApproximation(num: float, tolerance: float):
    # Starting from 0
    # Increase by step (which is tolerant^2)
    step = tolerance ** 2
    root = 0.0

    max_value = num + tolerance

    # Check if the val^2 is within tolerance of num
    # Should break out if the value surpasses our number
    while (abs(num - root ** 2) >= tolerance):
        root += step
        if (root > max_value):
            # If we surpass our number, there is no approx sq root
            print("Failed to find a square root of", num)
            break
    print("Approximate square root of {} is {} (tolerance: {})".format(num, root, tolerance))


# (b) Write a program that prompts the user for a floating-point number and checks
# that the number entered is non-negative. If it is, it calls the function defined in part
# (a) with the number and a tolerance defined in the program and prints out the square
# root of the number; if not, it prints out an appropriate error message.

# Request a float number
in_val = float(input("Insert float: "))

# If its negative, print error
if in_val < 0:
    print("Value must be greater than 0!")
else:
    calculateApproximation(in_val, 0.01)
print("Finished!")