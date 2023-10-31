# Write a program that uses a while loop to go through the first 50 
# integers and prints out each number and the square of the number.

num = 1

while num <= 50:
    print(str(num) + "^2 = " + str(num**2))
    num += 1