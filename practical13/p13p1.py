# Implement the programs that illustrate the definition and use of functions in Python 
# from the lectures (Pages 4 and 5 of the notes on Lecture 15, the section on “Function
# Definition and Function Use”).
# Save these programs as p13p1.py and p13p2.py, respectively.

# Program to print out the largest of two numbers entered by the user
# Uses a function max
def max(a, b):
    """Function that returns the largest of its two arguments"""
    if a > b:
        return a
    else:
        return b

# Prompt the user for two numbers
number1 = float(input("Enter a number:  "))
number2 = float(input("Enter a number:  "))
biggest = max(number1, number2)
print("The largest of", number1, "and", number2, "is", biggest)
print("Finished!")