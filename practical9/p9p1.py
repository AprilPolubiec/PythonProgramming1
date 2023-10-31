# Write a program that prompts the user for a positive integer and uses a while
# loop to calculate the sum of the positive integers up to and including that number.

# Request an input number
# If num is less than 0, request again
# Create a counter initialized to 0
# Create an accumulator initialized to 0
# While the counter is less than the input number
#    Add the counter to the accumulator
# When loop is over
# Print sum

int_num = int(input("Enter positive integer: "))

while (int_num < 0):
    print("Integer must be positive!")
    int_num = int(input("Enter positive integer: "))

counter = 0
acc = 0

while (counter <= int_num):
    acc += counter
    counter += 1

print("Sum =", acc)
