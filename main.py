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

game_images = [rock, paper, scissors]

player = int(input("What to you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n"))

if player == 0 or player == 1 or player == 2:
    print(game_images[player])
    computer = random.randint(0, 2)
    print(game_images[computer])

    if computer == 0:
        if player == 0:
            print("It's a draw.")
        elif player == 1:
            print("You won!")
        elif player == 2:
            print("You lost. Try again.")
        else:
            print("You entered an invalid number. You lose.")
    elif computer == 1:
        if player == 0:
            print("You lost. Try again.")
        elif player == 1:
            print("It's a draw.")
        elif player == 2:
            print("You won!")
        else:
            print("You entered an invalid number. You lose.")
    elif computer == 2:
        if player == 0:
            print("You won!")
        elif player == 1:
            print("You lost. Try again.")
        elif player == 2:
            print("It's a draw.")
        else:
            print("You entered an invalid number. You lose.")
else:
    print("You Entered an Invalid number. You lose.")
# if player == 0:
#     print("You chose:" + rock)
# elif player == 1:
#     print("You chose:" + paper)
# elif player == 2:
#     print("You chose:" + scissors)
# else:
#     print("Please enter a valid option.")


