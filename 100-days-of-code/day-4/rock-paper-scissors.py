from random import randint

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

MESSAGE_USER_WIN = 'You win!'
MESSAGE_COMPUTER_WIN = 'You lose!'
MESSAGE_DRAW = 'It\'s a Draw!'
MESSAGE_INVALID_NUMBER = 'You typed an invalid number. You lose!'

GAME_IMAGES = [rock, paper, scissors]

print('What do you choose?')

user_choice = int(input('Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = randint(0, 2)

if 0 <= user_choice <= 2:
    print(f'User choose\n {GAME_IMAGES[user_choice]}')

print(f'Computer choose\n {GAME_IMAGES[computer_choice]}')

if user_choice >= 3 or user_choice < 0:
    print(MESSAGE_INVALID_NUMBER)
elif user_choice == 0 and computer_choice == 2:
    print(MESSAGE_USER_WIN)
elif computer_choice == 0 and user_choice == 2:
    print(MESSAGE_COMPUTER_WIN)
elif computer_choice > user_choice:
    print(MESSAGE_COMPUTER_WIN)
elif user_choice > computer_choice:
    print(MESSAGE_USER_WIN)
elif user_choice == computer_choice:
    print(MESSAGE_DRAW)
