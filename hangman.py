# HW, 7th, Hangman
import random
#Create a list of 10 words on a seperate txt file
# Create another file holds win/loss counts
with open("stats.txt","w") as file:
    stats = file.write("0,0")
# Use split(",") on the content of the words txt document to create your list of words
with open("words.txt", "r") as file:
    words = file.read().split(",")
# Pull win and lose totals from the other txt file and save them as 2 seperate variables
win,loss = stats.split(",")
# Build the hangman game

# Save the correct word as a variable random.choise(name of the list)
  answer = random.choise(list)
# number of wrong guesses --> start at 0
guess == 0
guess += score
# What letters have been guessed --> start []
print(guess)

# Function to display the hangman (needs number of wrong guesses)
"""
    _______
    |     |
    |     O
    |    /|\
    |    / \
    |________
"""
# Function to show the letters and spaces (The correct word, letters that have been guessed)
# Variable for display word (starts as an empty string)
display("")
# Loop over the correct word
    # check if letter has been guessed
    if guess == word:
        guess += display
      # Then add the letter to the display word
    #if they haven't guessed the letter
    elif guess != word:

        #Add an underscore to the display word
#Return the finished display word (outside of the loop)
    return
# Main game loop (While True)
def stupid_proof(guess)
    while True:
        try:
            guess = input("Guess a letter:"))
    # call function to show hangman
    #print function call to show display word
    #create variable and ask user to guess a letter
    #add the letter to list of guessed letters
    #check if not letter in word:
    if not letter in word:
        incorrect += 1
        #increase incorect guesses
    #check if (display word)#call function is same as the word
        #Tell user they won!
    if display == word:
        win += 1
        print("Congradulations! You won!!!")
        print("Would you like to play again?")
        reset
        #increase win total
        #ask if they want to play again
            #reset random word, rest wrong guess count, (guessed letters)
    #Check to see if they lost (if they have 6 wrong guesses)
    if incorrect == 6:
        incorrect += 1
        print("You lost!!")
        print(f"The word was {answer}.")

        #Tell them they lost
        #Tell them what the word was
        #Increase the lost count
        score -= 1
        #ask if they want to play again
        print("Would you like to try again?")

        