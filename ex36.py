#!/usr/bin/python2.7

from sys import exit
from random import randint

# Hmm.
# The treasure they are looking for
# print "In doing so you have managed to recover",treasure,"and quickly head out the exit."
# Make the treasure fit in the sentence above.
treasure = "the Great BearBear"


# Everyone dies sometimes.
def dead(why):
    print why, "Good job!"
    exit(0)


# Main choice: choice = raw_input("> ").lower
# First main room of the library
def lib_first_room():
    print "You are standing just inside the large Library of Palanthas."
    print "To the east and west you can see more rooms leading out."
    print "A bookcase swings closed behind you closing the door you just entered from."
    print "All wall space that isn't a door or doorway is bookshelves."
    print "Which way would you like to go east or west?"

    # Choose which way to go.
    choice = raw_input("> ").lower()
    if choice == "east":
        lib_2_exit("east", 0, 1)
    elif choice == "west":
        lib_2_exit("west", 0, 0)
    else:
        dead("You really should pay more attention. A bookcase falls and crushes you.")


# Directions
def directions_out(dir_from, top, side, corner):
    # Find direction came from using the info on the directions I chose.
    came_from = ""
    go_to = ""
    if dir_from == "east":
        came_from = "west"
    elif dir_from == "west":
        came_from = "east"
    elif dir_from == "north":
        came_from = "south"
    elif dir_from == "south":
        came_from = "north"
    else:
        dead("Randy is going crazy!!!")

    # Is the previous room a corner?
    if corner == 0:
        # If it wasn't and I came from the <BLANK> go_to should be the opposite:
        if came_from == "north":
            go_to = "south"
        elif came_from == "south":
            go_to = "north"
        elif came_from == "east":
            go_to = "west"
        elif came_from == "west":
            go_to = "east"
        else:
            dead("Broke corner 0 directions")
    elif corner == 1:
        # print top, came_from, side
        if top == 1 and came_from == "south" and side == 1:
            go_to = "west"
        elif top == 1 and came_from == "south" and side == 0:
            go_to = "east"
        elif top == 0:
            go_to = "north"
        else:
            dead("Broke corner 1 directions")
    else:
        dead("I really cannot code!")

    print "Directions out of the room are", came_from, "(the way you came) or", go_to, "please choose..."
    choice = raw_input("> ").lower()
    if choice == came_from or choice != go_to:
        dead("You must continue moving forward! You will surely die of boredom.")
    elif choice == "north" and came_from == "south":
        lib_corner(choice, 1, side)
    elif choice == "south" and came_from == "north":
        lib_corner(choice, 0, side)
    elif choice == "east" and came_from == "west":
        if top == 1:
            foyer()
        else:
            lib_corner(choice, top, side)
    elif choice == "west" and came_from == "east":
        if top == 1:
            foyer()
        else:
            lib_corner("east", top, side)
    elif choice == "west" or choice == "north" or choice == "east" or choice == "south":
        lib_2_exit(choice, top, side)
    else:
        dead("You should have continues forward! You eventually die of starvation.")


# Foyer
def foyer():
    print "Standing before a large angry looking Zombie, you tremble in fear."
    print "You notice a door behind it."
    print "You must decide what to do:"
    print "1. Throw a spear from the wall at the Zombie."
    print "2. Distract the Zombie, open the door and rush through quickly."
    print "3. Taunt the Zombie and try to make a run for it."

    choice = int(raw_input("> "))
    if choice == 1:
        dead("""You grab the spear and hurl with all of your strength and manage to hit it's big toe.
            You didn't slow it enough and it begins eating your toes when it catches you.""")
    elif choice == 3:
        dead("This Zombie obviously ran cross contry. It catches you and begins eating your fingers.")
    elif 2:
        print """You throw some dog food shaped like brains into a far corner,
        distracting the Zombie and rush through the door."""
        treasure_room()
    else:
        dead("Well that didn't work did it.")


# Library 2 exit rooms
def lib_2_exit(dir_from, top, side):
    print "You have stepped into another of the many rooms in the Library."
    # print "2 Exit"
    random_text()
    directions_out(dir_from, top, side, 0)


# Corner Rooms (came_from, top, corner, side): lib_corner(choice, 1, side)
def lib_corner(dir_from, top, side):
    print "You have stepped into another of the many rooms in the Library."
    # print "Corner!!!"
    random_text()
    directions_out(dir_from, top, side, 1)


# Random text for rooms:
def random_text():
    number = randint(0, 6)
    room_descript = ["You notice a fountain in the room. Odd...",
                     """There lies the skeletal remains of a traveller that was lost
                        due to the confusing nature of the Library.""",
                     "There are many dusty tomes upon the shelves. It seems the no one has been through in a while.",
                     "You notice a slight humming coming from the walls of this room. That is quite strange.",
                     "You hear a dripping noise coming from behind the walls.",
                     "You could swear you have been in this room before...",
                     "You begin to wonder if you will ever find the way out of this crazy place."]
    print room_descript[number]


# Treasure Room
def treasure_room():
    print "Congratulations, Explorer! You have made it through the library."
    print "In doing so you have managed to recover", treasure, "and quickly head out the exit."
    print "Praying you never return to this place again...."
    exit(0)


# Start of the adventure.
def start():
    print "You are in a poorly lit room."
    print "There is a doorway to the north, leading deeper into the Library."
    print "Seems the only way to go is north. Please proceed..."

    choice = raw_input("> ").lower()

    if choice == "north":
        lib_first_room()
    else:
        dead("You stumble around the room until you starve. Next time you should try going 'North'.")


start()
