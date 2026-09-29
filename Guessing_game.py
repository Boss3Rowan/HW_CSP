# HW, 7th, Number Guessing Game

# ask question
print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it!")

# variables
import random 
number = random.randint(1,101)
number_of_guesses = 1

# loops
while True:
    guesses = int(input(f"Guess number {number_of_guesses}: "))
    if guesses == number: 
        print("Correct! You win!")
        break
    elif number_of_guesses == 6:
        print(f"Your out of guesses! The number was {number}!")
        break
    elif guesses > number:
        print("Too high!")
    else:
        print("Too low!")
        number_of_guesses += 1
