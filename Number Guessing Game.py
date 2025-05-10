# Generate a Random Number.
# Loop
    # Ask the user to make a guess.
    # If the guess is not a Valid Number
    #   Print an Error Message.
    # If Random Number < Guess Number 
    #   Print "Too Low"
    # If Random Number > Guess Number
    #   Print "Too High"
    #Else
    #   Print "Well Done! Your Guess is Correct."


import random
random_number = random.randint(1, 100)

while True:
    try:
        guess_number = int(input("Guess the Number between 1 and 100: "))
  
        if guess_number < random_number:
            print("Too Low!")
        elif guess_number > random_number:
            print("Too High!")
        else:
            print("Well Done! Your Guess is Correct.")
            break
 
    except ValueError:
        print("Guess a Valid Number")


# Here we have added Exception to avoid Value Error while giving user input.
# We have declared the variable "guess_number" inside the try block.
# So out of that block that variable is invalid.
# Thatswhy we have written condition within the try block.