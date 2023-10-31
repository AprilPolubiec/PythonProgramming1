# Write a program that prompts the user for a positive integer and uses a for loop to calculate
# the factorial of that number.

# Initialize target number to negative
# While the target number is less than 0
#   Request integer from user, stores as target
# Create an incrementer starting at 1 (bc 0 will always multiply to 0!)
# For each number in range 0 - target
#   Multiply incrementer by that number + 1 (because it will be from 0-target - 1)

target = int(input("Enter positive integer: "))

while (target < 0):
    print("Integer must be positive!")
    target = int(input("Enter positive integer: "))

incrementer = 1
for val in range(target):
    incrementer *= val + 1
print("{}! = {}".format(target, incrementer))