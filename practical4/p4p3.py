# Write a program that takes as input an amount (a float), 
# divides the amount in the ratio 60:40, calculates the tax 
# due according to two different tax rates (13.5% on the larger 
# amount and 23% on the smaller), and prints out the initial amount, 
# the two different tax amounts, the total tax and the total amount 
# (initial amount plus taxes).

amt = float(input('Enter amount: '))

# higher tax
amt_60 = amt * .6
amt_60_tax_rate = .135
amt_60_tax = amt_60 * amt_60_tax_rate
upper_bracket_total =  amt_60_tax + amt_60

# lower tax
amt_40 = amt * .4
amt_40_tax_rate = .23
amt_40_tax = amt_40 * amt_40_tax_rate
lower_bracket_total = amt_40_tax + amt_40

print('Initial amount: ', amt)
print('Higher tax amount: ', upper_bracket_total)
print('Lower tax amount: ', lower_bracket_total)
print('Total tax: ', amt_60_tax + amt_40_tax)

print ('Total amount due:', upper_bracket_total + lower_bracket_total)
