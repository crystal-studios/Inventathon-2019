from tkinter import *



root = Tk()
root.title("One Small Step")
root.geometry("600x650")
app = Frame(root)
app.grid()

def North():
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

def Inventory():
    pront = inventory

    output.delete(0.0, END)
    output.insert(0.0, pront)

def Get():
    poop = spec.get()
    pront = poop + " added to inventory"

    output.delete(0.0, END)
    output.insert(0.0, pront)

def Look():
    poop = spec2.get()
    pront = poop + " added to inventory"

    output.delete(0.0, END)
    output.insert(0.0, pront)

goNorth = Button(app, command = North, text = "Go North")
goNorth.grid(row = 1, column = 1)

goEast = Button(app, command = East, text = "Go East")
goEast.grid(row = 2, column = 2)

goSouth = Button(app, command = South, text = "Go South")
goSouth.grid(row = 3, column = 1)

goWest = Button(app, command = West, text = "Go West")
goWest.grid(row = 2, column = 0)

inventory = Button(app, command = Inventory, text = "Inventory")
inventory.grid(row = 2, column = 1)

output = Text(app, width = 60, height = 20, wrap = WORD)
output.grid(row = 0, column = 0, columnspan = 3) #nice

spec = Entry(app, width = 15)
spec.grid(row = 1, column = 2)

spec2 = Entry(app, width = 15)
spec2.grid(row = 3, column = 2)

look = Button(app, command = Look, text = "Look")
look.grid(row = 3, column = 0)

get = Button(app, command = Get, text = "Get")
get.grid(row = 1, column = 0)

root.mainloop()