# Created by Crystal Studios
# Run this game in the terminal

from time import sleep
from random import randint
import sys
import os


def showstatus():

    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentarea)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in areas[currentarea]:
        print('You see a ' + areas[currentarea]['item'])
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
            'east': 'Caves'

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

        }

}
currentarea = 'Shuttle'

print("You have crash-landed on a distant alien planet.")
sleep(3)
print("Your shuttle has recieved varying degrees of damage, the most severe areas being:")
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
        exit()
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
                    print("Used ice and sap to create mercurium!")
        if move[1] == 'berylldium':
            if 'beryllium' in inventory:
                if 'mercurium' in inventory:
                    inventory.append('berylldium')
                    print("Used mercurium and beryllium to create berylldium!")

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

    if move[0] == 'launch':
        if engine_repaired == 'true' and thrusters_repaired == 'true' and areas[currentarea] == 'Shuttle':
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
                print("Continue Launch? [y/n]")
                print("Note: The game will quit if you say no.")
                idk = input('>')
                if idk == 'y':
                    print("Initiating Launch Sequence")
                    sleep(1)
                    print("Input Launch Code (inc. dashes)")
                    launchcode = input('>')
                    if launchcode == launch_code:
                        print("Verifying...")
                        sleep(1)
                        print("Valid Launch Code: Initiating Launch. Countdown started.")
                        print("Communicating with Micro:Bit...")
                        sleep(5)
                        print("READY")
                        print("System Ready For Launch")
                        print("10")
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
                        print(4)
                        sleep(1)
                        print(3)
                        sleep(1)
                        print(2)
                        sleep(1)
                        print(1)
                        sleep(1)
                        print("LIFT OFF")
                        sleep(1)
                        print("Setting destination to Home, Moon 69")
                        print("GAME OVER!")
                        sleep(1)
                        clear()
                        print("Credits:")
                        print("Developers: Taysir, Dan and Zain.")
                        print("With special thanks to all of BBC Birmingham's CodingBrum Mentors!")
                        break
                    else:
                        print("Verifying...")
                        sleep(1)
                        print("Invalid Launch Code. Aborting Launch.")
                elif idk == 'n':
                    sys.exit()
                    # currentarea = 'Shuttle'
                    # inventory = []
                    # engine_repaired = 'false'
                    # thrusters_repaired = 'false'
                    # areas = {
                    #
                    #     'Shuttle': {
                    #         'north': 'Ice Deposit',
                    #         'west': 'Forest',
                    #         'east': 'Caves'
                    #
                    #     },
                    #
                    #     'Ice Deposit': {
                    #         'south': 'Shuttle',
                    #         'item': 'ice'
                    #
                    #     },
                    #
                    #     'Caves': {
                    #         'west': 'Shuttle',
                    #         'item': 'beryllium'
                    #
                    #     },
                    #
                    #     'Forest': {
                    #         'east': 'Shuttle',
                    #         'item': 'sap'
                    #
                    #     }
                    #
                    # }
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
                print("Quitting anyway in 10 seconds")
                exit = input('>')
                if exit == 'quit':
                    sys.exit()
                sleep(10)
                sys.exit()
    # elif move[0] == 'reset' or 'restart':
    #     currentarea = 'Shuttle'
    #     inventory = []
    #     engine_repaired = 'false'
    #     thrusters_repaired = 'false'
    #     areas = {
    #
    #         'Shuttle': {
    #             'north': 'Ice Deposit',
    #             'west': 'Forest',
    #             'east': 'Caves'
    #
    #         },
    #
    #         'Ice Deposit': {
    #             'south': 'Shuttle',
    #             'item': 'ice'
    #
    #         },
    #
    #         'Caves': {
    #             'west': 'Shuttle',
    #             'item': 'beryllium'
    #
    #         },
    #
    #         'Forest': {
    #             'east': 'Shuttle',
    #             'item': 'sap'
    #
    #         }
    #
    #     }

