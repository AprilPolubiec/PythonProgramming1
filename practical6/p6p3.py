# Write a program that asks the user their name. If they enter 
# your name, print “That is a cool name!” If they enter “Mickey Mouse” 
# or “Spongebob Squarepants”, tell them that you are not sure that that 
# is their name. Otherwise, tell them “You have a nice name.” The program 
# should then terminate.

# Ask user for name
# Check if name == "April"
# If yes, print "That is a cool name!"
# else if its mickey mouse OR Spongebob Squarepants, print "I'm not sure thats your name"
# else, tell them they have a nice name

name = input("What is your name? ")
if name == "April":
    print("That is a cool name!")
elif name == "Mickey Mouse" or name == "Spongebob Squarepants":
    print("I'm not sure that is your name...")
else:
    print("You have a nice name.")
