import random

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
myhand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
hands = [rock, paper, scissors]
com_hand = random.randint(0,2)

if myhand == 0:
    print("You choose")
    print(rock)
    if com_hand == 0:
        print("Computer Choose")
        print(rock)
        print("Its draw!")
    elif com_hand == 1:
        print("Computer Choose")
        print(paper)
        print("You loose")
    else:
        print("Computer Choose")
        print(scissors)
        print("You won")
elif myhand == 1:
    print("You choose")
    print(paper)
    if com_hand == 0:
        print("Computer Choose")
        print(rock)
        print("You won")
    elif com_hand == 1:
        print("Computer Choose")
        print(paper)
        print("Its draw!")
    else:
        print("Computer Choose")
        print(scissors)
        print("You loose")
elif myhand == 2:
    print("You choose")
    print(scissors)
    if com_hand == 0:
        print("Computer Choose")
        print(rock)
        print("You loose")
    elif com_hand == 1:
        print("Computer Choose")
        print(paper)
        print("You won")
    else:
        print("Computer Choose")
        print(scissors)
        print("Its draw!")
else:
    print("Invalid Inputs")