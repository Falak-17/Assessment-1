#Exercise 03: Biography
"""#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single print() statement.
#3. Use variables with appropriate data types for each piece of information"""
#Additional requiremnents 
"""#Have the user input their name, hometown, and age instead of hardcoding the values. 
#Try giving both your first and second name when asked for your name. 
# What happens? How can you handle multiple words in Python? Test the program by entering a string value for age (e.g., "twenty"). 
# What happens? How can you prevent this issue?"""

name= str(input("Enter name: "))          #Asking user to input their name
hometown= str(input("Enter hometown: "))  #Asking user to input their hometown
age= str(input("Enter age: "))            #Asking user to input their age

print(name, hometown, age,sep="\n")       #Printing the entered data on seperate lines  