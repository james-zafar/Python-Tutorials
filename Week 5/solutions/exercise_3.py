# Exercise 3 - Solution

import random


class HigherOrLower:
    def __init__(self, upper_bound: int, max_rounds: int) -> None:
        self.upper_bound = upper_bound
        self.max_rounds = max_rounds

        self.play_game()

    def get_user_input(self) -> str:
        choice = str(input('Would you like to Higher or Lower? '))
        if choice.lower() != 'higher' and choice.lower() != 'lower':
            print('Error: You must choose either \'higher\' or \'lower\'')
            return self.get_user_input()
        return choice.lower()

    def play_game(self):
        random_number = random.randint(0, self.upper_bound)
        round_no = 0
        while round_no < self.max_rounds:
            print(f'You are currently on round {round_no}, the number for this round is: {random_number}')
            choice = self.get_user_input()
            new_random_number = random.randint(0, self.upper_bound)
            if (choice == 'higher' and new_random_number > random_number) or (choice == 'lower' and new_random_number < random_number):
                print(f'Correct! The number was \'{new_random_number}\'')
                round_no += 1
                random_number = new_random_number
            else:
                print(f'Unlucky, you chose {choice}, but the number was {new_random_number}!')
                print(f'You managed to reached round {round_no}/{self.max_rounds}')
                break
        if round_no == self.max_rounds:
            print(f'Congratulations, you managed to pass all {self.max_rounds} rounds!')


if __name__ == '__main__':
    HigherOrLower(100, 2)
