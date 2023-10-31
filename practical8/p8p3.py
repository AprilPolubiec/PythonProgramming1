# Write a program that uses a while loop to generate a simple multiplication table 
# from 0 to 20. For example, were the user to enter “6”, the following table would 
# be generated:

# 00 16
# 2 12
# 3 18
# 4 24
# 5 30
# 6 36
# 7 42
# 8 48
# 9 54
# 10 60
# 11 66
# 12 72
# 13 78
# 14 84
# 15 90
# 16 96
# 17 102
# 18 108
# 19 114
# 20 120

# Request a number
# Loop over numbers 0 - 20
# For each number, get product of input * number
# Print number and product

in_num = int(input("Enter number: "))
counter = 0

print("Times 6 Table")
while (counter <= 20):
    print(counter, counter * in_num)
    counter += 1