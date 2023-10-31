# Write a program that prompts the user for a series of strings and counts
# and prints out the number of vowels (letters ’a’, ’e’, ’i’, ’o’ or ’u’)
# in each string. The program should exit when an empty string is entered.

in_string = input("Enter string: ")
while (in_string != ""):
    vowel_count = 0
    for c in in_string:
        if (
            c == 'a' or 
            c == 'e' or 
            c == 'i' or  
            c =='o' or 
            c =='u' or
            c == 'A' or 
            c == 'E' or 
            c == 'I' or  
            c =='O' or 
            c =='U'
            ):
            vowel_count += 1
    print("Number of vowels:", vowel_count)
    in_string = input("Enter string: ")

print("Finished!")