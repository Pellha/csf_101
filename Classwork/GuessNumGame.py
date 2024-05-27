# importing the random module
import random
# generate a random number between 1 and 10
secret_number = random.randint(1, 10)
# maximum attempys allowed
max_attempts = 3
# function to display a welcome message
def welcome_message():
        print("\nWelcome to tje Number Guessing Game!")
        print(f"you have {max_attempts} attempts to guess the correct number.")
# func for recursive guessing 
def guess_recursive(attempts_left):
        # get user input
        guess = int(input("\nguess the number between (1 and 10): "))
        # check if the guess is correct 
        if guess == secret_number:
                print("congratulation! you guess the correct number!")
        else:
                print(f"wrong guess. attempt left {attempts_left-1}")
                if attempts_left > 1:
                        # make a recursive call for another guess
                        guess_recursive(attempts_left - 1)
                else:
                        print(f"\nsorry, you couldn't guess the number. The correct number was {secret_number}.")
                # calling the func
                welcome_message()
                guess_recursive(max_attempts)
                # using id() to get memory address
                print(f"memory address of secret number {secret_number} is: {id(secret_number)}")