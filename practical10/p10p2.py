# Write a program that prompts the user for a series of integers and, for each of the numbers
# entered, performs exhaustive enumeration to find the integer cube root of the number.
# If the number is not a perfect cube, the program should print out a message to that 
# effect. Note that the program should work for negative numbers as well as positive 
# numbers. The program should exit when a 0 is entered.


# Prompt user for a number
# Set a max_seen value which stores the highest square we have found
# While our max_seen is less than our target
#   If the current value cubed equals target, break out

target = int(input("Enter integer: "))
while (target != 0):
    counter = 0
    max_seen = 0

    while (max_seen < target):
        if (counter**3 == target):
            print("Cube root of {} is {}".format(target, counter))
            break
        max_seen = counter**2
        counter += 1
    else:
        print("{} is not a perfect cube".format(target))
    
    target = int(input("Enter integer: "))

print("Finished!")