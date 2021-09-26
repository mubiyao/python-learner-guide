import random # Imports the random module in case you couldn't tell.

again = True

while again:
    print(random.randint(1, 6)) # Prints a random number from 1 to 6 like on a dice.
    another_roll = input("Want to roll the dice again? (y/n): ") # Gives the user a choice to roll again which the choices being 'y' for yes and 'n' for no.
    if another_roll.lower() == "y": # If the user inputs "y", repeats the statement and generates another random number from 1 to 6.
        continue # Continues the statment as said in previous line.
    else: # If the user inputs 'n' or anything else, brings the code to a stop.
        break # Ends the program :)
