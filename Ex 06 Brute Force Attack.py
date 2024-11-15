#Exercise 06: Brute Force Attack
"""#1.Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered."""

password="$He110$"                          #Declare the password
while password=="$He110$":                  #Using while loop
    password=input("Enter password: ")      #Asking user to input the corrct password
    if password=="$He110$":
       print("Access granted")              #If condition is fulfilled, access granted
       break
    else:
        print("Access denied. Try again!")  #If condition is not fullfilled, access denied