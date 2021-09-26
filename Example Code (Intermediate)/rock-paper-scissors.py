import random

user_wins = 0 # number of wins the user starts off with
computer_wins = 0 # number of wins the computer starts off with

options = ["rock", "paper", "scissors"] # options of what you can choose from at the beginning of the round


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")


    if user_input =="rock" and computer_pick == "scissors": 
        print("You won! :D" )
        user_wins += 1

    elif user_input =="paper" and computer_pick == "rock": 
        print("You won! :D")
        user_wins += 1
    
    elif user_input =="scissors" and computer_pick == "paper": 
        print("You won! :D")
        user_wins += 1

    else:
        print("You lost. :(")
        computer_wins += 1


print("You won", user_wins, "times." )
print("The computer won,", computer_wins, "times.")
print("Goodbye!")
