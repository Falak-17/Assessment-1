#Exercise 04:Primitive Quiz
"""#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong."""

capital=str(input("What is the capital of France? "))  #Asking the user to input the answer
if(capital=="paris"):                                  #Checking if the answer is "paris" or not
    print("The answer is correct")                     #Declaring the statement if the answer is correct
else:
    print("The answer is wrong")                       #Declaring the statement if the answer is incorrect