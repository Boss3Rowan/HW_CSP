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

for letter in password:
    if letter in "!?@$#&":
        symbol = True



print(f"At least 8 characters: {characters}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")

# score
score = 0
if characters:
    score += 1

if uppercase:
    score += 1
    
if lowercase:
    score += 1

if number:
    score += 1

if symbol:
    score += 1
   
# strength
if score >= 2:
    print("Your password strength is: weak")
elif score <= 4:
    print("Your password strength is: medium")
else:
    print("Your password strength is: strong")

# Feedback
print("To make it stronger, add: ")

if not characters:
    print("- At least 8 characters")

if not uppercase:
    print("- An uppercase letter")

if not lowercase:
    print("- A lowercase letter")

if not number:
    print("- A number")

if not symbol:
    print("- A symbol")
