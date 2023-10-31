# Implement the recursive solution presented in lectures for checking whether given
# strings input by the user are palindromes.

def isPalindrome(s):
    def toChars(s):
        """Converts a string to lowercase and removes non-letters
        Assumes s is a str.
        Converts uppercase letters to lowercase and removes non-letter
        # First of all, convert uppercase letters to lowercase
        """
        s = s.lower()
        letterstring = ''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                letterstring += c
        return letterstring

    def isPal(in_string):
        if len(in_string) <= 1:
            return True
        else:
            return in_string[0] == in_string[-1] and isPal(in_string[1:-1])
    
    return isPal(toChars(s))

str = input("Enter a string (empty string to exit):  ")
while str != '':
    if isPalindrome(str):
        print(str, "is a palindrome")
    else:
        print(str, "is not a palindrome")
    str = input("Enter a string (empty string to exit):  ")
print("Finished!")