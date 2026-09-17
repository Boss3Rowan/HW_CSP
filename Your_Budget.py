# HW, 7th, Your Budget


while True: 
    try:
        income = float(input("What us your monthly income: $"))
        break
    except:
        print("Thats not a number!")
  
while True:
    try:
        rent = float(input("What is your monthly rent: $"))
        break
    except:
        print("That's not a number!")

while True:
    try:
        utilities = float(input("What is your monthly utilities: $"))
        break
    except:
        print("That's not a number!")

while True:
    try:
        groceries = float(input("What is your monthly groceries: $"))
        break
    except:
        print("That's not a number!")

while True:
    try:
        transportation = float(input("What is your monthly transportation: $"))
        break
    except:
        print("That's not a number!")

while True: 
    try:

    smth = str(f"Your utilities are {} and that is {} of your income")