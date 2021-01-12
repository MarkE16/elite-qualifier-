import time
import random
import sys
import math

# Project - Chatbot
# Tasks - Fix bugs & improve the bot.

# // Variables & Functions //

def login():
  loginAttempts = 5
  for password in passwords:
    if password == correctPass:
      print(f"- {password.capitalize()}")
    else:
      print(f"- {password}")

  passcode = input("In order to log in, type the correct password. ")
  while passcode != correctPass:
    loginAttempts -= 1
    print("LOG-IN ATTEMPTS LEFT:", loginAttempts)
    passcode = input("That's not correct. Try again. ")
    if loginAttempts <= 1:
      print("You typed the wrong password too many times. Wait 10s for the cooldown to end.")
      loginAttempts = 5
      time.sleep(10)

def game():
  global attempts
  botNumber = random.randint(1,10)
  print(f"{botName}: What number am I thinking of?")
  response = int(input("What number 1 - 10? "))
  while response != botNumber:
    attempts += 1
    response = int(input("Wrong. Try again. "))
  print("-----YOU WIN!-----")
  print("Attempts you took:", attempts)
  attempts = 0
  time.sleep(2)

def diceGame():
  botRoll = random.randint(1,6)
  print(f"{botName}: Roll your dice!")
  roll = int(input("Roll... (1 - 6) "))
  if roll == botRoll:
    print("Nice! We both got the same number!")
  else:
    print("Oh. We didn't get the same number.")
  print(f"{botName}'s Roll:", botRoll)
  print("Your roll:", roll)
  input("Press ANY KEY to close.")

def pickupGame():
  print("Numbers:")
  for num in nums:
    randomNums = random.choice(nums)
    print(randomNums, end=" ")
    storedNums.append(randomNums)
  print()
  print(f"{botName}: I dropped numbers! Please, help me pick them up!")
  while True:
    print("Pick up by typing a number (Type 0 for the first number in the list. Type 1 for the second number. Type 2 for third, and so on.). ")
    pickup = int(input("Pick up... "))
    pickups.append(pickup)
    storedNums.pop(pickup)
    if pickup in pickups:
      pass
    print(storedNums)
    if not storedNums:
      break
  print(f"{botName}: Thank you so much for helping me, {username}!!")
  time.sleep(3)

def mathQuestion():
  first = random.randint(1,100)
  second = random.randint(1,100)
  if selectedEquation == "add":
    sum = first + second
    print(f"{botName}: What does {first} + {second} equal?")
    answer = int(input("Answer... "))
    while answer != sum:
      answer = int(input("Wrong. Try again. "))
  elif selectedEquation == "subtract":
    subtotal = first - second
    print(f"{botName}: What does {first} - {second} equal?")
    answer = int(input("Answer... "))
    while answer != subtotal:
      answer = int(input("Wrong. Try again. "))
  elif selectedEquation == "multiply":
    total = first * second
    print(f"{botName}: What does {first} x {second} equal?")
    answer = int(input("Answer... "))
    while answer != total:
      answer = int(input("Wrong. Try again. "))
  elif selectedEquation == "modulus":
    remain = first % second
    print(f"{botName}: What does {first} % {second} equal?")
    answer = int(input("Answer... "))
    while answer != remain:
      answer = int(input("Wrong. Try again. "))
  elif selectedEquation == "power":
    power = pow(first, second)
    print(f"{botName}: What does {first} with the power of {second} equal?")
    answer = int(input("Answer... "))
    while answer != power:
      answer = int(input("Wrong. Try again. "))
  print(f"{botName}: Good job! That's right!")

def heading(text):
  print("----------")
  print(text)
  print("----------")

nums = "1234567890"
storedNums = []
pickups = []
programActive = True
conversationGoing = True
botName = "ChatBot"
attempts = 0

welcomeMessages = [
  "Hi there user!",
  "Oh, hello there.",
  "Hi!"
]
welcome = random.choice(welcomeMessages)

messages = [
  "How're you doing?",
  "How's the weather?",
  "Did you have a good day?",
  "Did you do anything fun today?",
  "Amazing!",
  "That's cool.",
  "Ah... I see...",
  "That's fun!",
  "Let's play a game.",
  "Let's roll a dice.",
  "Oh No!",
  "I have a math question."
]
selectedMessage = random.choice(messages)

passwords = [
  'abc123',
  'house',
  'program',
  'games',
  "work"
]
correctPass = random.choice(passwords)

equations = [
  "add",
  "subtract",
  "multiply",
  "modulus",
  "power"
]
selectedEquation = random.choice(equations)

# // Main Code //

username = input("Input your username... ")
final = input(f"USERNAME: {username}. Is this correct? (y/n) ")
while final == 'n':
  username = input("Re-enter your username. ")
  final = input(f"USERNAME: {username}. Is this correct? (y/n) ")
if final == 'y':
  pass
else:
  sys.exit("Not a valid choice. Closed the program.")
login()
print("Password accepted!")
while programActive:
  heading("|| Welcome to the ChatBot! v 1.0 ||")
  print("Welcome,", username, "!")
  print(
    "You can do 2 things currently:\n"
    "1. Talk with Chatbot\n"
    "2. Exit the program"
  )
  decision = input("Whatcha wanna do? (Type the number) ")
  if decision == '1':
    print(f"{botName}: {welcome}")
    print("Type 'quit' to leave whenever!")
    respond = input("Respond... ")
    while conversationGoing:
      selectedMessage = random.choice(messages)
      print(f"{botName}: {selectedMessage}")
      response = input("Respond... ")
      if selectedMessage == "Let's play a game.":
        game()
      elif selectedMessage == "Let's roll a dice.":
        diceGame()
      elif selectedMessage == "Oh No!":
        pickupGame()
      elif selectedMessage == "I have a math question.":
        mathQuestion()
      if response == 'quit':
        break
  elif decision == '2':
    sys.exit("The program was closed.")

# Program coded by Mark E.