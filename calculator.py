import random
import time
from os import system, name
import periodictable as pd
import time

ab_num = 6.02e23
mol_liter = 22.4

print("""
            _____      _            _       _              ____   _____ 
           / ____|    | |          | |     | |            / __ \ / ____|
          | |     __ _| | ___ _   _| | __ _| |_ ___  _ __| |  | | (___  
          | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__| |  | |\___ \ 
          | |___| (_| | | (__| |_| | | (_| | || (_) | |  | |__| |____) |
           \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   \____/|_____/ 
""")
print(".")
time.sleep(random.random() * 1.5)
print(".")
time.sleep(random.random() * 1.5)
print(".")
time.sleep(random.random() * 1.5)
print("")

def get_input():
    cmd = input("::: ")
    if cmd == "a" or cmd == "A" or cmd == "add" or cmd == "addition" or cmd == "+":
        x = float(input("Num 1: "))
        y = float(input("Num 2: "))
        print(x + y)
        print("")
        get_input()
    elif cmd == "s" or cmd == "S" or cmd == "subtraction" or cmd == "subtract" or cmd == "-":
        x = float(input("Num 1: "))
        y = float(input("Num 2: "))
        print(x - y)
        print("")
        get_input()
    elif cmd == "d" or cmd == "D" or cmd == "divide" or cmd == "division" or cmd == "/" or cmd == "\\":
        x = float(input("Num 1: "))
        y = float(input("Num 2: "))
        z1 = int(x / y)
        z2 = float(x / y)
        a = int(x % y)
        print(str(z2) + " or " + str(z1) + " r" + str(a))
        print("")
        get_input()
    elif cmd == "m" or cmd == "M" or cmd == "multiply" or cmd == "multiplication" or cmd == "*":
        x = float(input("Num 1: "))
        y = float(input("Num 2: "))
        print(x * y)
        print("")
        get_input()
    elif cmd == "dance":
        print("(づ◕‿◕)づ")
        print("dasda")
        print("")
        get_input()
    elif cmd == "h" or cmd == "help":
        print('''Commands:
h - help
dance - do a lil dance :)
rng - Random number generator

Operators: 
a - add
s - subtract
d - divide
m - multiply

Chemistry: 
mm - calculate molar mass of element
gf - grams to F.U
fg - F.U to grams
lf - liters to F.U
fl - F.U to liters
lg - liters to grams
gl - grams to liters

Load:
1 - Guessing game
2 - Coin flip
3 - Dice roll
        ''')
        get_input()
    elif cmd == "l" or cmd == "L" or cmd == "load":
        print("What game would you like to load?")
        x = input(":/: ")
        print("")
        if x == "1":
            print("Guessing game!")
            fr = int(input("From: "))
            to = int(input("To: "))
            print("")
            y = random.randint(fr, to)
            print("Okay, choose a number between " + str(fr) + " and " + str(to) + "!")
            inp = int(input(":/: "))
            if inp == y and inp >= fr and inp <= to:
                print("Correct! You win!")
                print("")
                get_input()
            elif inp != y and inp >= fr and inp <= to:
                print("You lose!")
                print("")
                get_input()
            else:
                print("Invalid number, you lose!")
                print("")
                get_input()
        elif x == "2":
            print("Coin toss!")
            print("O - Heads  0 - Tails")
            print("")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            print(".")
            print("")
            time.sleep(0.2)
            coin = random.randint(1, 100)
            if coin >= 2:
              print("0")
              print("")
              print("Heads!")
              print("")
            elif coin == 1:
              print("|")
              print("")
              print("...Side?!")
              print("")
            else:
              print("O")
              print("")
              print("Tails!")
              print("")
            get_input()
        elif x == "3":
                delay = input("Press enter to roll the dice!")
                rand = random.randint(1, 6)
                if rand == 1:
                    print('''
 _______
/       \\
|   O   |
\\_______/''')
                    print("")
                    get_input()
                elif rand == 2:
                    print('''
 _______
/     O \\
|       |
\\_O_____/''')
                    print("")
                    get_input()
                elif rand == 3:
                    print('''
 _______
/     O \\
|   O   |
\\_O_____/''')
                    print("")
                    get_input()
                elif rand == 4:
                    print('''
 _______
/ O   O \\
|       |
\\_O___O_/''')
                    print("")
                    get_input()
                elif rand == 5:
                    print('''
 _______
/ O   O \\
|   O   |
\\_O___O_/''')
                    print("")
                    get_input()
                elif rand == 6:
                    print('''
 _______
/ O   O \\
| O   O |
\\_O___O_/''')
                    print("")
                    get_input()
                else:
                    print("wtf how did you even do that???")
                    print("")
                    get_input()
    elif cmd == "rng" or cmd == "RNG":
        x = input("From: ")
        y = input("To: ")
        z = random.randint(int(x), int(y))
        print(str(z))
        print("")
        get_input()
    elif cmd == "mm" or cmd == "MM" or cmd == "mass":
        x = input("Element (symbol and first letter capitalized): ")
        y = input("How many of this element: ")
        if x == "H":
            x = pd.H.mass
            elemass = float(x) * float(y)
            name = "H"
        elif x == "He":
            x = pd.He.mass
            elemass = float(x) * float(y)
            name = "He"
        elif x == "Li":
            x = pd.Li.mass
            elemass = float(x) * float(y)
            name = "Li"
        elif x == "Be":
            x = pd.Be.mass
            elemass = float(x) * float(y)
            name = "Be"
        elif x == "B":
            x = pd.B.mass
            elemass = float(x) * float(y)
            name = "B"
        elif x == "C":
            x = pd.C.mass
            elemass = float(x) * float(y)
            name = "C"
        elif x == "N":
            x = pd.N.mass
            elemass = float(x) * float(y)
            name = "N"
        elif x == "O":
            x = pd.O.mass
            elemass = float(x) * float(y)
            name = "O"
        elif x == "F":
            x = pd.F.mass
            elemass = float(x) * float(y)
            name = "F"
        elif x == "Ne":
            x = pd.Ne.mass
            elemass = float(x) * float(y)
            name = "Ne"
        elif x == "Na":
            x = pd.Na.mass
            elemass = float(x) * float(y)
            name = "Na"
        elif x == "Mg":
            x = pd.Mg.mass
            elemass = float(x) * float(y)
            name = "Mg"
        elif x == "Al":
            x = pd.Al.mass
            elemass = float(x) * float(y)
            name = "Al"
        elif x == "Si":
            x = pd.Si.mass
            elemass = float(x) * float(y)
            name = "Si"
        elif x == "P":
            x = pd.P.mass
            elemass = float(x) * float(y)
            name = "P"
        elif x == "S":
            x = pd.S.mass
            elemass = float(x) * float(y)
            name = "S"
        elif x == "Cl":
            x = pd.Cl.mass
            elemass = float(x) * float(y)
            name = "Cl"
        elif x == "Ar":
            x = pd.Ar.mass
            elemass = float(x) * float(y)
            name = "Ar"
        elif x == "K":
            x = pd.K.mass
            elemass = float(x) * float(y)
            name = "K"
        elif x == "Ca":
            x = pd.Ca.mass
            elemass = float(x) * float(y)
            name = "Ca"
        elif x == "Sc":
            x = pd.Sc.mass
            elemass = float(x) * float(y)
            name = "Sc"
        elif x == "Ti":
            x = pd.Ti.mass
            elemass = float(x) * float(y)
            name = "Ti"
        elif x == "V":
            x = pd.V.mass
            elemass = float(x) * float(y)
            name = "V"
        elif x == "Cr":
            x = pd.Cr.mass
            elemass = float(x) * float(y)
            name = "Cr"
        elif x == "Mn":
            x = pd.Mn.mass
            elemass = float(x) * float(y)
            name = "Mn"
        print("The molar mass of " + str(name) + str(y) + " is " + str(round(elemass, 4)) + " grams.")
        print("")
        get_input()
    elif cmd == "gf" or cmd == "GF":
        x = input("Number of grams: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / float(y) * ab_num
        print(round(z, 5))
        print("")
        get_input()
    elif cmd == "fg" or cmd == "FG":
        x = input("Number of F.U: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / ab_num * float(y)
        print(round(z, 7))
        print("")
        get_input()
    elif cmd == "lf" or cmd == "LF":
        x = input("Number of liters: ")
        z = float(x) / mol_liter * ab_num
        print(round(z, 7))
        print("")
        get_input()
    elif cmd == "fl" or cmd == "FL":
        x = input("Number of F.U: ")
        z = float(x) / ab_num * mol_liter
        print(round(z, 7))
        print("")
        get_input()
    elif cmd == "lg" or cmd == "LG":
        x = input("Number of liters: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / mol_liter * float(y)
        print(round(z, 7))
        print("")
        get_input()
    elif cmd == "gl" or cmd == "GL":
        x = input("Number of grams: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / float(y) * mol_liter
        print(round(z, 7))
        print("")
        get_input()
    else:
        print("Invalid command.")
        print("")
        get_input()

get_input()
