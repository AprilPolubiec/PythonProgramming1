# Write a program that prompts the user for a year and checks whether 
# the year is a leap year. Use my algorithm from Lecture 8.

# Algorithm
# Prompt the user for a year Read the year
#   if year ≥ 0 then
#     if (year mod 4 = 0 and year mod 100 != 0) or year mod 400 = 0 then
#      Print(“Year is a leap year”)
#     else
#      Print(“Year is not a leap year”)
#   else
#    Tell the user that the year must be ≥ 0 Program finishes

year_in = int(input("Enter a year: "))

if year_in >= 0: 
    if (year_in % 4 == 0 and year_in % 100 != 0) or year_in % 400 == 0:
        print("Year is a leap year")
    else:
        print("Year is not a leap year")
else:
    print("Year must be >= 0")