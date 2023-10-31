# Using the program developed in Question 3 as a starting point, or
# using a completely new technique if you prefer, write a program
# that searches for prime numbers in a range of integers. Again, the
# program should print out an appropriate message if a number is a
# prime number. However, instead of printing out the first pair of
# factors that it discovers for a non-prime number, this program should
# print out all the pairs of factors.

for val in range(2, 20):
    for div in range(2, val):
        if (val % div == 0):
            print(val, "equals", div, "*", val//div)
    else:
        print(val, "is prime")