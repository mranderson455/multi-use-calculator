import random
import time
from os import system, name
import periodictable as pd
import time

ab_num = 6.02e23
mol_liter = 22.4

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
        print("")
        get_input()
    elif cmd == "h" or cmd == "help":
        print('''Commands:
h - help
dance - do a lil dance :)

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
        if x == "2":
            print("Coin toss!")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            print("   .")
            time.sleep(0.2)
            print("       .")
            time.sleep(0.2)
            print("   .")
            time.sleep(0.2)
            print(".")
            coin = random.randint(1, 2)
            if coin == 1:
              print("Heads!")
              print("")
            else:
              print("Tails!")
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
        print("The molar mass of " + str(name) + str(y) + " is " + str(round(elemass, 4)) + " grams.")
        print("")
        get_input()
    elif cmd == "gf" or cmd == "GF":
        x = input("Number of grams: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / float(y) * ab_num
        print(round(z, 5))
        print("")
    elif cmd == "fg" or cmd == "FG":
        x = input("Number of F.U: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / ab_num * float(y)
        print(round(z, 7))
        print("")
    elif cmd == "lf" or cmd == "LF":
        x = input("Number of liters: ")
        z = float(x) / mol_liter * ab_num
        print(round(z, 7))
        print("")
    elif cmd == "fl" or cmd == "FL":
        x = input("Number of F.U: ")
        z = float(x) / ab_num * mol_liter
        print(round(z, 7))
        print("")
    elif cmd == "lg" or cmd == "LG":
        x = input("Number of liters: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / mol_liter * float(y)
        print(round(z, 7))
        print("")
    elif cmd == "gl" or cmd == "GL":
        x = input("Number of grams: ")
        y = input("Molar mass of element/compound: ")
        z = float(x) / float(y) * mol_liter
        print(round(z, 7))
        print("")
    else:
        print("Invalid command.")
        print("")
        get_input()

get_input()
