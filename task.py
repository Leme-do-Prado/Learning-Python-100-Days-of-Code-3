
print("Hello! Welcome to the Treasure Island. \n Let's start your journey!. \n")


direction = str(input("Are you going left or right?\n"))
if direction == "left":
  print("You continue!")
  direction = str(input("You come across a lake. Are you going to swim or wait?\n"))
  if direction == "wait":
      print("You continue!")
      direction = str(input("You come across three doors of different colours: red, blue and yellow. Which door are you choosing?\n"))
      if direction == "red":
          print("You are burned by fire\n...Game over.")
      elif direction == "blue":
          print("You are eaten by beasts\n...Game over.")
      elif direction == "yellow":
          print("You find the treasure\n...You WIN!")
      else:
          print("Game over.")
  else:
      print("You were attacked by a trout\n...Game over.")
else:
    print("You fell into a hole\n...Game over.")



