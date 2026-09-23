# HW, 7th, Password Strength Checker Assignment


# variables
password = input("What is your password: ")
characters = False
uppercase = False
lowercase = False
number = False 
symbol = False


for letter in password:
    if(len(password)) >= 8:
        characters = True 
    print("At least 8 characters: ")

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

if password is strong:
    print("Good job!")
else:
    print("To make it strong, add: ")
    