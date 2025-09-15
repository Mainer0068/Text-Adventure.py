import math
import time as t
import sys


def end():
    print("\n<<< Game Over >>>\n")
    sys.exit(1)


inventory = []
# this doesn't do anything right now, im working on it. 
# Follow up to the above note, no matter what I try it keeps breaking my code.


def BoxHermitEnding():
    print("You never left the box... you sat in a dark box for the next week until you keeled over and died from starvation.")
    t.sleep(1)
    end()


def badend():
    print("You were then dispatched by the same creature with lightning speed, your remains will not be recovered.")
    t.sleep(1)
    end()


def BigBossEnding():
    print("You start to remember...")
    t.sleep(1)
    print("You put on the bandana and the eye patch, upon leaving the "
          " carboard box you remember you've been on a stealth op for the military; you kept 'em waiting huh?.")
    t.sleep(1)
    end()


def goodending():
    print("The soldier actually led you out of the facility, still unsure as to why you were let go, you pay it no mind as you find your way to the highway looking to hitch-hike back to civilization.")
    t.sleep(1)
    end()


def darknessEnd():
    print("You ran out of things to look at(I got lazy) and stayed in the dark for an unknown time, but you weren't seen again")
    t.sleep(1)
    end()


def TransformersEnd():
    print("You enter the Semi-Truck and before you can start driving, he transforms revealing"
          " a giant robot and he breaks you out of the facility; you then ride into the sunset listening to linkin park"
          " like in that one movie from 2007.")
    t.sleep(1)
    end()


def funnyend():
    print("You were shot several times, 5.56 tastes funny doesn't it?")
    t.sleep(1)
    end()


def StupidDeathEnd():
    print("YOU SERIOUSLY DIED BY SLIPPING ON A BANANA PEEL?\n HAVE YOU LEARNED NOTHING FROM MARIO KART?")
    t.sleep(1)
    end()

# Ending text code.


print("You wake up in a very dark, cramped room, sitting down with your legs pulled in.")
lookaround = input("Do you want to look around? \n(y/n):")

if lookaround.casefold() in ["n", "no"]:
    print("Good job, you remembered it's dark, and you can't see.")
else:
    print("It's dark, dummy.")

feelaround = input("Would you like to feel around? \n(y/n):")
if feelaround.casefold() in ["y", "yes"]:
    print("You realize you are sitting in a cardboard box, when touching the floor"
          " you feel a bandana and an eye patch.")

else:
    BoxHermitEnding()

bandanaEyePatch = input("Do you put them on? \n(y/n):")
if bandanaEyePatch.casefold() in ["y", "yes"]:
    BigBossEnding()

else:
    print("For some reason you find them nostalgic, but you leave them where they are.")
openbox = input("Would you like to exit the Cardboard Box? \n(y/n):")
if openbox.casefold() in ["n", "no"]:
    BoxHermitEnding()

# if openbox.casefold() in ["check inv", "check inventory"]:
#     print("wait what? Where did you get a tool box?")
#     t.sleep(1)
#     print(" I didn't give that to you...")


else:
    print("You have left the box, the room is large, and there is a crashed Go-Kart in the corner;"
          "a tattered red cap rests next to it; the letter M engraved on it.")
leavebox = input("Would you like to investigate?\n (y/n):")
if leavebox.casefold() in ["y", "yes"]:
    print("You approach the Go-kart, it's totaled, theres no way you can repair this. There is also a peculiar banana peel a little to your right.")

    while True:
        gokart = input(
            "Would you like to investigate the banana peel?\n (y/n): ")
        gokart = gokart.casefold()
        if gokart in ["y", "yes"]:
            StupidDeathEnd()
            break
        elif gokart == "repair go-kart":
            print("Are you illiterate or- no, you can't be, so open your eyes.")
        elif gokart in ["n", "no"]:
            print(
                "You step away from the Banana Peel, probably the safest bet, Mario Kart has taught you well.")
            break
        if gokart.casefold() in ["n", "no"]:
            print(
                "You step away from the Banana Peel, probably the safest bet, Mario Kart has taught you well.")

# While True that runs the go-kart secret interaction, I don't know why but it wouldn't work properly without this.

if leavebox.casefold() in ["n", "no"]:
    print("you choose to leave the go-kart alone, walking around the room you spot a semi truck")
    truck = input("do you approach the semi?\n (y/n):")
    if truck.casefold() in ["y", "yes"]:
        TransformersEnd()

    else:
        darknessEnd()

bananaPeel = input(
    "'HALT', someone yell's from behind you, do you want to turn around?\n (y/n):")
if bananaPeel.casefold() in ["y", "yes"]:
    print("You see a soldier pointing a rifle at you, he looks scared, scanning you up and down, shaking lightly.")

Soldier = input("do you trust the soldier?\n (y/n):")
if Soldier.casefold() in ["y", "yes"]:
    goodending()

if Soldier.casefold() in ["CHARGE!".casefold()]:
    funnyend()


if Soldier.casefold() in ["n", "no"]:
    print("The soldier is then ripped apart by something faster than you can see.")
    t.sleep(3)
    badend()
