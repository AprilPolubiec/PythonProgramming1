import time

# Recursive factorial
def factRecursive(num):
    # print("Running fact({})".format(num))
    # Validate number is positive
    if (num < 0):
        # Do something & return
        return
    if (num == 0): # When we hit base case, we will return the number
        # print("Base case, return 1")
        return 1
    else: # For each number call the factorial
        num *= factRecursive(num - 1)
        # print("{} *= fact({} - 1) = {}".format(num, num, num))
        return num

# Non-recursive factorial
def fact(num):
    acc = 1 # initialize an accumulator to 1 (not 0 bc then everything will be 0)
    for val in range(num): # Iterate num times (eg: num = 5, 4 loops [0, 1, 2, 3, 4])
        multiplier = val + 1 # Increase the val by 1
        acc *= multiplier # Increment multiplier
    return acc # Return accumulator

in_val = 0
while (in_val >= 0):
    in_val = int(input("Enter integer: "))

    # Run non-recursively
    time_start = time.time()
    fact(in_val)
    time_end = time.time()
    print("Non-recursive strategy time: {}ms".format(((time_end - time_start) * 1000)))

    # Run non-recursively
    # time_start = time.time()
    # factRecursive(in_val)
    # time_end = time.time()
    # print("Recursive strategy time: {}ms".format(((time_end - time_start) * 1000)))