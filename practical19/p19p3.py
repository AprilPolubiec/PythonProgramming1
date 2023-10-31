# Write a program that reads a file and checks that brackets (ie ( and ), < and >, 
# { and } and [ and ]) are balanced, ie there should never be a situation where there
# are more right brackets of a particular type than there are corresponding left brackets
# and the total number of right brackets should equal the number of left brackets (You
# do not need to consider the interleaving of different bracket types). Your program
# should return the total number of each bracket and a message indicating whether or
# not the file has balanced brackets.

import os

def countBrackets(file_name):
    if os.path.isfile(file_name): # check if file exists
        f = open(file_name, "r") # open file in read mode
    else:
        raise Exception("File does not exist")
    
    # Initialize a counter for each type of bracket
    # Each counter is an array where idx [0] is the count of the open char, idx [1] is the count of the close char
    curly_count = [0, 0]
    parenthesis_count = [0, 0]
    angle_count = [0, 0]
    square_count = [0, 0]

    # Store a list of our openers, our closers and our counters
    open_chars = ["{", "(", "[", "<"]
    close_chars = ["}", ")", "]", ">"]
    counters = [curly_count, parenthesis_count, square_count, angle_count] # Indexes match the indexes in open/close chars (eg: curly is at 0)

    for char in f.read():
        if char in open_chars:
            i = open_chars.index(char)
            counters[i][0] += 1 # Every time we find a open char, we increase its counter by one
            continue
        
        if char in close_chars: # Every time we find a close char, we increase its counter by one
            i = close_chars.index(char)
            counters[i][1] += 1
            continue
    

    is_balanced = True
    idx = 0
    for counter in counters: # Count up all of our count arrays
        total = counter[0] + counter[1]
        if total % 2 != 0: # If its odd, its unbalanced
            is_balanced = False
        print(f"{open_chars[idx]}: found {counter[0]}")
        print(f"{close_chars[idx]}: found {counter[1]}")
        idx += 1
    print(f"Is file balanced? {is_balanced}")
    return [counter_arr[0] + counter_arr[1] for counter_arr in counters]

countBrackets("test_1.txt")
countBrackets("test_2.txt")

