# (a) Write a recursive function that takes as its single argument an integer ≥ 0
#     and prints out that number of terms from the above series (Assume that the 0th
#     term is the first term).

def doThing(num):
    if num == 0:
        print("We are at base case 0, return 13")
        return 13
    elif num == 1:
        print("We are at base case 1, return 8")
        return 8
    else:
        res = doThing(num - 2) + 13 * doThing(num - 1)
        print("return {}".format(res))
        return res

def doThingAndPrint(num):
    for i in range(num + 1):
        doThing(i)

# (b) Write a program that prompts the user for a series of integers. For each number
#     entered the program should check that it is greater than or equal to 0. If it is,
#     it calls the function defined in part (a). The program should stop when a negative
#     number is entered.

in_val = 0
while in_val >= 0:
    in_val = int(input("Enter integer: "))
    if in_val >= 0:
        doThingAndPrint(in_val)
print("Finished!")

# (c) In your function, include some print statements that allow you to see the operation
#     of the recursion and its progress towards the base cases.

