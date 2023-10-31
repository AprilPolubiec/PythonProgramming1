# Write an iterative version of an isPal function to check whether a supplied string is
# a palindrome.

def isPal(in_string: str) -> bool:
    """Function which when given a string, check if it is a palindrome and returns true if it is

    Args:
        in_string (str): string to check

    Returns:
        bool: true if is palindrome
    """
    # Initiate a pointer to the left-most char
    left_ptr = 0
    # Initiate a pointer to the right-most char
    right_ptr = len(in_string) - 1
    while (left_ptr < right_ptr):
        # If left char is not equal to right char, short circuit out
        if in_string[left_ptr] != in_string[right_ptr]:
            return False
        # otherwise, move our left pointer to the right and our right pointer to the left
        left_ptr += 1
        right_ptr -= 1
    return True # We succesfully found a palindrome!

print(isPal('abcdcba'))
print(isPal('abccba'))
print(isPal('acba'))
print(isPal('acbaa'))