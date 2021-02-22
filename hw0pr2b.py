# coding: utf-8
#
# hw0pr2b.py
#

""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.
"""

import time


def adventure():
    delay = 0.5
    user_name = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", user_name, " to the Libra Complex, a labyrinth")
    print("of weighty wonders and unreal quantities...of puppies!")
    print()

    print("Your quest: To find the best puppy!")
    print()
    flavor = input("What pup do you seek? ")
    if flavor == "corgi":
        print("Wise! You show deep pup experience.")
    elif flavor == "magic doggo":
        print("Magic is your true power!")
    else:
        print("Each to their own, then.")
    print()

    print("On to the quest!\n\n")
    print("A corridor stretches before you; its dim lighting betrays, to")
    print("two doors. Door one has an image of a fearsome beast")
    print("and, to the other, a door ajar, leaking laughter")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose door one or door two? [one/two] ")
    print()

    if choice1 == "one":
        print("As you approach door one, its hazy burdens loom ever larger,")
        print("until...")
        time.sleep(delay)
        print("...you see a mess of toys spread out around the ground")
        print("Unsure of why so many toys your search for reasoning...")

        print("\nYou come across toy box that is close but...")
        print("You can hear faint wimpers")
        print("As you get closer the wimpers seem also come from behind a curtain.\n")

        choice1 = input("Do you look inside the box, do you think nothing of it, or do you look behind the curtain? [box/leave/curtain] ")
        print()

        if choice1 == "box":
            print("\nYou built up the courage to look inside the box")
            print("There seems to be a hidden trap door!...")
            print("Go on and explore!\n\n")
            time.sleep(delay)
            print("Stepping into the trap door you can only see a flicker of light")
            print("This can be a scary journey...what do you do?\n")

            choice1 = input("Do you climb back to the room or do you continue down the tunnel? [go back/continue] ")
            print()

            if choice1 == "go back":
                print("Unsure of where the tunnel leads you climbed back up...")
                time.sleep(delay)
                print("Uh oh... the cats from door two escaped...Farewell")
            elif choice1 == "continue":
                print("Mighty brave of you...")
                print("After what seemed an eterinty you reached the end of the tunnel...")
                time.sleep(delay)
                print("Oh what a sight it is! Puppies everywhere!")
                print("Congrats", user_name, "NOW GO AND PLAY\n")

                choice1=input("WAIT...did you find a corgi? [yes/no]")
                if choice1 == "yes":
                    print("\nSay hi for me!")
        elif choice1 == "leave":
            print("You decided to stop your search.")
            print("I guess you are not ready to adventure")
            print("Farewell,", user_name)
        elif choice1 == "curtain":
            print("You decided to reach for the curtain but...")
            print("quickly realized it was a mistake.")
            print("The curtain was blocking a cold draft.")
            print("You must stop your search to go warm up...Farwell...")
        else:
            print("You did nothing and the wimpering stop...")
            print("You can no longer find the source of the sound")
            print("With out any clues you give up on your search for a pup...Farwell")
    else:
        print("You push door two into a gathering cats.")
        time.sleep(delay)
        print("There you wonder if this is the end.")
        print("They approach you surronding you from all ends")
        print("Farewell,", user_name, ".")
