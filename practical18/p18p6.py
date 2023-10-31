# Write a program that takes a page (eg the source of a Web page
# that you have saved), counts the occurrences of left angle brackets (<),
# right angle brackets (>), newlines, the lowercase letter e, the string
# <!-- and the string --> and prints out the results to a file results.txt.
# Your program should make appropriate checks regarding the existence of the
# input and output files.

        
# Utility functions
def isOpenCommentBracket(in_str):
    return in_str == '<!--'
def isCloseCommentBracket(in_str):
    return in_str == '-->'

# open the file
try:
    htmlFile = open("p18p6.html", "r")
except:
    print("Failed to find file")
    exit(400)

# Start a counter for each thing
left_angle_count = 0
right_angle_count = 0
new_line_count = 0
e_count = 0
open_comment_count = 0
close_comment_count = 0

# Read the lines of the file
lines = htmlFile.readlines()

for line in lines: # For each line...
    char_idx = 0 # Keep track of our char idx so we can check substrings
    for char in line: # and for each char in the line...
        # Check substrings first
        if isOpenCommentBracket(line[char_idx:char_idx + 4]):
            open_comment_count += 1
        if isCloseCommentBracket(line[char_idx:char_idx + 3]):
            close_comment_count += 1
        
        # Now check individual chars
        if char == '<':
            left_angle_count += 1
        elif char == '>':
            right_angle_count += 1
        elif char == 'e':
            e_count += 1
        elif char == '\n':
            new_line_count += 1
        char_idx += 1

try:
    outputFile = open("output.txt", "w")
except:
    print("output.txt doesnt exist")
    exit()

outputFile.writelines([f"Left angles: {left_angle_count}\n", f"Right angles: {right_angle_count}\n", f"New lines: {new_line_count}\n", f"'e' count: {e_count}\n", f"Open comments: {open_comment_count}\n", f"Close comments: {close_comment_count}\n"])