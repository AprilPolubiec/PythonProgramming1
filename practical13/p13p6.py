# (a) Write a recursive function that takes as its single argument a non-negative integer and
# returns the factorial of the number.

# Write function
# Input = integer (non-negatic)
# Return = integer
def fact(num):
    print("Running fact({})".format(num))
    # Validate number is positive
    if (num < 0):
        # Do something & return
        return
    if (num == 0): # When we hit base case, we will return the number
        print("Base case, return 1")
        return 1
    else: # For each number call the factorial
        num *= fact(num - 1)
        print("{} *= fact({} - 1) = {}".format(num, num, num))
        return num


# (b) Write a program that prompts the user for an integer and checks that the number entered is
# non-negative. If it is, it calls the function defined in part (a) and prints out the result;
# if not, it prints out an appropriate error message.

# Request input
in_val = int(input("Enter integer: "))
if in_val < 0:
    print("Integer must be >= 0. Try again.")
else:
    res = fact(in_val)
    print(res)
print("Finished!")

# (c) In your function, include some print statements that allow you to see the operation of the
# recursion and its progress towards the base case.