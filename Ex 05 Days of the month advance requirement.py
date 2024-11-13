#Exercise 05: Days of the month
"""#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month."""
#Additional Requirement
"""#Leap Year Adjustment: Modify the program to account for leap years. 
#For February, ask the user if the year is a leap year and adjust the number of days accordingly"""

#Creating a dictionary
month_days={
1:31,
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

year=int(input("Input a year: "))                           #asking user to input a year

#using if-else statement
if year%4==0:                                               #leap year
    print("Leap Year")
    num=int(input("Enter a number from(1-12): "))           #asking user to input a month's number 
    if num in month_days:
      print(f'{month_days[num]}',"days")
    else:
       print("Invalid number")
else:                                                       #Not a leap year
    print("Not a Leap Year")
    num=int(input("Enter a number from(1-12): "))           #asking user to input a month's number
    if (num==2):
       print("28 days")
    elif(num==1 or num<=12):
       print(f'{month_days[num]}',"days")
    else:
       print("Invalid number")