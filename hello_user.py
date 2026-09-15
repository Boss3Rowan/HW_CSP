# HW, hello user 

while True: 
    name = input("Hello! What's your name?").strip().capitalize()
    if name.isnumeric():
        print("That is a number not your name!")
    else:
        break

print(f"Nice to meet you {name}!")