#Random Number guess Game

import random
import os

def check(num,ran):
    if num>ran:
        return 1
    elif num<ran:
        return -1
    elif num == ran:
        return 0


choice = 'y'
while choice == 'Y' or choice == 'y':
    os.system('cls')
    g1 = True
    n = 0
    ran = random.randrange(1, 21)
    while g1:
        print("Guess a Number between 1 to 20!")
        a = int(input("Enter a Number:"))
        n += 1

        os.system('cls')

        chk = check(a,ran)

        if chk == 0:
            print("Congrats you got right number!")
            print(f"You used {n} attemps to guess the correct number!")
            g1 = False
        elif chk == 1:
            print("Enter a lower number please!")
        elif chk == -1:
            print("Enter a higher number please!")

    print("Want to Play Again?")
    choice = input("Yes(Y) or No(N):") 

os.system('cls')
print("Thanks For Playing!")
print("Author: Naman")
