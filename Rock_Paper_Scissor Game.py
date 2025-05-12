# Ask user to make a choice
# If choice is not valid
#   Print an Error Message
# Let the computer make a choice
# Print the choices of both user and computer (emojis)
# Determine the winner
# Ask the user if  they want to continue
# If not
#   Terminate


#In modules "random", "randint" is to generate random numbers between a range of two distinct numbers.
# But with "choice" we can select a random thing from multiple choices

# Note : To get those emojis
# In MacOS : Press Control (Ctrl) + Command (⌘) + Space bar
# In Windows : Press Windows Key(🪟) + Semicolon Key(;)

import random

# In Dictionary Key -> 'Value'
# 'r' -> "🪨"
# 'p' -> "📃"
# 's' -> "✂️"


#Ask user to make Choice
choices = ("r", "p", "s")
emoji = {'r' : "🪨", 'p' : "📃", 's' : "✂️"}


while True:
# Print Error Message if Choice is Invalid
    user = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    if user not in choices:
        print("Invalid Choice")
        continue

# Let Computer make a choice and print both user and computer's Choices
    computer = random.choice(choices)
    print(f'You Chose {emoji[user]}')
    print(f'Computer Chose {emoji[computer]}')

    #Determining The Winner
    if user == computer:
        print("Tie!")
    elif ((user == 'r' and computer == 's') 
    or (user == 'p' and computer == 'r') 
    or (user == 's' and computer == 'p')):
        print("You win!")
    else:
        print("You lose!")

    #Asking the user if they want to continue
    should_continue = input('Continue? (Y/N): ').lower()
    if should_continue == 'n':
        break