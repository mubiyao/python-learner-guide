import random # imports the random module

def even_odd(choice, fingers): # choice is whether its even or odd and fingers is the number
    human_choice = choice # human_choice is whether its odd or even.
    human_fingers = fingers # human_fingers is what number they chose from 1 to 10.
    if human_choice == "Even": # if the human choice is even, the computer choice must be odd.
        computer_choice = "Odd"
    else:
        computer_choice = "Even" # if the human choice is odd, the computer choice must be even.
    computer_finger = random.randint(0,10) # the computers choice of what number it will be. Could be odd or even ranging from 1 to 10 depending on what the player picked.
    total = human_fingers + computer_finger # the winner is decided by the total of the computers fingers and the players fingers.
    if total % 2 ==0: # results are even if statement appears true.
        results = "Even"
    else:
        results = "Odd" # results are odd if the ststement above appears to be something else. 
    if human_choice == results: # if the human choice is even, prints 'You won' as below.
        print ("Yay! You won! :D")
    else: # if the human choice is something other than even, prints 'You lost' as below.
        print ("You lost. The computer wins. :(")
        

even_odd("Odd", 5) # where the player inputs their choices for each round.
