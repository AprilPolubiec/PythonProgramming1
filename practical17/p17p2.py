import time
# Using your solution for the previous question as a guide, implement a optimised solution
# for calculating the common divisors of two numbers.

def findDivisorsOptimised(num1, num2, debug = False):
    """Finds the common divisors of num1 and num2
    Assumes that num1 and num2 are positive integers
    Optimised solution by also checking the multiplier of each divisor
    Returns a tuple containing the common divisors of num1 and num2"""
    loop_count = 0 # For testing optimisation
    max_num = max(num1, num2)
    min_num = min(num1, num2)

    # The highest number we will check is half of the smallest number; eg: num1,num2 = 20, 30; max_divisor = 10
    max_divisor = min(max_num // 2, min_num)
    # Can initialize with 1 and max_divisor
    divisors = (1,)
    if min_num % max_divisor == 0: # If our min number is also divisible by the highest divisor we are checking, we can add it to divisors!
        divisors += (max_divisor,)
    i = 2
    while max_divisor > i: # start at 2 and only go up to the max_divisor - 1
        if debug: loop_count += 1
        if num1 % i == 0 and num2 % i == 0: # This is a number that both values are divisible by
            divisors += (i,)

            # Given the divisors, we can also deduce their mulipliers and check if the other value is divisible by the multiplier
            # eg: i = 2, num1_multiplier = 10, num2_multiplier = 30
            num1_multiplier = int(num1 / i)
            if num2 % num1_multiplier == 0: # If num2 is divisible by num1_multiplier, we can add that to our list too! eg: num1_multiplier = 10, 30 % 10 == 0, 10 is another common denom
                divisors += (num1_multiplier,)
                max_divisor = min(num1_multiplier, max_divisor) # If our multiplier is less than our max_divisor, we can set this to the new max divisor!

            num2_multiplier = int(num2 / i)
            if num1 % num2_multiplier == 0: # eg: 10 % 30 != 0
                divisors += (num2_multiplier,)
                max_divisor = min(num2_multiplier, max_divisor)
        i += 1
    
    if debug:
        print("findDivisorsOptimised found divisors in {} loops".format(loop_count))
    return divisors

print(findDivisorsOptimised(30, 20))


# Optimization test
def findDivisors(num1, num2, debug = False):
    """Finds the common divisors of num1 and num2
    Assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    loop_count = 0
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    max_divisor = min(max_num // 2, min_num)
    divisors = (1,)

    if min_num % max_divisor == 0: # If our min number is also divisible by the highest divisor we are checking, we can add it to divisors!
        divisors += (max_divisor,)
    for i in range(2, max_divisor):
        if debug: loop_count += 1
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    if debug:
        print("findDivisors found divisors in {} loops".format(loop_count))
    return divisors

def runTest(num1, num2):
    print("==TEST {} {}==".format(num1, num2))
    start = time.time_ns()
    findDivisors(num1, num2, True)
    stop = time.time_ns()
    elapsed1 = (stop - start) * 1000
    print("Elapsed: {}ns".format(elapsed1))
    start = time.time_ns()
    findDivisorsOptimised(num1, num2, True)
    stop = time.time_ns()
    elapsed2 = (stop - start) * 1000
    print("Elapsed: {}ns".format(elapsed2))
    print("Optimised faster?: {}".format('YES' if elapsed2 < elapsed1 else 'NO'))

def testOptimisation():
    runTest(20, 30)
    runTest(24, 36)


testOptimisation()