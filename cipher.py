# HW 7th, Ceasar Cipher

letters = 'abcdefghijklmnopqrstuvwxyz'

encrypt = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()
message = input("Enter your message: ").strip()
shift = int(input("Enter a shift amount: "))
word = ""

if str(encrypt) == "E":

    for letter in message:
        if letter.isalpha():
            letter = ord(letter)
            letter += shift
            letter = chr(letter)
            word = word + letter

elif str(encrypt) == "D":

    for letter in message:
        if letter.isalpha():
            letter = ord(letter)
            letter -= shift
            letter = chr(letter)
            word = word + letter

else:
    print("Try again")

print(word)