# Write a program that takes an amount (a float), divides the amount in the ratio 60:40, 
# calculates the tax due according to two different tax rates (13.5% on the larger amount 
# and 23% on the smaller) and prints out the total amount (initial amount plus taxes)
# Save this program as p3p3.py.

amt = 232008.36

# higher tax
amt_60 = amt * .6
amt_60_tax_rate = .135
amt_60_tax = amt_60 * amt_60_tax_rate
upper_bracket_total =  amt_60_tax + amt_60
print('upper tax bracket due =', upper_bracket_total)

# lower tax
amt_40 = amt * .4
amt_40_tax_rate = .23
amt_40_tax = amt_40 * amt_40_tax_rate
lower_bracket_total = amt_40_tax + amt_40
print('lower tax bracket due =', lower_bracket_total)

print ('total taxes due:', upper_bracket_total + lower_bracket_total)

