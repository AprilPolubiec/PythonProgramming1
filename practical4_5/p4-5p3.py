# Write a program that takes as input an amount of income (a float), divides the amount 
# in the ratio 60:40, calculates the tax due according to two different tax rates (23% 
# on the larger amount and 41% on the smaller), and prints out the initial amount, the 
# two different tax amounts, the total tax and the total nett income (initial amount less taxes).
# When the amount is entered by the user, the program should check that it is non-negative. 
# If the amount of income is negative, the message “Amount of income must be >= 0. Please try again.” 
# should be printed out and the program should exit.


income = float(input('Enter amount: '))

if income <= 0:
    print("Amount of income must be >= 0. Please try again.")
    exit()

# higher tax
amt_60 = income * .6
amt_60_tax_rate = .23
amt_60_tax = amt_60 * amt_60_tax_rate
upper_bracket_total =  amt_60_tax + amt_60

# lower tax
amt_40 = income * .4
amt_40_tax_rate = .41
amt_40_tax = amt_40 * amt_40_tax_rate
lower_bracket_total = amt_40_tax + amt_40

print('Initial amount: ', income)
print('Higher tax amount: ', amt_60_tax)
print('Lower tax amount: ', amt_40_tax)
print('Total tax: ', amt_60_tax + amt_40_tax)

print ('Total net income:', income - (amt_60_tax + amt_40_tax))