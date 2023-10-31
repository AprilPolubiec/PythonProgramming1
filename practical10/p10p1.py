# Write a program that prompts the user for an integer and performs exhaustive 
# enumeration to find the integer square root of the number. By “exhaustive enumeration”,
# we mean that we start at 0 and succcessively go through the integers, checking
# whether the square of the integer is equal to the number entered.
# If the number is not a perfect square, the program should print out a message to
# that effect. The program should exit when a negative number is entered.

# Prompt user for a number
# Set a max_seen value which stores the highest square we have found
# While our max_seen is less than our target
#   If the current value squared equals target, break out

target = int(input("Enter integer: "))
if (target < 0):
    print("Must be greater than 0")
    exit()
counter = 0
max_seen = 0

while (max_seen < target):
    if (counter**2 == target):
        print("Square root of {} is {}".format(target, counter))
        exit()
    max_seen = counter**2
    counter += 1

print("{} is not a perfect square".format(target))