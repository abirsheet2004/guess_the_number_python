#Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.
#Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue,
# and his score gets reduced. The clue can be multiples, divisible, greater or smaller, or a combination of all.

import random as rn

def generate_number(low, high):
    #Generates a random number between 'low' and 'high'.
    return rn.randint(low, high)

def get_hint(number, guess):
    #Provides a hint based on the user's guess.
    if guess < number:
        return "The number is greater than your guess."
    elif guess > number:
        return "The number is smaller than your guess."
    else:
        return "Congratulations! You guessed the correct number."

def play_game():
    low = 1  # Define the lower bound of the number range
    high = 100  # Define the upper bound of the number range
    number = generate_number(low, high)
    score = 100  # Starting score

    print(f"Guess a number between {low} and {high}.")
    while True:
        guess = int(input("Enter your guess: "))

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        score -= 10  # Reduce score for each guess
        hint = get_hint(number, guess)
        print(hint)

        if guess == number:
            print(f"Congratulations! You guessed the number. Your score is {score}.")
            break

        if score <= 0:
            print(f"Game over! The number was {number}.")
            break
#Function to start the game
play_game()