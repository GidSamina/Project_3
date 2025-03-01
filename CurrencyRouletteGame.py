import requests
import random

difficulty = 3

class CurrencyGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self, usd_amount):
        response = requests.get('https://v6.exchangerate-api.com/v6/94355e7ba2e92a1e6ee5939d/latest/USD')
        rate = response.json()['conversion_rates']['ILS']
        total_value = usd_amount * rate
        interval = (total_value - (5 - self.difficulty), total_value + (5 - self.difficulty))
        return interval

    def get_guess_from_user(self, usd_amount):
        return float(input(f'Guess the value of {usd_amount} USD in ILS: '))

    def play(self):
        usd_amount = random.randint(1, 100)
        interval = self.get_money_interval(usd_amount)
        guess = self.get_guess_from_user(usd_amount)
        return interval[0] <= guess <= interval[1]

game = CurrencyGame(difficulty)
result = game.play()
print('You won!' if result else 'You lost!')
