
# (a) Write a recursive function that takes as its single argument a positive integer
#     and prints out that number of terms from the Fibonacci Series.

def fibonacciRecursive(val):
    # Base case - return the first and second value of fib (0)
    print("Current value:", val)
    if val == 1:
        print("Base case 1")
        return 0
    if val == 2:
        print("Base case 2")
        return 1
    sum = fibonacciRecursive(val - 1) + fibonacciRecursive(val - 2)
    print("Returning {}".format(sum))
    return sum

def printTerms(val):
    terms_str = ""
    for i in range(val):
        print("Getting the value {} of fibonacci".format(i))
        terms_str += str(fibonacciRecursive(i + 1)) + " "
    print(terms_str, sep=" ")

# (b) Write a program that prompts the user for a series of integers. For each number 
#     entered the program should check that it is non-negative. If it is, it calls the 
#     function defined in part (a). The program should stop when a non-positive number is entered.

in_val = 0
while in_val >= 0:
    in_val = int(input("Enter integer: "))
    printTerms(in_val)
print("Finished!")

# (c) In your function, include some print statements that allow you to see the operation of the 
#     recursion and its progress towards the base cases.