# HW, 7th, Number Information

for number in range(1,21):
    if number % 2 == 0:
        if number % 5 == 0:
            print(f"{number} is even and divisible by five :)")
        else:
            print(f"{number} is even and not divisible by five :(")
    else:
        if number % 5 == 0:
            print(f"{number} is odd and divisable by 5 :)")
        else: 
            print(f"{number} is odd and not divisible by 5 :(")
