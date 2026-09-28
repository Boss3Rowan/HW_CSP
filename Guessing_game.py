# HW, 7th, Number Guessing Game

# ask question
print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it!")

# variables
import random
number = random.randint(1,101)
guess = input("Guess #1: ")
guess2 = input("Guess #2: ")
guess3 = input("Guess #3: ")
guess4 = input("Guess #4: ")
guess5 = input("Guess #5: ")
guess6 = input("Guess #6: ")

# loops
while True:
    if guess > number: 
        print("Too high!")
    elif guess < number:
        print("Too low!")
    elif guess == number:
        print(f"Correct! You guessed it in tries!")
    else:
        break 


while True:
    if guess2 > number: 
        print("Too high!")
    elif guess2 < number:
        print("Too low!")
    elif guess2 == number:
        print(f"Correct! You guessed it in tries!")
    else:
        break 

while True:
    if guess3 > number: 
        print("Too high!")
    elif guess3 < number:
        print("Too low!")
    elif guess3 == number:
        print(f"Correct! You guessed it in tries!")
    else:
        break 

while True:
    if guess4 > number: 
        print("Too high!")
    elif guess4 < number:
        print("Too low!")
    elif guess4 == number:
        print(f"Correct! You guessed it in tries!")
    else:
        break 

while True:
    if guess5 > number: 
        print("Too high!")
    elif guess5 < number:
        print("Too low!")
    elif guess5 == number:
        print(f"Correct! You guessed it in tries!")
    else:
        break 

while True:
    if guess6 > number: 
        print("Too high!")
    elif guess6 < number:
        print("Too low!")
    elif guess6 == number:
        print(f"Correct! You guessed it in tries!")
    else:
        break 

    print(f"You're out of guesses! The number was {number}.")
