# HW, 7th, Number Guessing Game

# ask question
print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it!")

# variables
import random
number = random.randint(1,101)
guess = input("What is your guess: ")

# loops
   
while True:
    if guess > number: 
        print("Too high!")
    elif guess < number:
        print("Too low!")
    break