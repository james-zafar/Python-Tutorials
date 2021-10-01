import random

import requests

from hangman.test_suite import exercise_3_tests

# IMPORTANT: To run the solutions, you must run the following to run hangman
# as a package:
# python -m hangman.solutions.exercise_3
# from outside the hangman directory


class HangMan:
    def __init__(self, word: str = '') -> None:
        self.word = word.lower()
        if not self.word:
            self.generate_word()

        self.guesses_remaining = 6
        self.completed_word = ['_'] * len(self.word)
        self.letters = list(self.word)
        self.guessed = set()

        self.play_game()

    def generate_word(self) -> None:
        response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
        words = response.content.splitlines()
        self.word = random.choice(words).decode("utf-8").lower()

    def play_game(self) -> None:
        print(''.join(self.completed_word))
        while self.guesses_remaining > 0:
            guess = str(input('Enter a letter to guess: ')).lower()
            if guess in self.guessed:
                print(f'Error: The letter {guess} has already been guessed')
                continue
            self.guessed.add(guess)
            if guess not in self.letters:
                self.guesses_remaining -= 1
                print(f'That guess is incorrect. You have {self.guesses_remaining} guesses remaining')
                continue


if __name__ == '__main__':
    exercise_3_tests(HangMan)
