# Write a function that takes a string as an argument and returns the number
# of times that the string “code” (case-sensitive) appears anywhere in the
# given string, except that any letter will be accepted for the “d”, so
# “that cope”, “cooe” and “coDe” will also be accepted, but co3e”, “co-e” and
# “coe” will not be.


def appearances(in_string: str) -> int:
    """Given a string, in_string, checks how many times the word "code" occurs in it
    but any letter (alphabetical letters only) is accepted for "d"

    Args:
        in_string (str): string to look in

    Returns:
        count: number of occurrences
    """
    i = 0 # Keep track of what idx we are checking
    count = 0 # Keep track of how many times we've seen the word
    while i < len(in_string) - 3:
        if in_string[i : i + 2] == "co" and in_string[i + 2].isalpha() and in_string[i + 3 : i + 4] == "e": # Check the first 2 and last letter
            i += len("code") # If we found code, we can move our idx forward to the end of the word 'code"
            count += 1 # increase count
        else:
            i += 1 # if not, move our idx to the right one
    return count

print(appearances("that cope")) # 1
print(appearances("cooe")) # 1
print(appearances("cooe")) # 1
print(appearances("co3e")) # 0
print(appearances("co-e")) # 0
print(appearances("coe")) # 0