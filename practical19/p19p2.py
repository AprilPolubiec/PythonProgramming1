# Write a function that takes a string of digits, representing a number, 
# and a base (an int) as arguments, and returns the number in decimal (Base 10).
# The digits should include the letters A–F (uppercase and lowercase), so that
# hexadecimal numbers can be supplied and converted.

ASCII_A = 65
def convertToDecimal(num: str, base: int) -> int:
    """converts the given number into decimal

        Args:
        num (str): number to convert as a string
        base (int): base that num is in

    Returns:
        int: number in decimal
    """

    inc = 0  # Initialize our incrementer
    # First find the length of our string to find out what power to start at
    pow = len(num) - 1
    for char in num:
        if char.isalpha(): # If we have a letter, we need to convert to int
            val = ord(char) - ASCII_A + 10 # EG b -> 12
        else:
            val = int(char) # Get the integer value of the character
        inc += val * base**pow # Increase by the value times the base to the power of pow
        pow -= 1 # Decrement pow

    return inc

print(convertToDecimal('1011', 2)) # Expect 11
print(convertToDecimal('9B3', 16)) # Expect 2483