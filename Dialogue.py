from time import sleep

def start():

  print("You have crash-landed on a distant alien planet.")
  sleep(1)
  print("Your shuttle has recieved varying degrees of damage, the most severe areas being:")
  sleep(1)
  print(".The thrusters")
  sleep(0.5)
  print(".The engine")
  sleep(0.5)
  print(".and the hull")
  sleep(1)
  print("To leave this planet and reach the Moon, you must repair the broken pieces of the shuttle.")
  sleep(1)
  print('''Pieces you will need to repair are found all over this planet. To find out what these items are,
  use the "examine" command followed by the part which you wnat to repair.''')
  loop()
  
def leave():
  #the end bit sequence thing starts here
  sleep(4)
  print("The shuttle has been successfully repaired and you can leave the alien planet.")
  sleep(1)
  print("You board ")