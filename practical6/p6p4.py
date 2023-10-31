# Write a password checking program to keep track of how many 
# times a user has entered their password incorrectly. Store a 
# password in your program. If the user enters the password incorrectly 
# more than three times, print “You have been denied access.” and 
# terminate the program. If the password is correct, print “You have 
# successfully logged in.” and terminate the program.

# Store correct password as a variable
# Create a counter starting at 0
# While counter is less than 4, keep asking
# If the input is correct in the while code, print message and exit
# otherwise, increment the counter and ask again
# If we make it to the end of the loop without exiting the code, print access denied

password = "MyPassword123"
password_attempt = ""
num_tries = 0

while num_tries <= 3:
    password_attempt = input("Insert password: ")
    if password_attempt != password:
        print("Incorrect. Try again!")
        num_tries += 1
    else:
        print("You have successfully logged in.")
        exit()

print("You have been denied access.")
