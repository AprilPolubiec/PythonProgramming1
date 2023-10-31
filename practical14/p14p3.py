# Implement the program that searches for prime numbers in a range of integers and 
# demonstrates the use of the else clause in a for loop in Python from recent lectures
# (Lecture 13) (Page 16 of the notes). Ensure that you understand how this program works

for val in range(2, 20):
    for div in range(2, val):
        if (val % div == 0):
            print(val, "equals", div, "*", val//div)
            break
    else:
        print(val, "is prime")