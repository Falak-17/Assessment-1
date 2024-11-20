#Exercise 10:Is it even?
"""#1. The program should ask the user for a number from within the main function.
#2. The entered number should be passed to a function that determines if the value is even or odd.
#3. The function should return a message indicating whether the number is even or odd.
#4. The message returned by the function should be printed from within the main function"""

def check_even_or_odd():
    num=int(input("Enter a number: "))           #asking user to input a number
    if num % 2 == 0:                             #using if-else statement
        print("The number is even")              
    else:
        print("The number is odd")
check_even_or_odd()                              #calling the main function()   
