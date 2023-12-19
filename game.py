"""A number-guessing game."""

# Put your code here
#print ("hi")

#greet player
#get player name
#choose random number between 1 and 100
#repeat forever:
    #get guess
    #if guess is incorrect:
        #give hint
        #increase number of guesses
    #else:
        #congratulate player


print("Hello")

def get_player_name():
    name = input("What is your name >")
    print(f"Welcome {name}!")

get_player_name()

import random


def play_game():

    secret_number = random.randint(1, 100)
    guess = int 

    guess = input("Guess a number between 1 and 100 >")

    while secret_number != guess:

        if int(guess) > secret_number:
            guess = input("Too high, guess again >")
            
        elif int(guess) < secret_number:
            guess = input("Too low, guess again >")
            
        else:
            int(guess) == secret_number
            print("correct")
            break

    print(f"Shh... the secret number is {secret_number}")

    
play_game()