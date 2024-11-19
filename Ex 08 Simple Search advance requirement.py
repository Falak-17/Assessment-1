#Exercise 08: Simple Search
"""#Write a program that searches for a specific string within a list of strings. 
#The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam"."""
#Additional Requirement
"""#1. Allow the user to input the search term instead of using a predefined value.
#2. Implement the search functionality based on user input."""

names=["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]      #creating list of names
answer=input("Search for a name: ")                    #asking user to input a name
if answer in list(names):                              #checking if the name is in the list
    print("Searched name is in the list")              #printing the statement if name is in the list
else:                                                  
    print("Searched name not in the list")             #printing the statement if name is not in the list