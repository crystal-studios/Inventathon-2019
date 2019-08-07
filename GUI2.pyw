from tkinter import *
from time import sleep
from random import randint
import sys
import os

root = Tk()
root.title("One Small Step")
root.geometry("620x525")
app = Frame(root)
app.grid()

def clear():
    # for windows
    if sys.platform == 'win32':
        os.system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def showstatus():

    pront = "---------------------------\nYou are in the" + currentarea + "\nInventory: " + str(inventory) + "\n"
    if "item" in areas[currentarea]:
        pront = pront + "You see a " + areas[currentarea]["item"] + "\n---------------------------\nWhat would you like to do?"
        output.delete(0.0, END)
        output.insert(0.0, pront)
    else:
        output.delete(0.0, END)
        output.insert(0.0, pront)

def North():
    if current
    pront = "North"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def East():
    pront = "East"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def South():
    pront = "South"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def West():
    pront = "West"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def Launch():
    pront = "Launch"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def Get():
    poop = spec.get()
    pront = poop + " added to inventory"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def Look():
    poop = spec2.get()
    pront = "You look at " + poop

    output.delete(0.0, END)
    output.insert(0.0, pront)

def HELP():
    pront = "This helps"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def Repair():
    pront = spec4.get() + " has been repaired"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def Make():
    pront = spec3.get() + " has been made"

    output.delete(0.0, END)
    output.insert(0.0, pront)

goNorth = Button(app, command = North, text = "Go North")
goNorth.grid(row = 6, column = 1)

goEast = Button(app, command = East, text = "Go East")
goEast.grid(row = 7, column = 2)

goSouth = Button(app, command = South, text = "Go South")
goSouth.grid(row = 8, column = 1)

goWest = Button(app, command = West, text = "Go West")
goWest.grid(row = 7, column = 0)

launch = Button(app, command = Launch, text = "Launch")
launch.grid(row = 7, column = 1)

output = Text(app, width = 60, height = 20, wrap = WORD)
output.grid(row = 0, column = 0, columnspan = 3, rowspan = 5)

spec = Entry(app, width = 15)
spec.grid(row = 4, column = 5)

spec2 = Entry(app, width = 15)
spec2.grid(row = 3, column = 5)

look = Button(app, command = Look, text = "Look")
look.grid(row = 3, column = 4)

get = Button(app, command = Get, text = "Get")
get.grid(row = 4, column = 4)

hlep = Button(app, command = HELP, text = "Help")
hlep.grid(row = 0, column = 4)

repairbutt = Button(app, command = Repair, text = "Repair")
repairbutt.grid(row = 1, column = 4)

make = Button(app, command = Make, text = "Make")
make.grid(row = 2, column = 4)

spec3 = Entry(app, width = 15)
spec3.grid(row = 2, column = 5)

spec4 = Entry(app, width = 15)
spec4.grid(row = 1, column = 5)

while True:
    showstatus()

root.mainloop()