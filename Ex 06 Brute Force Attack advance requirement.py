#Exercise 06: Brute Force Attack
"""#1.Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered."""
#Additional Requirement
""""#Modify the program to include a maximum of 5 password attempts. 
#If the user enters the wrong password, inform them of the remaining attempts. 
#If the maximum number of attempts is reached, inform the user that the authorities have been alerted."""

max_attempts=5                                           #Declaring maximum 5 number of attempts 
attempt=0
password="$He110$"                                       #Declare the password
while attempt<max_attempts:                              #Using while loop
    password=input("Enter password: ")                   #Asking user to input the corrct password
    if password=="$He110$":
       print("Access granted")                           #If condition is fulfilled, access granted
       break                                             #using break funtion to exit the loop if the password is correct
    else:
      attempt = attempt + 1
      print(attempt,"attempt/s wrong")
      print("Access denied. Try again!")                 #If condition is not fullfilled, access denied
      if(attempt==max_attempts):
         print()                                         #Printing blank line
         print("Maximum number of attempts reached.")    
         print("Authorities have been alerted!!!")       #Printing statement about alerting the authorities