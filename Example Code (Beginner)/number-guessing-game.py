import random # library to import random numbers 'n stuff'
n = random.randint(1,199) # sets up our variable "n" to have a value equal to a number between 1 to 199
guess = int(input("Enter an integer from 1 to 199: ")) # scuffed printing and input method, asks for a number between 1 - 199 to start off the program
while n != "guess": # sets up your guessing method
    print
    if guess < n: # self explanatory with the printing below
        print ("Your number guess is too low!")
        guess = int(input("Enter an integer from 1 to 199: ")) # we use this to ask a number again
    elif guess > n:
        print ("Your number guess was too high") # again, self explanatory
        guess = int(input("Enter an integer from 1 to 199: "))
    else: # "else" is used when a result doesn't satisfy the first if condition, or the elif condition (second if condition)
        print ("You guessed the correct number!")
        break # ends program nicely c:
