# (a) Write a function that takes as its single argument a non-negative integer and returns the factorial of the number.

# Write function
# Input = integer (non-negatic)
# Return = integer
def fact(num):
    acc = 1 # initialize an accumulator to 1 (not 0 bc then everything will be 0)
    for val in range(num): # Iterate num times (eg: num = 5, 4 loops [0, 1, 2, 3, 4])
        multiplier = val + 1 # Increase the val by 1
        acc *= multiplier # Increment multiplier
    return acc # Return accumulator

# (b) Write a program that prompts the user for an integer and checks that the number entered is non-negative. 
# If it is, it calls the function defined in part (a) and prints out the result; if not, it prints out an appropriate 
# error message.

# Request user for input
in_val = int(input("Enter integer: "))
if in_val < 0: # If its less than 0, print error
    print("Integer must be > 0.")
else: # If its greater than 0, call fact and print result
    res = fact(in_val)
    print(res)

print("Finished!")