## Write a recursive function that takes as its single argument an integer ≥ 1 and prints out that number of terms from the above series.

def series(value: int, s: list) -> int:
    """Function that executes the series in practical 16.1

    Args:
        value (int): an integer >= 1
        s (list<int>): $value's that have been seen so far; passed by reference

    Returns:
        int: value at the $value'th location
    """
    print("series({})".format(value))
    ## Base case
    if value == 1:
        s[value - 1] = 2
        print("BASE: return 2")
        return 2
    else: ## Run the recursion
        res = 2 * series(value - 1, s)
        s[value - 1] = res
        print("return {}".format(res))
        return res

# Write a program that prompts the user for a series of integers. For each number entered the
# program should check that it is greater than or equal to 1. If it is, it calls the function
# defined in part (a). The program should stop when a zero or a negative number is entered.

in_val = 1
while in_val >= 1:
    in_val = int(input("Enter int: "))
    if in_val >= 1:
        l = list(range(in_val))
        series(in_val, l)
        print(l)
