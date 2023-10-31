# Two suggested optimisations for the algorithm to calculate the divisors of a number
# are to initalise the divisors tuple to include 1 and the number itself and to only
# search from 2 and as far as half of the number.
# Revise the solution on Pages 14–17 of the slides to include these optimisations.

def findDivisors(num):
    """Finds the divisors of num
    Assumes that num is a positive integer
    Returns a tuple containing the divisors of num"""
    divisors = (1, num // 2)

    for i in range(2, num // 2):
        if num % i == 0:
            divisors += (i,)
    return divisors

number1 = int(input("Enter a positive integer:  "))
number2 = int(input("Enter another positive integer:  "))
if number1 <= 0 or number2 <= 0:
    print("Numbers should be > 0.")
else:
# First of all, get the common divisors and print them out
    divisors = findDivisors(number1, number2)
    print("The common divisors of", number1, "and", number2, "are:", divisors)
# Now sum them and print the total
    total = 0
    for d in divisors:
        total += d
    print("Sum of the common divisors is:", total)
print("Finished!")