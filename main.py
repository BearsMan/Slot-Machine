import random
import time
import replit
from random import randint

# Variables
symbols = ["🍒", "🔔", "🍋", "🧡", "🌟", "☠️"]
money = 100
counter = 0
replit.clear()
randomList = []

# Create start of program
# while loops
while money != 0:
  print("|========| money =", money)
  print("| - | - | - | o")
  print("| 0 | 0 | 0 | /")
  print("| - | - | - |/")
  print("|========|")
  print("|00000000|")
  print("|00000000|")
  print(" ")

  input("roll:")
  money = money - 20

  replit.clear()
  counter = 0
  randomList = []

  # machine looping
  while counter != 20:
    replit.clear()
    randomList = []

    for i in range(9):
      randomList.append(symbols[randint(0, 5)])
    print(" ")
    print("|========| money =", money)
    print("| " + randomList[0] + "| " + randomList[1] + "|" + randomList[2] +
          "|")
    print("| " + randomList[3] + "| " + randomList[4] + "|" + randomList[5] +
          "|")
    print("| " + randomList[6] + "| " + randomList[7] + "|" + randomList[8] +
          "|")
    print("|---------|")
    print("|⬛⬛⬛⬛⬛|")
    print("|⬛⬛⬛⬛⬛|")
    time.sleep(0.5)
    counter = counter + 1

  done = 0

  randomSymbol = randint(0, 5)
  randomSymbolTwo = randint(0, 5)
  randomSymbolThree = randint(0, 5)
  if randomList[0] == randomList[1] == randomList[2]:
    print("top row matches")
    if (randomList[0] == "☠️"):
      print("You do not have any money left")
      money = 0

    else:
      money += 10

      print("You have won 10 dollars")
    done = 1

  if randomList[3] == randomList[4] == randomList[5]:
    print("middle row matches")
    if (randomList[3] == "☠️"):
      print("YOU DO NOT HAVE ANY MORE MONEY!")
      money = 0
    else:
      money += 10
      print("You have won 10 dollars")
    done = 1
  if randomList[6] == randomList[7] == randomList[8]:
    print("last row matches")
    if (randomList[6] == "☠️"):
      print("You are broke!")
      money = 0
    else:
      money += 10
    done = 1
    if (randomList[0] == randomList[4] ==
        randomList[8]) or (randomList[2] == randomList[4] == randomList[6]):

      print("diagonal matches")
      if (randomList[4] == "️☠️"):
        print("You are broke!")
        money = 0
      else:
        money += 10
      done = 1
    if (done != 1):
      print("No Match")
      done = 1
    time.sleep(3)
    replit.clear()
replit.clear()
print("")
print("Game Over!")
