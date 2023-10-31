# On any given day, a pizza company offers the choice of a certain number of toppings
# for its pizzas. Depending on the day, it provides a fixed number of toppings with
# its standard pizzas. Write a program that prompts the user (the manager) for the
# number of possible toppings and the number of toppings offered on the standard pizza
# and calculates the total number of different combinations of toppings. Recall that
# the number of combinations of k items from n possibilities is given by the formula nCk = n! .

toppings_possible = int(input("Enter number of possible toppings: "))
toppings_on_pizza = int(input("Enter number on a pizza: "))\

numerator = 1
for val in range(toppings_possible):
    numerator *= val + 1

denom_operand_1 = 1
for val in range(toppings_on_pizza):
    denom_operand_1 *= val + 1

denom_operand_2 = 1
for val in range(toppings_possible - toppings_on_pizza):
    denom_operand_2 *= val + 1

total_possibilities = numerator // (denom_operand_1 * denom_operand_2)
print(total_possibilities)