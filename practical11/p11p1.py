# Taking the program to calculate the factorial of a number presented in class,
# investigate how it would be possible to have just two cases, one where the
# number is less than 0 and one where it isn"t. Rewrite the program to do this.

# Calculating the factorial of a number
# Program prompts the user for the number
# Uses a for loop
# Prompt the user for a number
number = int(input("Enter the number for which you wish to calculate the factorial (an int >= 0):  "))

if number < 0:
    print("Error:  Number entered was less than 0.")
else:
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    print("Factorial of", number, "is", fact)
print("Finished!")