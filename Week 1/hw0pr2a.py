# coding: utf-8
#
# hw0pr2a.py
#

import random          # imports the library named random


def rps():
    while True:
        user_choice = input("Choose your weapon: ")
        comp = random.choice(["rock", "paper", "scissors"])
        print()

        print("The user (you) chose", user_choice)
        print("The computer (I) chose", comp)
        print()

        if user_choice == comp:
            print("Both Players Chose: ", user_choice)
        elif user_choice == "rock":
            if comp == "scissors":
                print("Your WIN: Rock beats Scissors")
            else:
                print("Guessing is not your thing: Paper beats Rock")
        elif user_choice == "paper":
            if comp == "rock":
                print("You WIN: Paper beats Rock")
            else:
                print("Sorry but: Scissors beats Rock")
        elif user_choice == "scissors":
            if comp == "rock":
                print("Oops looks like: Rock beats Scissors")
            else:
                print("You WIN: Scissors beats Paper")
        print("Still running...")
        response = input("Play again? ")
        if response == "n":
            break