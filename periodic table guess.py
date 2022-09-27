
import random

def main():
    """Start a periodic table  guessing game."""
    print("Guess the periodic table!")

#this variable is to list out the elements in periodic table
    periodic_table = [
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        ]

#this variable is a random periodic table 
    x = random.choice(periodic_table)
#print(x)
    guess = None

    while x != guess:

        guess = str(input("what periodic table am i thinking of?"))

#this variable is a hint of periodic table
        if x == guess:
            print("you guessed {}. You winned!".format(guess))
        elif x == "H":
                 print("Try a non-toxic periodic table.")
        elif x == "He":
                 print("Try a colorless.")
        elif x == "Li":
                 print("Try a mineral oil.")
        elif x == "Be":
                 print("Try a hard metal.")
        elif x == "B":
                 print("Try a electricity.")
        elif x == "C":
                 print("try a soft")
        elif x == "N":
                 print("Try a odorless gas.")
        elif x == "O":
                 print("Try a standard tempeture.")
        elif x == "F":
                 print("Try a pale yellow-green.")
        elif x == "Ne":
                 print("Try a second-lightest noble gas.")

main()
