import random

print("Python3 Coding Exercise: Name from a Hat\n")
print("Start entering names. Type 'complete' when you have finished.\n")

pendingInput = True
nameCount = 1
name_list = []

while pendingInput:
  val = input("Enter name "+str(nameCount)+": ")
  if val == "complete":
    pendingInput = False
    print("Names successfully entered\n")
  else:
    name_list.append(val)
    nameCount += 1

print("Type 'draw' or 'draw again' to randomly select a name.\n")

def drawRandomName():
  randomname = random.choice(name_list)
  print("The name drawn was: "+ randomname +"\n")

while True:
  randomname = ""

  val = input()
  if val == "draw":
    drawRandomName()
  elif val == "draw again":
    drawRandomName()
  else:
    print("unexpected input.")
  
