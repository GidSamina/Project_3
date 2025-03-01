#Welcome function
from Score import add_score
# from UpdateMainGame import game_choice



def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\n'
          f'Here you can find many cool games to play.')

#Load game function
def load_game():
    game_choice = input(f'Please choose a game to play: \n'
        '1. Memory Game (a sequence of numbers will appear for 1 second and you have to guess it back)\n'
        '2. Guess Game (guess a number and see if you chose like the computer) \n'
        '3. Currency Roulette: (try and guess the value of a random amount of USD in ILS) \n' )
    if game_choice not in ['1', '2', '3']:
        print('Please enter a number between 1 and 3.')
        return
    # print(game_choice)

    difficulty_choice = input(f'Please choose game difficulty from 1 to 5: ')
    if difficulty_choice not in ['1', '2', '3', '4', '5']:
        print('Please enter a number between 1 and 5.')
        return

    # print(difficulty_choice)
#
#     if game_choice == '1':
#         from MemoryGame import play
#         if play(int(difficulty_choice)):
#             add_score()
# load_game()
#
#     if game_choice == '2':
#         from GuessGame import GuessGame
#         game = GuessGame(int(difficulty_choice))
#         add_score()
#         game.play()
# game.play()

#     if game_choice == '3':
#         from CurrencyRouletteGame import result
#         if result(int(difficulty_choice)):
#             add_score()
# result()