#Exercise 03: Biography
"""#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single print() statement.
#3. Use variables with appropriate data types for each piece of information"""
#Additional requiremnents 
"""#Have the user input their name, hometown, and age instead of hardcoding the values. 
#Try giving both your first and second name when asked for your name. 
# What happens? How can you handle multiple words in Python? Test the program by entering a string value for age (e.g., "twenty"). 
# What happens? How can you prevent this issue?"""

name=str(input("Enter your name: "))                                                #asking user to input their name
hometown=str(input("Enter your hometown: "))                                        #asking user to input their homwtown
age=str(input("Enter your age: "))                                                  #asking user to input their age
person_info = {"name":name, "hometown": hometown, "age":age}                        #creating a dictionary
print(person_info["name"],person_info["hometown"],person_info["age"],sep="\n")      #printing all the values on seperate lines
