import random # random module used AGAIN!

def even_odd(choice, fingers): # defines choice and fingers
    human_choice = choice # human choice will be substitued for choice in the rest fo the program
    human_fingers = fingers # i.... really don't know
    if human_choice == "Even": # if the human chooses even, the computer chooses odd
        computer_choice = "Odd"
    else:
        computer_choice = "Even" # if the human choice is odd, the computer chooses even
    computer_finger = random.randint(0,10) # computer chooses what number using a randint generator
    total = human_fingers + computer_finger # the winner is decided by the total of the computers fingers and the players fingers.
    if total % 2 ==0: # if the total is divisible by two, its even (basic math rule)
        results = "Even"
    else:
        results = "Odd" # if its anything else (not divisible by 2) then it is odd
    if human_choice == results: # if human wins, print winning message
        print ("You Won! c:")
    else: # if anything other than a win, then print loss message
        print ("You Lose... The computer outsmarted you :c")
        

even_odd("Odd", 5) # round input
