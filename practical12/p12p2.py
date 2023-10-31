# a) Write a function that takes as its argument a non-negative integer and prints out that 
# number of terms of the Fibonacci Series. This function should not return an explicit value.

# Write function
# Input = non-neg int
# Return = void
# Outcome = print #
def printFib(num):
    out_str = ""
    first_num = 0 # Store the first number of fibonacci
    second_num = 1 # Store the second number of fibonacci
    out_str += str(first_num) + ' '
    out_str += str(second_num) + ' '
    # Iterate num -2 times (minus 2 because we already stored the first and second)
    for val in range(num - 2):
        current_val = first_num + second_num # Current value is the first_num plus the second_num
        out_str += str(current_val) + " "
        first_num = second_num # Shift our second num to our first num
        second_num = current_val # Our second num is our current value
    print(out_str)


# (b) Write a program that prompts the user for an integer and checks that the number entered
# is non-negative. If it is, it calls the function defined in part (a); if not, it prints out
# an appropriate error message.

# Prompt for a number
in_val = int(input("Enter integer: "))

# If its negative, print an error
if in_val < 0:
    print("Integer must be less than 0. Try again!")
else: # If its positive, continue running our program
    printFib(in_val)

print("Finished!")