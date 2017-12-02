import random, time
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
_________________________________________
0                                       0
|Bases Game by Luke Roberts 10AB.       | 
|                                       |
|01110100 01101000 01101001 01110011    |
|00100000 01110100 01101111 01101111    |
|01101011 00100000 01101100 01101001    |
|01110100 01100101 01110010 01100001    |
|01101100 01101100 01111001 00100000    |
|01101110 01101111 00100000 01110100    |
|01101001 01101101 01100101 00100000    |
|01110100 01101111 00100000 01101101    |
|01100001 01101011 01100101             |
|                                       |
|Note:                                  |
|This game is a bit falty and not 100%  |
|correct all of the time; I'm working on|
|the bugs so don't throw anything at me |
|because of the errors.                 |
0_______________________________________0
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print(
  '''
   ___       _     ____  ____ ____
  │   │     ╱ ╲    │    │     │
  │___     ╱___╲   ____ │___  ____
  │   │   ╱     ╲     │ │        │
  │___│  ╱       ╲ ____ │____ ____
  __________________________________
   ___      _     _____  ____
  │        ╱ ╲    │ │ │ │
  │ ___   ╱___╲   │ │ │ │___
  │   │  ╱     ╲  │ │ │ │
  │___│ ╱       ╲ │ │ │ │____ version 0.0.1
  ___________________________________________
  '''
  )
time.sleep(3)
print("DO NOT use a calculator")
print("")
time.sleep(3)
print("This game is brutaly difficult.")
print("So if you do badly don't give in!")
print("")
time.sleep(3)
print("Ignore 0b, 0x and 0o")
print("")
time.sleep(3)
print("Good Luck!")
print("")
time.sleep(3)
def binary():
  score = 0
  while True:
    n = random.randint(0,maxinum)
    b = bin(n)
    print(b)
    a = int(input("denery: "))
    if n == a:
        score += 1
    elif a >= maxinum + 1:
        print("exeeded amount")
        print("the actual answer was", n)
        break
    else:
      print("the actual answer was", n)
      break
  time.sleep(0.3)
  print("")
  print("your score in binary:")
  print(score)

def hexidecimal():
  score = 0
  while True:
    n = random.randint(0,maxinum)
    b = hex(n)
    print(b)
    a = int(input("denery: "))
    if n == a:
        score += 1
    elif a >= maxinum + 1:
        print("exeeded amount")
        print("the actual answer was", n)
        break
    else:
      print("the actual answer was", n)
      break
  time.sleep(0.3)
  print("")
  print("your score in hexidecimal:")
  print(score)


def octal():
  score = 0
  while True:
    n = random.randint(0,maxinum)
    b = oct(n)
    print(b)
    a = int(input("denery: "))
    if n == a:
        score += 1
    elif a >= maxinum + 1:
        print("exeeded amount")
        print("the actual answer was", n)
        break
    else:
      print("the actual answer was", n)
      break
  time.sleep(0.3)
  print("")
  print("your score in octal:")
  print(score)


def mix():
  score = 0
  while True:
    mode = random.randint(0,2)
    n = random.randint(0,maxinum)
    if mode == 0:
      print("binary:")
      b = bin(n)
    elif mode == 1:
      print("hexidecimal:")
      b = hex(n)
    elif mode == 2:
      print("octal:")
      b = oct(n)
    print(b)
    a = int(input("denery: "))
    if n == a:
        score += 1
    elif a >= maxinum + 1:
        print("exeeded amount")
        print("the actual answer was", n)
        break
    else:
      print("the actual answer was", n)
      break
  time.sleep(0.3)
  print("")
  print("your score:")
  print(score)
while True:
  print("Chose your difficulty.")
  print("Their are more difficulties in the sorce code.")
  difficulty = input("easy, medium, hard or legendary? " )
  if difficulty == "easy":
    maxinum = 15
    break
  elif difficulty == "medium":
    maxinum = 63
    break
  elif difficulty == "hard":
    maxinum = 255
    break
  elif difficulty == "legendary":
    maxinum = 1023
    break
  elif difficulty == "brain_fry":
    maxinum = 4095
    break
  elif difficulty == "illigal":
    maxinum = 16383
    break
  elif difficulty == "tsar_bomba":
    maxinum = 65535
    break
  else:
    print("not a difficulty")
print("")
while True:
  print("chose your mode.")
  choice = input("binary, hexidecimal, octal or mix? ")
  if choice == "binary":
    print("")
    binary()
    break
  elif choice == "hexidecimal":
    print("")
    hexidecimal()
    break
  elif choice == "octal":
    print("")
    octal()
    break
  elif choice == "mix":
    print('')
    mix()
    break
  else:
    print("not an option")
    print("")
