# Write a function that takes as arguments two strings and returns
# True if either of the strings appears at the very end of the other
# string, ignoring upper/lower case differences (in other words, the
# computation should not be case sensitive). Recall that s.lower()
# returns the lowercase version of a string.

def checkSuffix(str_1: str, str_2: str) -> bool:
    """Given 2 strings, checks if one is the suffix of the other

    Args:
        str_1 (str): first string to check
        str_2 (str): second string to check

    Returns:
        bool: True if one of the strings is a suffix
    """
    # If str_1 is the bigger string, index from the end to the length of str_2 and check equality
    if len(str_2) <= len(str_1) and str_1[len(str_2) * -1:] == str_2:
        return True
    # If str_2 is the bigger string, index from the end to the length of str_1 and check equality
    if len(str_1) <= len(str_2) and str_2[len(str_1) * -1:] == str_1:
        return True
    return False

print(checkSuffix("potatocat", "cat"))
print(checkSuffix("cat", "potatocat"))
print(checkSuffix("cats", "potatocat"))
print(checkSuffix("cat", "potatocats"))