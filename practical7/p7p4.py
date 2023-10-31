# Write a program that uses a while loop to sum the first 5000 
# integers and prints out the total

num = 1
inc = 0

while num <= 5000:
    inc += num
    num += 1

print("Sum:", inc)