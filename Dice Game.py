#Loop
    # Ask: Roll the dice?
    # If user enters Y
    #   Generate two random numbers
    #   Print "those two random numbers"
    # elif user enters N
    #   Print "Message: Thankyou!"
    #   Terminate
    # Else
    #   Print "Error message: Invalid Choice"

import random   

while True:     
    choice = input('Roll the dice? (Y/N): ').lower()   
    if choice == 'y':
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        print(f'({die_1},{die_2})')
    elif choice == 'n':
        print('Thankyou for playing!') 
        break
    else:
        print('Invalid Choice')

#Line-13: Here we import "random" module, which is necessary for generating random numbers.
#Line-15: This creates an infinite loop, allowing user to roll the dice multiple times until they quit.
#Line-16: Here we use "lower()" function because we may give input in lowercase or uppercase.
#It will be converted to lowercase itself without getting error.
#Line 20: Prints the result of the dice roll in tuple format
