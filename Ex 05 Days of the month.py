#Exercise 05: Days of the month
"""#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month."""

#Creating a dictionary
months={1:31,
2:29,
3:31,
4:30,
5:31,
6:30,
7:31,
8:31,
9:30,
10:31,
11:30,
12:31}   
num=int(input("Enter a month's number: "))                                #asking user to input a month's number
if num in months:                                                         #using if-else statement
    print(months[num],"days")                                             #printing number of days if defined in the dictionary
else:
    print("Invalid")                                                      #printing message of number being invalid/not in the dictionary