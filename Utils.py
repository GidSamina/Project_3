import os

# A string representing a file name. By default “Scores.txt”
SCORES_FILE_NAME = 'Scores.txt'
if not os.path.exists(SCORES_FILE_NAME):
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write('0')


# A number representing a bad return code for a function.
BAD_RETURN_CODE = -1


# Screen_cleaner - A function to clear the screen (useful when playing memory game or
# before a new game starts).
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
