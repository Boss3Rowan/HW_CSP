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

score = 0
if len(password) <2:
    score = 2
else:
    feedback = feedback+()
if len(password) >= 4:
    score = 4

if len(password) == 5:
    score = 5

if score == 2:
    print("Your password strength is: weak")

if score == 4:
    print("Your password strength is: medium")

if score == 5:
    print("Your password strength is: strong")

print("To make it strong, add: ")
    