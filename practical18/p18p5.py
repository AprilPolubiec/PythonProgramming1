# Write a function that takes a string as an argument and returns True if
# the given string contains an appearance of “xyz” where the “xyz” is not
# directly preceeded by a period (“.”). So “xxyz”, “xxyz.x.xyzz” and “xyz.xyz”
# are accepted but “x.xyz” is not.

def checkXyz(in_str: str) -> bool:
    """Checks a string for the presence of "xyz" without being preceded by a "."

    Args:
        in_str (str): string to look in

    Returns:
        bool: true if it contains xyz
    """
    idx = 0
    # Starting from 0 until 3 back from the end of the string (no point in checking the last 2 chars since xyz is impossible)
    while idx <= len(in_str) - 3:
        if in_str[idx] == '.':
            idx += 2 # If its a period, we can skip 2 indices ahead since we know the next wont be valid
            continue
        if in_str[idx:idx + 3] == "xyz": # Check if this is a xyz
            return True
        idx += 1 # Increment to the next idx
    return False

print(checkXyz("xxyz")) # True
print(checkXyz("xxyz.x.xyzz")) # True
print(checkXyz("xyz.xyz")) # True
print(checkXyz("x.xyz")) # False