# Write a program that takes as input a string and checks whether
# the string entered is the name of a town or city known to the
# program. The towns and cities should include: Dublin, Belfast,
# Cork, Limerick, Derry, Galway, Lisburn, Kilkenny, Waterford and
# Sligo. If the name of one of these towns or cities is entered,
# the program should print out the string “You entered x. x is in y.”,
# where x is the name of the town or city and y is the province (Ulster,
# Munster, Leinster or Connacht) in which the town or city is situated.
# If the string entered is not recognised, the message “Sorry, I didn’t
# recognise that name.” should be printed out.

towns_ulster = ["Belfast", "Derry", "Lisburn"]
towns_munster = ["Cork", "Waterford", "Limerick"]
towns_leinster = ["Dublin", "Kilkenny"]
towns_connacht = ["Galway", "Sligo"]

text_in = input("Enter a town or city: ")

def check_town(town_to_check, town_list, province_name):
    for town in town_list:
        if town_to_check.lower() == town.lower():
            print(f"You entered {town}. {town} is in {province_name}.")
            exit()


check_town(text_in, towns_ulster, "Ulster")
check_town(text_in, towns_munster, "Munster")
check_town(text_in, towns_leinster, "Leinster")
check_town(text_in, towns_connacht, "Connacht")

print("Sorry, I didn’t recognise that name.")
