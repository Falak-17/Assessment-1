#Exercise 03: Biography
"""#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single print() statement.
#3. Use variables with appropriate data types for each piece of information"""

person_info = {"name":"John", "hometown": "New York", "age":21}                                    #creating a dictionary
print(str(person_info["name"]),str(person_info["hometown"]),int(person_info["age"]),sep="\n")      #printing all the values on seperate lines
