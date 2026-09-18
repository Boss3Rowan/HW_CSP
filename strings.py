# HW 7th, Strings Notes

# string => any saved inside of quotation marks "" '' 

name = input("What is your name: ").strip().capitalize()

age = input('How old are you: ')
print(type(age))

# Concatenation => puts two strings directly next to each other
print(age+age)

print(name + " " + "LaRose")

#
sentance = "The quick brown fox jumped over the lazy dog."

print(sentance)
print(sentance.replace("dog", "monkey"))
print(len(name)) #<= gets the length of a string
print(f"Your name is {name} that is {len(name)} letters long. Your first initial is {name[0]} I think I will call you {name[0:3]}")