import math
import time as t
import sys


def end():
    print("\n<<< Game Over >>>\n")
    sys.exit(1)


inventory = []


def SecretEnding():
    print("You repaired the Go-Kart and found a garage door on the other end of the Room...")
    t.sleep(1)
    print("This... shouldn't be possible...")
    end()

def JoshuaEnd():
    print("Congradulations, you found the Joshua ending, and yes I prepared this for when you typed potato.")
    t.sleep(1)
    end()

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
    print("You put on the bandana and the eye patch, upon leaving the carboard box you remember you've been on a stealth op for the military; you kept 'em waiting huh?.")
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
    print("You enter the Semi-Truck and before you can start driving, he transforms revealing a giant robot and he breaks you out of the facility; you then ride into the sunset listening to linkin park like in that one movie from 2007.")
    t.sleep(1)
    end()


def funnyend():
    print("you were shot several times, 5.56 tastes funny doesn't it?")
    t.sleep(1)
    end()


def StupidDeathEnd():
    print("YOU SERIOUSLY DIED BY SLIPPING ON A BANANA PEEL?\n HAVE YOU LEARNED NOTHING FROM MARIO KART?")
    t.sleep(1)
    end()

# Game start


print("You wake up in a very dark, cramped room, sitting down with your legs pulled in.")
lookaround = input("Do you want to look around? \n(y/n):")

if lookaround.casefold() in ["n", "no"]:
    print("Good job, you remembered it's dark, and you can't see.")
if lookaround.lower() in ["Potato", "potato"]:
    JoshuaEnd()
if lookaround.lower() in ["yes", "Yes"]:
    print("It's dark, dummy.")
    
    

feelaround = input("Would you like to feel around? \n(y/n):")
if feelaround.casefold() in ["y", "yes"]:
    print("You realize you are sitting in a cardboard box, when touching the floor you feel a bandana and an eye patch.")
if feelaround.lower() in ["potato", "Potato"]:
    JoshuaEnd()
if feelaround.lower() in ["n", "no"]:
    BoxHermitEnding()

bandanaEyePatch = input("Do you put them on? \n(y/n):")
if bandanaEyePatch.casefold() in ["y", "yes"]:
    BigBossEnding()
if bandanaEyePatch.lower() in ["potato", "Potato"]:
    JoshuaEnd()
else:
    print("For some reason you find them nostalgic, but you leave them where they are.")

openbox = input("Would you like to exit the Cardboard Box? \n(y/n):")
if openbox.casefold() in ["n", "no"]:
    BoxHermitEnding()
if openbox.lower() in ["potato", "Potato"]:
    JoshuaEnd()
else:
    openbox.lower() in ["y", "yes"]
    print("You have left the box, the room is large, and there is a crashed Go-Kart in the corner; a tattered red cap rests next to it; the letter M engraved on it.")


leavebox = input("Would you like to investigate?\n (y/n):")
if leavebox.casefold() in ["potato", "Potato"]:
    JoshuaEnd()
    if leavebox.lower() in ["check inv", "check inventory"]:
        print("wait what? Where did you get a tool box?")
        t.sleep(1)
        print("\n I didn't give that to you... \n")
        inventory.append("Tool Box")

if leavebox.lower() in ["y", "yes", "check inv", "check inventory"]:
    print("You approach the Go-kart, it's totaled, theres no way you can repair this. There is also a peculiar banana peel a little to your right.")
    while True:
        gokart = input(
            "Would you like to investigate the banana peel? Or try something else?\n (y/n): ").lower()
        
        if gokart in ["y", "yes"]:
            StupidDeathEnd()
            break
        if gokart in ["potato", "Potato"]:
            JoshuaEnd()
            break
        elif gokart == "repair go-kart":
            if "Tool Box" in inventory:
                SecretEnding()
                break
            else:
                print("\n Are you illiterate or- no you managed to make it here.\n")
        if gokart.casefold() in ["n", "no"]:
            print("You step away from the Banana Peel, probably the safest bet, Mario Kart has taught you well.")
            break
      
            

if leavebox.lower() in ["n", "no"]:
    print("you choose to leave the go-kart alone, walking around the room you spot a semi truck")
    truck = input("do you approach the semi?\n (y/n):")
    if truck.casefold() in ["y", "yes"]:
        TransformersEnd()
    elif truck.lower() in ["potato", "Potato"]:
        JoshuaEnd()
    elif truck.lower() in ["n", "no"]:
        darknessEnd()
        

bananaPeel = input(
    "'HALT', someone yell's from behind you, do you want to turn around?\n (y/n):")
if bananaPeel.casefold() in ["y", "yes"]:
    print("You see a soldier pointing a rifle at you, he looks scared, scanning you up and down, shaking lightly.")
if bananaPeel.lower() in ["potato", "Potato"]:
    JoshuaEnd()

Soldier = input("do you trust the soldier?\n (y/n):")
if Soldier.casefold() in ["y", "yes"]:
    goodending()
elif Soldier.casefold() == "charge!":
    funnyend()
elif Soldier.casefold() in ["n", "no"]:
    print("The soldier is then ripped apart by something faster than you can see.")
    t.sleep(3)
    badend()
elif Soldier.lower() in ["potato", "Potato"]:
    JoshuaEnd()
