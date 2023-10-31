# Write a program that prompts the user for a series of positive integers and,
# for each of the numbers entered, uses a for loop to calculate the sum of the
# positive integers up to and including that number. The program should stop
# when a non-positive number is entered.

# Initialize target number to 0
# While the target number is >= 0
#   Request number from user, store as target number
#   Initialize counter to 0
#   Initialize accumulator to 0
#   While counter is less than the target number
#       add counter number to the accumulator
#   Print the number

target = 0

while (target >= 0):
    target = int(input("Enter number: "))
    accumulator = 0
    for val in range(target + 1):
        accumulator += val
    print("Sum of numbers up to {} is {}".format(target, accumulator))

print("Finished!")