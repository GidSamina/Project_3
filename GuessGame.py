import random

difficulty = 100

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                return int(input(f'Guess a number between 1 and {self.difficulty}: '))
            except ValueError:
                print('Please enter a valid integer.')

    def compare_results(self, user_guess):
        return user_guess == self.secret_number

    def play(self):
        self.generate_number()
        while True:
            user_guess = self.get_guess_from_user()
            if self.compare_results(user_guess):
                print(f'Correct! The answer was {self.secret_number}.')
                break
            elif user_guess < self.secret_number:
                print('Too low , try again!')
            else:
                print('Too High , try again!')


game = GuessGame(difficulty)
game.play()
