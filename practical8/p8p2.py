# Write a program that prompts the user for a number and uses a while 
# loop to generate the “multiplication table” for that number from 1 up 
# to the number. For example, if the user were to enter “5”, the following 
# table would be generated:

# 1 2 3 4 5 
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

# Ask for a number
in_num = int(input("Insert a number: "))
# Start counter
row_num = 1
# While our counter is less than the input number
while (row_num <= in_num):
    col_num = 1
    row_str = ""
    # Print row * col
    while (col_num <= in_num):
        row_str += str(row_num * col_num) + " "
        col_num += 1
    print(row_str)
    row_num += 1