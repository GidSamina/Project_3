from Live import welcome, load_game
import random
import time
from time import sleep

welcome('Guy')

game_choice = input(f'Please choose a game to play: \n'
    '1. Memory Game (a sequence of numbers will appear for 1 second and you have to guess it back)\n'
    '2. Guess Game (guess a number and see if you chose like the computer) \n'
    '3. Currency Roulette: (try and guess the value of a random amount of USD in ILS) \n' )
if game_choice not in ['1', '2', '3']:
    print('Please enter a number between 1 and 3.')

diff_choice = input(f'Please choose game difficulty from 1 to 5: ')
if diff_choice not in ['1', '2', '3', '4', '5']:
    print('Please enter a number between 1 and 5.')

difficulty = int(diff_choice)


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    return [int(input(f'Enter number {i+1}: ')) for i in range(difficulty)]

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print('Remember this sequence:', sequence)
    time.sleep(0.7)
    print('\n' *20)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_list):
        print('You won')
    else:
        print('You lost')

play(difficulty)


from CurrencyRouletteGame import CurrencyGame
CurrencyGame(difficulty=3)
