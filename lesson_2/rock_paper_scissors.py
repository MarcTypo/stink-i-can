import random

def prompt(message):
    print(f' ==> {message}')

def display_message(player, computer):
    if ((player == 'rock' and computer == 'scissorrs') or 
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')):
            prompt('You win!')
            
    elif ((player == 'rock' and computer == 'paper') or
        (player == 'scissors' and computer == 'rock') or 
        (player == 'paper' and computer == 'scissors')):
        prompt('You lose. ')

    else:
        prompt(f'You chose {choice} and the computer chose {computer}. So it is a tie.')

VALID_CHOICES = ['rock', 'paper', 'scissors']

while True:

    prompt(f'Welcome to Rock, Paper, Scissors. Please enter {', '.join(VALID_CHOICES).lower()}.')
    choice = input()

    if choice not in VALID_CHOICES:
        print('This is not a valid choice. Please select a vlaid choice.')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)


    display_message(choice, computer_choice)

    #Break if user does not want to play 
    prompt('Do you want to play again.(Y/N)?')
    answer = input().lower()
    while True: 
         if answer.startswith('n') or answer.startswith('y'):
              break
         prompt("Please enter 'y' or 'n'.")
         answer = input().lower

    if answer[0] == 'n':
         break
