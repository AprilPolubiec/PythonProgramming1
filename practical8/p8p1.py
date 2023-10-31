# Write a program that uses a while loop to prompt the user for a series of numbers, 
# check whether each number is divisble by 2, 3, 5 or 7 and print out which of 2, 3, 
# 5 or 7 it is divisible by. Execution of the program continues until a negative number 
# is entered.

in_num = 0
# Ask for input while the input is still positive
while (in_num >= 0):
    in_num = int(input("Enter number: "))
    # Check if divisible by 2 3 5 or 7
    if (in_num % 2 == 0):     # print what it is divisible by
        print("{} is divisible by {}".format(in_num, 2))
    if (in_num % 3 == 0):
        print("{} is divisible by {}".format(in_num, 3))
    if (in_num % 5 == 0):
        print("{} is divisible by {}".format(in_num, 5))
    if (in_num % 7 == 0):
        print("{} is divisible by {}".format(in_num, 5))
print("Goodbye!")