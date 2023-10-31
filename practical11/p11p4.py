# Write a program that prompts the user for an integer and calculates that number
# of Catalan Numbers using one or more of the above techniques.

in_num = int(input("Enter integer: "))

# Formula = (2n)! / (n + 1)!n!
def calculateFactorial(val):
    fact = 1
    for i in range(1, val + 1):
        fact *= i
    return fact

num_catalan = calculateFactorial(2 * in_num) // (calculateFactorial(in_num) * calculateFactorial(in_num + 1))
print("Catalan numbers", num_catalan)