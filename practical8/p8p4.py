# Write a program that uses a while loop to prompt the user for a series of integers and check 
# whether each number is in one of the specified ranges:
# • Number is equal to 0
# • Number is greater than 0 and less than or equal to 20
# • Number is greater than 20 and less than or equal to 40 
# • Number is greater than 40 and less than or equal to 60
# • Number is greater than 60 and less than or equal to 80
# • Number is greater than 80 and less than or equal to 100
# • Number is greater than 100
# The program should also count the number of numbers in each range.
# The program should continue until the user enters a number that is less than 0. 
# Before finishing, the program should print out the analysis of the input, ie the 
# number of numbers in each range.

# Request input value
# While the value is not negative

# Check what range the value is in
# Increase the counter for that range
# On loop finish, print the range counts

in_num = int(input("Enter integer: "))

zero_count = 0
below_20_count = 0
between_20_40 = 0
between_40_60 = 0
between_60_80 = 0
between_80_100 = 0
between_70_80 = 0
over_100 = 0

while (in_num >= 0):
    if (in_num == 0):
        zero_count += 1
    elif (in_num > 0 and in_num <= 20):
        below_20_count += 1
    elif (in_num > 20 and in_num <= 40):
        between_20_40 += 1
    elif (in_num > 40 and in_num <= 60):
        between_40_60 += 1
    elif (in_num > 60 and in_num <= 80):
        between_60_80 += 1
    elif (in_num > 80 and in_num <= 100):
        between_80_100 += 1
    else:
        over_100 += 1
    in_num = int(input("Enter integer: "))

print("Numbers == 0: {}".format(zero_count))
print("Numbers between 0 and 20: {}".format(below_20_count))
print("Numbers between 20 and 40: {}".format(between_20_40))
print("Numbers between 40 and 60: {}".format(between_40_60))
print("Numbers between 60 and 80: {}".format(between_60_80))
print("Numbers between 80 and 100: {}".format(between_80_100))
print("Numbers over 100: {}".format(over_100))