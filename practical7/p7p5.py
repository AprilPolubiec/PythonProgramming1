# Write a program that sums the integers in the range 1–10000 that are divisble by 3 or by 5 and
# prints out the total.

sum = 0
count = 1

while count <= 10000:
    if count % 3 == 0 or count % 5 == 0:
        sum += count
    count += 1


print("Total:", sum)