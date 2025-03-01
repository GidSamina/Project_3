
import os
from Utils import SCORES_FILE_NAME

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


def add_score(difficulty):
    try:
        if not os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'w') as file:
                file.write('0')

        with open(SCORES_FILE_NAME, 'r+') as file:
            current_score = int(file.read().strip())
            new_score = current_score + POINTS_OF_WINNING(difficulty)
            file.seek(0)
            file.write(str(new_score))
    except Exception as e:
        print(f"Error: {e}")