import random
import time
import replit
from random import randint

# Variables
symbols = ["🍒", "🔔", "🍋", "🧡", "🌟", "☠️"]
money = 100
counter = 0
replit.clear()

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

 # machine looping
  while counter != 20:
    replit.clear()
  
    randomSymbol = randint(0, 5)
    randomSymbolTwo = randint(0, 5)
    randomSymbolThree = randint(0, 5)
  
    print(" ")
    print("|========| money =", money)
    print("| - | - | - | o")
    print("| ☁️ | ☁️ | ☁️ | /")
    print("| " + symbols[randomSymbol] + "| " + symbols[randomSymbolTwo] +  "| " + symbols[randomSymbolThree] + "|")
    print("| ☁️ | ☁️ | ☁️ | ---o")
    print("|---------|")
    print("|⬛⬛⬛⬛⬛|")
    print("|⬛⬛⬛⬛⬛|")
  
  # setup sleep timer
    time.sleep(0.1)
    counter = counter +1
done = 0

# if randomSymbol != randomSymbolTwo and randomSymbol != randomSymbolThree and randomSymbolTwo != randomSymbolThree:
  # print("you win!")
  # money = money + 20
 # done = 1