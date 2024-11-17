#Exercise 07: Some counting
"""#1. Write a loop that counts up from 0 to 50 in increments of 1.
#2. Write a loop that counts down from 50 to 0 in decrements of 1.
#3. Write a loop that counts up from 30 to 50 in increments of 1.
#4. Write a loop that counts down from 50 to 10 in decrements of 2.
#5. Write a loop that counts up from 100 to 200 in increments of 5. You may include all loops in a single project"""

#1.
a=0
for a in range(51):             #using range to generate numbers from 0 to 50
 print(a)                    #output the loop of numbers

print()                         #printing blank space to seperate outputs of different codes 

#2.
for b in range(50,-1,-1):       #using range to generate numbers from 50 to 0 with decrement of 1
    print(b)                    #output the loop of numbers

print()                         #printing blank space to seperate outputs of different codes 

#3.
for c in range(30,51):          #using range to generate numbers from 30 to 50 with increment of 1
    print(c)                    #output the loop of numbers

print()                         #printing blank space to seperate outputs of different codes 

#4.
for d in range(50,9,-2):        #using range to generate numbers from 50 to 10 with decrement of 2
    print(d)                    #output the loop of numbers

print()                         #printing blank space to seperate outputs of different codes

#5.
for e in range(100,201,+5):     #using range to generate numbers from 100 to 200 with increment of 5
    print(e)                    #output the loop of numbers