# (a) Write a recursive function that takes as its single argument an integer ≥ 1
#     and prints out that number of terms from the above series.

def doThing(num):
    if num == 1:
        print("We are at base case, return 1")
        return 1
    else:
        res = doThing(num - 1) + 2**(num - 1)
        print("return {}".format(res))
        return res

def doThingAndPrint(num):
    for i in range(1, num):
        doThing(i)

# (b) Write a program that prompts the user for a series of integers. For each number
#     entered the program should check that it is greater than or equal to 1. If it is, it
#     calls the function defined in part (a). The program should stop when a zero or a
#     negative number is entered.

in_val = 1
while in_val >= 1:
    in_val = int(input("Enter integer: "))
    if in_val >= 1:
        doThingAndPrint(in_val)
print("Finished!")

# (c) In your function, include some print statements that allow you to see the operation
#     of the recursion and its progress towards the base case.