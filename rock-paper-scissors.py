import random

user_wins = 0 # The amount of wins the player starts with at the beginning of the game.
computer_wins = 0 # The amount of wins the computer starts with at the beginning of the game.

options = ["rock", "paper", "scissors"] # The options that the player and computer can choose from at the start of the game.


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options: # If the user types in something which is not in the options, then it stops the code.
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number] # Computer picks random number which is either 0, 1 or 2 which translates to rock, paper, or scissors.
    print("Computer picked", computer_pick + ".") # Prints what the computer picked.


    if user_input =="rock" and computer_pick == "scissors": # If the user picks rock and the computer picks scissors, prints "You won"
        print("You won! :D" )
        user_wins += 1 # Adds 1 to the user_wins category.

    elif user_input =="paper" and computer_pick == "rock": # If the user picks paper and the computer picks rock, prints "You won"
        print("You won! :D")
        user_wins += 1 # Adds 1 to the user_wins category.
    
    elif user_input =="scissors" and computer_pick == "paper": # If the user picks scissors and the computer picks paper, prints "You won"
        print("You won! :D")
        user_wins += 1 # Adds 1 to the user_wins category.

    else:
        print("You lost. :(") # If it is a different outcome then the 3 if statements above, then prints "You lost"
        computer_wins += 1 # Adds 1 to the computer_wins category.


print("You won", user_wins, "times." ) # When the code ends, prints how many times the user won.
print("The computer won,", computer_wins, "times.") # When the code ends, prints how many times the computer won.
print("Goodbye!") # Simply prints goodbye to end the code off nicely.
