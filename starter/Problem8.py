### Problem-8: Guessing game
#Write a function that takes a number 1 to 9 from the user input (use input function inside a function).
#  Store a number in a variable (let’s assume 6). 
# If the input value is less than the variable, print (your guess is almost there), 
# if the input value is greater than the variable, print - your guess is higher, 
# if the input value and variable are equals, print - Your Guess Is Correct!
def guessing_game():
    secret_number = 6
    user_input = int(input("Guess a number between 1 and 9: "))
    
    if user_input <1 or user_input>9:
        print("Please enter a number between 1 and 9")
        return
    

    if user_input < secret_number:
        print("Your guess is almost there")
    elif user_input > secret_number:
        print("Your guess is higher")
    else:
        print("Your Guess Is Correct!")


guessing_game()