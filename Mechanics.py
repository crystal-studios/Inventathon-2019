#Created by Crystal Studios

from time import sleep

def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    print("What would you like to do?")

    inventory = []

    areas = {

        'Shuttle': {
            'north': 'Ice Deposit',
            'west': 'Forest',
            'east': 'Caves'

        },

        'Ice Deposit': {
            'south': 'Shuttle'

        },

        'Caves': {
            'west': 'Shuttle'

        },

        'Forest': {
            'east': 'Shuttle'

        }

    }

currentArea = 'Shuttle'

def loop():

    while True:
        showStatus()

        move = ''
        while move == '':
            move = input('>')

        move = move.lower().split()

        if move[0] == 'go':
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print('You can\'t go that way!')

        if move[0] == 'get':
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                inventory += [move[1]]
                print(move[1] + ' got!')
                del rooms[currentRoom]['item']
            else:
                print('Can\'t get' + move[1] + '!')

        if move[0] == 'quit':
            exit()
