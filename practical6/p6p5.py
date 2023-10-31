# Ask the user to enter a password. If the password is correct 
# (ie it matches the password stored in the program), print 
# “You have successfully logged in.” and terminate the program. 
# If the password is wrong print “Sorry, the password is wrong.” 
# and ask the user to enter the password three times. If the user 
# enters the correct password three times, print “You have successfully 
# logged in.” and terminate the program; otherwise print “You have 
# been denied access.” and terminate the program.

# Store correct password as a variable
# Ask for password
# If its correct, ouput and close
# if its incorrect, create a counter starting at 0
# While counter is less than 3...
#   Ask for the password
#     if the password is wrong...
#       print access denied
#       short circuit out - its impossible for them to get 3 correct
#    if the password is correct
#       increment the counter
# Once the loop is finished, print success

password = "MyPassword123"
attempt = input("Enter password: ")
if attempt == password:
    print("You have successfully logged in.")
    exit()

print("Incorrect - enter the correct password 3 times to proceed")
counter = 0
while counter < 3:
    attempt = input("Enter password: ")
    if attempt == password:
        counter += 1
    else:
        print("You have been denied access.")
        exit()

print("You have successfully logged in")