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


print(f"Your rent is ${rent:.2f} and that is {int(rent/income*100)}% of your income.")

print(f"Your utilities are ${utilities:.2f} and that is {int(utilities/income*100)}% of your income.")

print(f"Your groceries are ${groceries:.2f} and that is {int(groceries/income*100)}% of your income.")

print(f"Your transportation is ${transportation:.2f} and that is {int(transportation/income*100)}% of your income.")

print(f"You should save ${income/10:.2f} a month, that is 10% of your income.")

print(f"You have ${income-rent-utilities-groceries-transportation-income/10:.2f} of spending money each month!")