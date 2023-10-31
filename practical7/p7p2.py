# Write a program that prompts the user for a year and checks whether 
# the year is a leap year. Use the algorithm on the Wikipedia page 
# (also mentioned in Lecture 8).

# if (year is not exactly divisible by 4) then (it is a common year) else
# if (year is not exactly divisible by 100) then (it is a leap year) else
# if (year is not exactly divisible by 400) then (it is a common year) else (it is a leap year)

year_in = int(input("Enter a year: "))

if year_in % 4 != 0:
    print("Not a leap year")
elif year_in % 100 != 0:
    print("It is a leap year!")
elif year_in % 400 != 0:
    print("Not a leap year")
else:
    print("It is a leap year!")