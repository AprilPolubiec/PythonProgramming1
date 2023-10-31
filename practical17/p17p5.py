# Implement a variation of the palindrome program that prints out messages to allow you to trace how it works. For example, modify the isPal function as follows:
#          def isPal(s):
#              """Checks whether the string s is a palindrome
#              Assumes that s is a str with only lowercase letters and no non-letters.
#              Returns True if s is a palindrome;
#              Returns False otherwise.
#              Recursive function.
#              Has print statements to trace its operation."""
#              print ’isPal function called with argument’, s
#              if len(s) <= 1:
#      # A palindrome of length 0 or 1 is a palindrome
#                  print ’About to return True from isPal from the base case’
#                  return True
#              else:
#      # Compare the first and the last letters and check the remainder of the string
#                  result = s[0] == s[-1] and isPal(s[1:-1])
#                  print ’About to return result’, result, ’from isPal with argument’, s
#                  return result
# Ensure you understand how this works.

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

str = input("Enter a string:  ")
while str != '':
    if isPalindrome(str):
        print(str, "is palindrome")
    else:
        print(str, "is not palindrome")
    str = input("Enter a string:  ")
print("Finished!")