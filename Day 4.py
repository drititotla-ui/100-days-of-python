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

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
player=input("Choose your weapon!type 0 for rock, 1 for paper and 2 for scissors")
if player=="0":
    print(rock)
elif player=="1":
    print(paper)
else:
    print(scissors)
computer=[rock, paper , scissors]
computer_choice= random.choice(computer)
print(computer_choice)

if computer_choice==rock:
    if player=="0":
        print("match draw.")
    elif player=="1":
        print("you win!")
    else:
        print("you lose. Try again")
elif computer_choice==paper:
    if player=="0":
        print("you lose")
    elif player== "1":
        print("match draw")
    else:
        print("You win!")
else:
    if player=="0":
        print("you win!")
    elif player=="1":
        print(" you lose")
    else:
        print("match draw")