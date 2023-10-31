# A perfect number is a positive integer that is equal to the sum of its
# proper factors (its positive integer factors excluding the number itself).
# For example, 6 (with proper factors 1, 2 and 3) and 28 (with proper factors
# 1, 2, 4, 7 and 14) are perfect numbers.
# Write a program that prompts the user for a positive integer and finds all
# the perfect numbers up to and including that number.

def sumProperFactors(val: int) -> int:
    """Given a positive integer $val, returns the sum of its proper factors

    Args:
        val (int): Value to get sum of proper factors of

    Returns:
        int: Sum of proper factors
    """
    sum = 0
    for num in range(1, val):
        if val % num == 0:
            sum += num
    return sum

def findPerfectNumbers(val):
    numbers = ()
    for num in range(0, val + 1):
        sum = sumProperFactors(num)
        if num == sum:
            numbers += (num,)
    return numbers

in_val = 0
while in_val >= 0:
    in_val = int(input("Enter value: "))
    if in_val >= 0:
        print(findPerfectNumbers(in_val))
print("Finished!")