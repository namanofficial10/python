#Snake, Water, Gun game

import os


def winCheck(p1,p2):
    if p1 == p2:
        return 0
    elif p1=='s':
        if p2 == 'w':
            return 1
        elif p2 == 'g':
            return 2
    elif p1=='w':
        if p2 == 'g':
            return 1
        elif p2 == 's':
            return 2
    elif p1=='g':
        if p2 == 's':
            return 1
        elif p2 == 'w':
            return 2

    



s1 = 0
s2 = 0
t = 0

name1 = input("Enter the name of Player 1:")
name2 = input("Enter the Name of Player 2:")
game = "Y"

while game=='Y':
    os.system('cls')
    tg=s1+s2+t
    print(f"Current Score:\t{name1}: {s1}\t{name2}: {s2}\tTie: {t}\tTotal Games: {tg}")
    print("Please Enter your choice: Snake(s), Water(w) & Gun(g)")

    i = True
    while i:
        a=input(f"{name1}'s Turn:")
        if(a=='w' or a=='s' or a=='g'):
            i=False
        else:
            os.system('cls')
            print("Please Enter a Valid Choice.")
            print("Please Enter your choice: Snake(s), Water(w) & Gun(g)")


    os.system('cls')

    print("Please Enter your choice: Snake(s), Water(w) & Gun(g) ")



    i=True
    while i:
        b=input(f"{name2}'s Turn:")
        if(b=='w' or b=='s' or b=='g'):
            i=False
        else:
            os.system('cls')
            print("Please Enter a Valid Choice.")
            print("Please Enter your choice: Snake(s), Water(w) & Gun(g) ")

    win = winCheck(a,b)



    os.system('cls')

    if win == 0:
        print("There is a tie.")
        t += 1
    elif win == 1:
        print("Player 1 Wins.")
        s1 += 1
    else:
        print("Player 2 Wins.")
        s2 += 1

    print("Do you wish to play again:")
    game=input("Y for Yes and N for No:")

os.system('cls')

print(f"Final Score is: \t{name1}: {s1}\t{name2}: {s2}\tTie: {t}\tTotal Games: {tg}")
print("Thanks For Playing!")
print("Author: Naman")
