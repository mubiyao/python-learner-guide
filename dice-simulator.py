import random # imports radom module, which allows for the random methods/functions later-on

again = True # i honestly dont know why..... but just substititue a "True" call for "again" in the code

while again: # while "again" runs:
    print(random.randint(1, 6)) # the program will print a random number from 1-6
    another_roll = input("Want to roll the dice again? (y/n): ") # self explanatory text, asks "y/n" to continue the rolling
    if another_roll.lower() == "y": # if y is pressen then...
        continue # the program continues
    else: # any other key bress will result in...
        break # the program ending.
