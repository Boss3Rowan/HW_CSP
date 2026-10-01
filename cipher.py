# HW 7th, Ceasar Cipher



encrypt = input("Whould you like to (E)ncrypt or (D)ecrypt a message? ")
message = input("Enter your message: ")
shift = float(input("Enter your message: "))



for letter in message:
    if letter.isalpha():
        letter = ord(letter)      
        letter += shift
        print(letter)
 