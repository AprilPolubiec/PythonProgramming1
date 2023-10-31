# Write a Python function that takes a number in base 10 and a base,
# both positive ints, and, using the algorithm presented in lectures,
# returns the number in the base supplied.

ASCII_A = 65
ASCII_Z = 90

def getNumberInBaseX(base_10_num: int, base: int) -> str:
    """Given a number in base 10 and a base, returns the number converted to the given base

    Args:
        base_10_num (int): base 10 number to convert
        base (int): base to convert to

    Returns:
        int: converted value as a string
    """
    # Initialize a string to push each int value into
    converted = ""
    # Initialize a incrementer which we will run divisions on
    inc = base_10_num
    while inc > 0:
        # Get the remainder
        remainder = inc % base
        if remainder >= (ASCII_Z - ASCII_A) + 10:
            raise Exception("Can't support bases over 36")
        # If our remainder is >= 10, we need to use letters
        if remainder >= 10: # 65 is the ASCII value of A
            converted = chr(ASCII_A + (remainder - 10)) + converted
        else:
            converted = str(remainder) + converted  # add to the front of our string
        inc //= base # divide our incrementer
    
    return converted # convert string to int

print(getNumberInBaseX(379, 8)) # Expect 573
print(getNumberInBaseX(4592, 2)) # Expect 1 0001 1111 0000
print(getNumberInBaseX(2483, 16)) # Expect 9B3
# print(getNumberInBaseX(2483, 36)) # Expect throw