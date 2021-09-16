import random # library to import random numbers 'n stuff'
n = random.randint(1,199) # sets up our variable "n" to have a value equal to a number between 1 to 199
guess = int(input("Enter an integer from 1 to 199: ")) # scuffed printing and input method, asks for a number between 1 - 199 to start off the program
while n != "guess": #
    print
    if guess < n:
        print ("Your number guess is too low!")
        guess = int(input("Enter an integer from 1 to 199: "))
    elif guess > n:
        print ("Your number guess was too high")
        guess = int(input("Enter an integer from 1 to 199: "))
    else:
        print ("You guessed the correct number!")
        break
