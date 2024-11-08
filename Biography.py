#Exercise 03: Biography
"""#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single print() statement.
#3. Use variables with appropriate data types for each piece of information"""

name= str(input("Enter name: "))          #Asking user to input their name
hometown= str(input("Enter hometown: "))  #Asking user to input their hometown
age= int(input("Enter age: "))            #Asking user to input their age

print(name,hometown,age,sep="\n")         #Printing the enetered data on seperate lines