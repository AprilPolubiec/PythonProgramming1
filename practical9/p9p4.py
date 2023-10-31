# Write a program that prompts the user for a series of positive integers and,
# for each of the numbers entered, uses a while loop to calculate the factorial
# of that number. The program should stop when a negative number is entered.

# Request integer from user, stores as target
# While the target number is more than 0
#   Create an incrementer starting at 1 (bc 0 will always multiply to 0!)
#   Create a counter starting at 1
#      While counter <= target
#           Multiply incrementer by that counter (because it will be from 0-target - 1)
#           increase counter by 1
#   Request integer again, store as target
# Print finished

target = int(input("Enter positive integer: "))

while (target >= 0):
    incrementer = 1
    counter = 1
    while (counter <= target):
        incrementer *= counter
        counter += 1
    print("{}! = {}".format(target, incrementer))
    target = int(input("Enter positive integer: "))

print("Finished!")