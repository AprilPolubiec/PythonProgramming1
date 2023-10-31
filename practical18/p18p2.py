# Write a function that takes a string as an argument and returns the
# number of times that the string “code” (case-sensitive) appears anywhere
# in the given string.

def appearances(in_string: str) -> int:
    """Given a string, in_string, checks how many times the word "code" occurs in it

    Args:
        in_string (str): word to search through

    Returns:
        int: number of times "code" appears in the word
    """
    i = 0 # Keep track of what idx we are checking
    count = 0 # Keep track of how many times we've seen the word
    while i < len(in_string):
        if in_string[i:i+len("code")] == "code":
            i += len("code") # If we found code, we can move our idx forward to the end of the word 'code"
            count += 1 # increase count
        else:
            i += 1 # if not, move our idx to the right one
    return count

print(appearances("codeh ecodel locode"))