# Implement the program to calculate common divisors from Lecture 16.
# You may use the solution on Pages 14–17 of the slides in your solution.

# Write a program that prompts the user for two positive integers, finds and
# prints out their common divisors, sums the common divisors and prints out the total
# Prompt the user for two positive integers
# if the numbers entered are not positive then
# print out an error message
# else
# find the common divisors print out the common divisors sum the common divisors print out the total

def findCommonDivisors(num1, num2):
    """Given two numbers, finds the common divisors and returns as a list

    Args:
        num1 (int): First number
        num2 (int): Second number

    Returns:
        None
    """
    min_num = min(num1, num2)
    sum = 0
    divisors = ()
    for val in range(min_num):
        if num1 % (val + 1) == 0 and num2 % (val + 1) == 0:
            divisors += (val + 1,)
            sum += val + 1
    print("Divisors: {}".format(divisors))
    print("Sum: {}".format(sum))
    return

in_val_1 = 0
in_val_2 = 0

while(in_val_1 >= 0 and in_val_2 >= 0):
    in_val_1 = int(input("Enter first number: "))
    in_val_2 = int(input("Enter second number: "))
    if in_val_1 >= 0 and in_val_2 >= 0:
        findCommonDivisors(in_val_1, in_val_2)
    else:
        print("Both numbers must be positive")

print("Finished!")