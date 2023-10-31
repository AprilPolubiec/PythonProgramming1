# Write a program that prompts the user for a series of non-negative integers and,
# for each of the numbers entered, uses a for loop to calculate that number of terms
# of the Fibonacci Series. The program should stop when a negative number is entered.

num_in = int(input("Enter int: "))
while (num_in > 0):
    prev_last_num_seen = 0
    last_num_seen = 1
    for val in range(num_in - 1): # Eg: [0, 1, 2]
        sum = prev_last_num_seen + last_num_seen
        prev_last_num_seen = last_num_seen
        last_num_seen = sum
    print("Term #{} of fib = {}".format(num_in, last_num_seen))
    num_in = int(input("Enter int: "))
print("Bye!")