# Write a program that prompts the user for three numbers 
# (ints), examines the numbers and prints out the largest 
# odd number among them. If none of them is odd, the program 
# should print out a message to that effect. The program 
# should then terminate.

# Keep track of how many #s we've received
# Keep track of largest number we've seen
# Ask user for a number
# If the number is odd and is larger than the largest number we've seen
#    store it as the new largest number
# Increment the number of #s we've seen by 1
# After we've received all three numbers...
#  If there is a value in largest number, print it
#  If there is not (in other words we havent seen any odd numbers), print that its even



numbers_inputted = 0
largest_number = None

while numbers_inputted < 3:
    num = int(input("Insert number: "))
    if num % 2 == 1 and (largest_number == None or num >= largest_number):
        largest_number = num
    numbers_inputted += 1

if largest_number == None:
    print("No odd numbers entered")
else:
    print("Largest odd number is", largest_number)


