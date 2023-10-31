# Write a program that prompts the user for a non-negative integer and uses
# a while loop to calculate that number of terms of the Fibonacci Series.
# Try to make the program as small and efficient as possible.

in_num = int(input("Enter integer: "))

counter = 0
prev_last_num_seen = 0
last_num_seen = 1

while (counter < in_num - 1):
    sum = prev_last_num_seen + last_num_seen
    prev_last_num_seen = last_num_seen
    last_num_seen = sum
    counter += 1
print("Term #{} of fib = {}".format(in_num, last_num_seen))