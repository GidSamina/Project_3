import random
import time
from time import sleep


difficulty = 3

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

#play(difficulty)