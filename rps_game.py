import random


# Welcome to the python Rock Paper Scissors Game
print("Welcome to the python Rock Paper Scissors Game")

# define global variables
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
# create a list to hold all variables
options = [rock, paper, scissors]

# create an input to retrive user's option
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
print("you chose: \n", options[user_choice])

# generate computer's option via the random function
computer_choice = random.randint(0, 2)
print("computer chose: \n", options[computer_choice])

# game logic block
if user_choice >= 3 or user_choice < 0:
    print("Invalid input")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif user_choice < computer_choice:
    print("You lose")
elif user_choice == computer_choice:
    print("It's a draw")



