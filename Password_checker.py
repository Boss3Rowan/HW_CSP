# HW, 7th, Password Strength Checker Assignment


# variables
password = input("What is your password: ")
characters = False
uppercase = False
lowercase = False
number = False 
symbol = False


if len(password) >= 8:
    characters = True

for letter in password:
    if letter.isupper():
       uppercase = True

for letter in password:
    if letter.islower():
       lowercase = True


for letter in password:
    if letter.isnumeric():
        number = True

if letter in "!?@$#&":
    symbol = True



print(f"At least 8 characters: {characters}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"Your password strength is: {symbol}")
print("To make it strong, add: ")
    