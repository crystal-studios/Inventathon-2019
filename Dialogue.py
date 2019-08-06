def start():
  print("You have crash-landed on a distant alien planet.")
  sleep(1)
  print("Your shuttle has recieved varying degrees of damage, the most severe areas being:")
  print("-The engine")
  sleep(0.5)
  print("-The thrusters")
  sleep(1)
  print("To leave this planet and reach the Moon, you must repair the broken pieces of the shuttle.")
  sleep(1)
  print('''Pieces you will need to repair are found all over this planet. To find out what these items are,
  use the "examine" command followed by the part which you want to repair.''')
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
  

def leave():

  print("Credits:")
  print("Developers: Taysir, Dan and Zain.")
  print("With special thanks to all of BBC Birmingham's CodingBrum Mentors!")
