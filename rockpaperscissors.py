rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random 

list = [rock, paper, scissors]

you = int(input("Which do you choose? Type 0 for rock, 1 for paper, 2 for scissors. "))


print("You:")

if you == 0:
  print(rock)
if you == 1:
  print(paper)
if you == 2:
  print(scissors)
if you >= 3:
  print("Invalid number. You lose")

print("Computer:")

computer = random.choice(list)
print(computer)

if you == 0 and computer == rock:
  print("Draw")
if you == 1 and computer == paper:
  print("Draw")
if you == 2 and computer == scissors:
  print("Draw")
if you == 0 and computer == scissors:
  print("You win!")
if you == 0 and computer == paper:
  print("You lose.")
if you == 2 and computer == paper:
  print("You win!")
if you == 2 and computer == rock:
  print("You lose.")
if you == 1 and computer == rock:
  print("You win!")
if you == 1 and computer == scissors:
  print("You lose.")
