#Exercise 04:Primitive Quiz advanced requirements
"""#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong."""
#Additional Requirements
"""#Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct). 
#Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries.
#Provide feedback for each question."""

#Creating a dictionary
country = {"France": "Paris",
"Germany": "Berlin",
"Italy": "Rome",
"Austria": "Vienna",
"Denmark": "Copenhagen",
"United Kingdom": "London",
"Ireland": "Dublin",
"Greece": "Athens",
"Norway": "Oslo",
"Hungary": "Budapest"}

score = 0                                                             #original score is zero
total_questions = len(country)
for country, capital in country.items():                              #using for loop
    answer = input(f"What is the capital of {country}? ").strip()     #asking user to input the capitals for each country
    if answer.capitalize() == capital.capitalize():                   #ignoring the capitalizations
        print("Correct!")
        score += 1                                                    #adding a score if answer is correct
        print()                                                       #printing a blank line 
    else:
        print(f"Wrong! The capital of {country} is {capital}.")
        print()                                                       #printing a blank line
print(f"\nScore: {score}/{total_questions}")                          #printing the scores
