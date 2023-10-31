# • Number is equal to 0
# • Number is greater than 0 and less than or equal to 20
# • Number is greater than 20 and less than or equal to 40 
# • Number is greater than 40 and less than or equal to 60 
# • Number is greater than 60 and less than or equal to 80 
# • Number is greater than 80 and less than or equal to 100 
# • Number is greater than 100

num = int(input("Number: "))
if num == 0:
    print(num, "is zero.")
elif num > 0 and num <= 20:
    print(num, "is greater than 0 and <= 20")
elif num > 20 and num <= 40:
    print(num, "is greater than 20 and <= 40")
elif num > 40 and num <= 60:
    print(num, "is greater than 40 and <= 60")
elif num > 60 and num <= 80:
    print(num, "is greater than 60 and <= 80")
elif num > 80 and num <= 100:
    print(num, "is greater than 80 and <= 100")
elif num > 100:
    print(num, "is greater than 100")
else:
    print(num, "is negative.")
