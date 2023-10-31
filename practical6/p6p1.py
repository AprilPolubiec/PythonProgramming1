# Write a program that prompts the user for two numbers. If the sum 
# of the numbers is greater than 100, print “That is a big number!” 
# and terminate the program.

# Ask for first number
num1 = int(input("Insert 1st number: "))

# Ask for second number
num2 = int(input("Insert 2nd number: "))

# Add numbers
sum = num1 + num2

# If sum is over 100, print
if sum > 100:
    print("That is a big number!")