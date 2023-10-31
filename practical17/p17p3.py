# Write a Python program that checks whether the strings “cat” and “dog”
# appear the same number of times in a given string input by the user

def isSameCount(input_str: str) -> bool:
    if len(input_str) < 6: # Not enough letters to have both dog and cat
        return False
    cat_ptr = 0 # Keep a ptr to where we last saw cat
    cat_count = 0 # How many cats we have seen

    dog_ptr = 0
    dog_count = 0
    while cat_ptr < len(input_str) and dog_ptr < len(input_str): # while at the cat_ptr or dog_ptr has no hit the end of the string
        has_dog = input_str[dog_ptr:].find("dog") # Check if there is a dog

        if has_dog > -1:
            dog_count += 1 # Increment
            dog_ptr += has_dog + 3 # Move point to the end of "dog"
        else:
            dog_ptr = len(input_str) # Set dog_ptr to the end of string so we stop looking for it
        
        # Repeat for cat
        has_cat = input_str[cat_ptr:].find("cat")
        if has_cat > -1:
            cat_count += 1 
            cat_ptr += has_cat + 3
        else:
            cat_ptr = len(input_str)
    return cat_count == dog_count

in_string = input("Enter a string: ")
is_same_count = isSameCount(in_string)
if is_same_count:
    print("cat and dog appear equal number of times!")
else:
    print("nope")