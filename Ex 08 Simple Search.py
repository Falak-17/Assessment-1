#Exercise 08: Simple Search
"""#Write a program that searches for a specific string within a list of strings. 
#The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam"."""

names=["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]      #creating list of names
if "Sam" in list(names):                               #checking predefined statement
    print("Name is availabe in the list")              #printing the statement if name is in the list
else:
    print("Name not available in the list")            #printing the statement if name is not in the list