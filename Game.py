# Created by Crystal Studios
# Run this game in the terminal

from time import sleep
from random import randint
from tkinter import *
import sys
import os


root = Tk()
root.title("SYSTEM - LAUNCH CODE")
canvas = Canvas(root, width = 150, height = 150)
canvas.pack()


def continuelaunch():
    print("Verifying...")
    sleep(1)
    print("Valid Launch Code: Initiating Launch. Countdown started.")
    print("Communicating with Micro:Bit...")
    sleep(5)
    print("READY")
    print("Press LAUNCH")
    print("Pinging Micro:Bit. Printing onto Micro:Bit")
    print("...")
    sleep(20)
    print("LIFT OFF")
    sleep(1)
    print("Setting destination to Home, Moon 69")
    print("GAME OVER!")
    sleep(1)
    clear()
    print("Credits:")
    print("Developers: Taysir, Dan and Zain.")
    print("With special thanks to all of BBC Birmingham's CodingBrum Mentors!")
    sleep(1000000)
    sys.exit()


def Launch():
    code = spec.get()
    if code == launch_code:
        root.destroy()
        sleep(2)
        continuelaunch()
    else:
        print("Verifying...")
        sleep(1)
        print("Invalid Launch Code.")
        sleep(1)
        print("Error: UNABLE TO ABORT. Forcing shut down.")
        sleep(5)
        sys.exit(1)


# def Help():
#         pront = '''You have crash-landed on a distant alien planet.
# Your shuttle has recieved varying degrees of damage, the most severe areas being:
# -The engine
# -The thrusters
# To leave this planet and reach the Moon, you must repair the broken pieces of the shuttle.
# Pieces you will need to repair are found all over this planet. To find out what these items are,
# use the "examine" command followed by the part which you want to repair.
# One Small Step by Crystal Studios
# =================================
# Commands for text mode:
# reset (or restart)
# help
# go <direction>
# get <item>
# repair <shuttle part>
# examine <shuttle part>
# make <item>
# launch
# quit
# '''
#

# def Repair():
#     if spec.get() == 'engine':
#         if 'mercurium' in inventory:
#             if currentarea == 'Shuttle':
#                 engine_repaired = 'true'
#                 pront = "Successfully repaired the engine!"
#             else:
#                 pront = "You need to be at the Shuttle to repair the engine!"
#         else:
#             pront = "You lack the resources necessary to repair the engine. Use the examine command to see what you need."
#     elif spec.get() == 'thrusters':
#         if 'berylldium' in inventory:
#             if currentarea == 'Shuttle':
#                 thrusters_repaired = 'true'
#                 pront = "Successfully repaired the thrusters!"
#             else:
#                 pront = "You need to be at the Shuttle to repair the thrusters!"
#         else:
#             pront = "You lack the resources necessary to repair the thrusters. Use the examine command to see what you need."
#
#
# def Make():
#     if spec.get() == 'mercurium':
#         if 'ice' in inventory:
#             if 'sap' in inventory:
#                 inventory.append('mercurium')
#                 pront = "Used ice and sap to create mercurium!"
#     elif spec.get() == 'berylldium':
#         if 'beryllium' in inventory:
#             if 'mercurium' in inventory:
#                 inventory.append('berylldium')
#                 pront = "Used mercurium and beryllium to create berylldium!"
#
#
# def Get():
#     if "item" in areas[currentarea] and spec.get() in areas[currentarea]['item']:
#         inventory.append(spec.get())
#         pront = spec.get() + ' got!'
#         del areas[currentarea]['item']
#     else:
#         pront = 'Can\'t get ' + spec.get() + '!'
#
#
# def Look():
#     if spec.get() == 'engine' and areas[currentarea] == 'Shuttle':
#         pront = '''The engine requires Mercurium. To make this,
# use a cooling agent such as ice and some rubber such as sap from a tree.'''
#     elif spec.get() == 'thrusters' and areas[currentarea] == 'Shuttle':
#         pront = '''The thrusters requires Berylldium. To make this, you need two metals.'''
#
#
# def Launch():
#         if engine_repaired == 'true' and thrusters_repaired == 'true':
#             pront = "You board the ship and power on all the systems."
#             pront = pront + "The system prepares to launch."
#             pront = "The system console will now be printed"
#             pront = "==========================================================================="
#             pront = "Preparing to launch"
#             sleep(1)
#             pront = "Checking prerequisites"
#             sleep(1)
#             pront = "Analysing environment"
#             sleep(1)
#             pront = "Analysing system status"
#             sleep(1)
#             pront = "WARNING: Unable to abort. You are locked in."
#             sleep(1)
#             pront = "System detected no problems"
#             sleep(1)
#             pront = "LAUNCH SEQUENCE"
#             sleep(1)
#             pront = "Contacting Mission Control"
#             sleep(1)
#             pront = "Generating Launch Code"
#             sleep(1)
#             pront = "Successfully generated launch code"
#             sleep(1)
#             pront = "Launch Code: " + launch_code
#             sleep(1)
#             pront = "Initiating Launch Sequence"
#             sleep(1)
#             pront = "Input Launch Code (inc. dashes)"
#
#             if enter == launch_code:
#                 pront = "Verifying..."
#                 sleep(1)
#                 pront = "Valid Launch Code: Initiating Launch. Countdown started."
#                 pront = "Communicating with Micro:Bit..."
#                 sleep(5)
#                 pront = "READY"
#                 pront = "System Ready For Launch"
#                 pront = "Pinging Micro:Bit. Printing onto Micro:Bit"
#                 pront = "TERMINATING..."
#                 sleep(20)
#                 pront = "LIFT OFF"
#                 sleep(1)
#                 pront = "Setting destination to Home, Moon 69"
#                 pront = "GAME OVER!"
#                 sleep(1)
#                 clear()
#                 pront = "Credits:"
#                 pront = "Developers: Taysir, Dan and Zain."
#                 pront = "With special thanks to all of BBC Birmingham's CodingBrum Mentors!"
#                 sleep(99999999999999999999999999999)
#                 sys.exit()
#             else:
#                 print("Verifying...")
#                 sleep(1)
#                 print("Invalid Launch Code. Aborting Launch.")
#         else:
#                 print("You board the ship and power on all the systems.")
#                 print("The system prepares to launch.")
#                 print("The system console will now be printed")
#                 print("===========================================================================")
#                 print("Preparing to launch")
#                 sleep(1)
#                 print("Checking prerequisites")
#                 sleep(1)
#                 print("Analysing environment")
#                 sleep(1)
#                 print("Analysing system status")
#                 sleep(1)
#                 print("WARNING! System has detected several fatal errors.")
#                 sleep(1)
#                 print("Using pre-programmed protocol and continuing launch")
#                 sleep(1)
#                 print("Using pre-prepared Launch Code")
#                 sleep(1)
#                 print(10)
#                 sleep(1)
#                 print(9)
#                 sleep(1)
#                 print(8)
#                 sleep(1)
#                 print(7)
#                 sleep(1)
#                 print(6)
#                 sleep(1)
#                 print(5)
#                 sleep(1)
#                 print("FATAL ERROR ABORTING LAUNCH")
#                 sleep(1)
#                 print("The systems failed, causing the thrusters to give out.")
#                 sleep(1)
#                 print("With the engine still running with no thrusters, the shuttle exploded")
#                 sleep(1)
#                 print("GAME OVER!")
#                 sleep(1)
#                 print("Close the window to quit.")
#                 print("Quitting anyway in 10 seconds")
#                 sleep(10)
#                 sys.exit()
#
# def Enter():
#     enter = spec.get()


def showstatus():

    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentarea)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in areas[currentarea]:
        print('You see ' + areas[currentarea]['item'])
    print("---------------------------")
    print("What would you like to do?")


def clear():
    # for windows
    if sys.platform == 'win32':
        os.system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


launch_code = "LAUNCH-" + str(randint(0, 10)) + "-" + str(randint(0, 10)) + "-" + str(randint(0, 10)) + "-" + str(randint(0, 10)) + "-" + str(randint(0, 10))
engine_repaired = 'false'
thrusters_repaired = 'false'
inventory = []
areas = {

        'Shuttle': {
            'north': 'Ice Deposit',
            'west': 'Forest',
            'east': 'Caves',
            'south': 'Abandoned Mine'

        },

        'Ice Deposit': {
            'south': 'Shuttle',
            'item': 'ice'

        },

        'Caves': {
            'west': 'Shuttle',
            'item': 'beryllium'

        },

        'Forest': {
            'east': 'Shuttle',
            'item': 'sap'

        },

        'Abandoned Mine': {
            'north': 'Shuttle',
            'item': 'scandium'
        }

}
currentarea = 'Shuttle'


label = Label(root, text="INPUT LAUNCH CODE")
canvas.create_window(75, 45, window=label)
# goNorth = Button(app, command = North, text = "Go North")
# goNorth.grid(row = 6, column = 1)
#
# goEast = Button(app, command = East, text = "Go East")
# goEast.grid(row = 7, column = 2)
#
# goSouth = Button(app, command = South, text = "Go South")
# goSouth.grid(row = 8, column = 1)
#
# goWest = Button(app, command = West, text = "Go West")
# goWest.grid(row = 7, column = 0)
#
launch = Button(text='LAUNCH', command=Launch, bg='red', fg='white')
canvas.create_window(75, 95, window=launch)
# launch.grid(row = 0, column = 0)
#
# enter = Button(app, command = Enter, text = "Enter")
# enter.grid(row = 4, column = 6)
#
# output = Text(app, width = 60, height = 20, wrap = WORD)
# output.grid(row = 0, column = 0, columnspan = 3, rowspan = 5)
#
spec = Entry (root)
canvas.create_window(75, 75, window=spec)
# spec.grid(row = 1, column = 0)
#
# look = Button(app, command = Look, text = "Look")
# look.grid(row = 3, column = 4)
#
# get = Button(app, command = Get, text = "Get")
# get.grid(row = 4, column = 4)
#
# hlep = Button(app, command = Help, text = "Help")
# hlep.grid(row = 0, column = 4)
#
# repairbutt = Button(app, command = Repair, text = "Repair")
# repairbutt.grid(row = 1, column = 4)
#
# make = Button(app, command = Make, text = "Make")
# make.grid(row = 2, column = 4)


# def ask():
#     pront = '''You have crash-landed on a distant alien planet. Your shuttle has received varying degrees of damage, the most severe areas being:
#     -The engine
#     -The thrusters
#     To leave this planet and reach the Moon, you must repair the broken pieces of the shuttle.
#     Pieces you will need to repair are found all over this planet. To find out what these items are,
#     use the "examine" command followed by the part which you want to repair. You can also use the fabricator to create items from
#     the materials you have.
#
#     One Small Step by Crystal Studios
#     =================================
#     Commands:
#     help
#     go <direction>
#     get <item>
#     repair <shuttle part>
#     examine <shuttle part>
#     make <item>
#     launch
#     quit'''
#     print("Would you like to use Text Mode or GUI mode? [text/gui]")
#     text = input('>')
#     if text == 'text':
#         print("Enabling Text Mode...")
#     elif text == 'gui':
#         root.mainloop()
#         output.delete(0.0, END)
#         output.insert(0.0, pront)
#     else:
#         print("Unrecognised Command. Please Try Again")
#         ask()


print("You have crash-landed on a distant alien planet.")
sleep(3)
print("Your shuttle has received varying degrees of damage, the most severe areas being:")
print("-The engine")
sleep(3)
print("-The thrusters")
sleep(1)
print("To leave this planet and reach the Moon, you must repair the broken pieces of the shuttle.")
sleep(3)
print('''Pieces you will need to repair are found all over this planet. To find out what these items are,
use the "examine" command followed by the part which you want to repair. You can also use the fabricator to create items from
the materials you have.''')
sleep(3)
print('''
One Small Step by Crystal Studios
=================================
Commands:
help
go <direction>
get <item>
repair <shuttle part>
examine <shuttle part>
make <item>
launch
quit
''')
print("Note: all commands are case sensitive. Everything is lowercase!")
sleep(3)


while True:
    showstatus()

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in areas[currentarea]:
            currentarea = areas[currentarea][move[1]]
        else:
            print('You can\'t go that way!')
    elif move[0] == 'get':
        if "item" in areas[currentarea] and move[1] in areas[currentarea]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del areas[currentarea]['item']
        else:
            print('Can\'t get ' + move[1] + '!')
    elif move[0] == 'quit':
        sys.exit()
    elif move[0] == 'examine':
        if move[1] == 'engine' and areas[currentarea] == 'Shuttle':
            print('''The engine requires Mercurium. To make this,
use a cooling agent such as ice and some rubber such as sap from a tree.''')
        elif move[1] == 'thrusters' and areas[currentarea] == 'Shuttle':
            print('''The thrusters requires Berylldium. To make this, you need two metals.''')
    elif move[0] == 'repair' and move[1] == 'engine':
        if 'mercurium' in inventory:
            if currentarea == 'Shuttle':
                engine_repaired = 'true'
                print("Successfully repaired the engine!")
            else:
                print("You need to be at the Shuttle to repair the engine!")
        else:
            print("You lack the resources necessary to repair the engine. Use the examine command to see what you need.")

    elif move[0] == 'repair' and move[1] == 'thrusters':
        if 'berylldium' in inventory:
            if currentarea == 'Shuttle':
                thrusters_repaired = 'true'
                print("Successfully repaired the thrusters!")
            else:
                print("You need to be at the Shuttle to repair the thrusters!")
        else:
            print("You lack the resources necessary to repair the thrusters. Use the examine command to see what you need.")
    elif move[0] == 'make':
        if move[1] == 'mercurium':
            if 'ice' in inventory:
                if 'sap' in inventory:
                    inventory.append('mercurium')
                    print("Used ice and sap to create mercurium!")#
                    inventory.remove('ice')
                    inventory.remove('sap')
        if move[1] == 'berylldium':
            if 'beryllium' in inventory:
                if 'scandium' in inventory:
                    inventory.append('berylldium')
                    print("Used mercurium and beryllium to create berylldium!")
                    inventory.remove('beryllium')
                    inventory.remove('scandium')

    elif move[0] == 'help':
        print("You have crash-landed on a distant alien planet.")
        print("Your shuttle has recieved varying degrees of damage, the most severe areas being:")
        print("-The engine")
        print("-The thrusters")
        print("To leave this planet and reach the Moon, you must repair the broken pieces of the shuttle.")
        print('''Pieces you will need to repair are found all over this planet. To find out what these items are,
        use the "examine" command followed by the part which you want to repair.''')
        print('''
        One Small Step by Crystal Studios
        =================================
        Commands:
        reset (or restart)
        help
        go <direction>
        get <item>
        repair <shuttle part>
        examine <shuttle part>
        make <item>
        launch
        quit
        ''')
        print("Note: all commands are case sensitive. Everything is lowercase!")

    if move[0] == 'launch':
        if engine_repaired == 'true' and thrusters_repaired == 'true':
            print("You board the ship and power on all the systems.")
            print("The system prepares to launch.")
            print("The system console will now be printed")
            print("===========================================================================")
            print("Preparing to launch")
            sleep(1)
            print("Checking prerequisites")
            sleep(1)
            print("Analysing environment")
            sleep(1)
            print("Analysing system status")
            sleep(1)
            print("WARNING: Unable to abort. You are locked in.")
            sleep(1)
            print("System detected no problems")
            sleep(1)
            print("STARTING LAUNCH SEQUENCE")
            sleep(1)
            print("Contacting Mission Control")
            sleep(1)
            print("Generating Launch Code")
            sleep(1)
            print("Successfully generated launch code")
            sleep(1)
            print("Launch Code: " + launch_code)
            sleep(1)
            print("Initiating Launch Sequence")
            sleep(1)
            print("Input Launch Code (inc. dashes)")
            root.mainloop()
        else:
            print("You board the ship and power on all the systems.")
            print("The system prepares to launch.")
            print("The system console will now be printed")
            print("===========================================================================")
            print("Preparing to launch")
            sleep(1)
            print("Checking prerequisites")
            sleep(1)
            print("Analysing environment")
            sleep(1)
            print("Analysing system status")
            sleep(1)
            print("WARNING! System has detected several fatal errors.")
            sleep(1)
            print("Using pre-programmed protocol and continuing launch")
            sleep(1)
            print("Using pre-prepared Launch Code")
            sleep(1)
            print(10)
            sleep(1)
            print(9)
            sleep(1)
            print(8)
            sleep(1)
            print(7)
            sleep(1)
            print(6)
            sleep(1)
            print(5)
            sleep(1)
            print("FATAL ERROR ABORTING LAUNCH")
            sleep(1)
            print("The systems failed, causing the thrusters to give out.")
            sleep(1)
            print("With the engine still running with no thrusters, the shuttle exploded")
            sleep(1)
            print("GAME OVER!")
            sleep(1)
            print("Enter quit to quit the game.")
            exit = input('>')
            if exit == 'quit':
                sys.exit()



