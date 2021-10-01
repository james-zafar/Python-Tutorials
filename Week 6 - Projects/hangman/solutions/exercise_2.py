import random

import requests

from hangman.test_suite import exercise_2_tests

# IMPORTANT: To run the solutions, you must run the following to run hangman
# as a package:
# python -m hangman.solutions.exercise_2
# from outside of the hangman directory


class HangMan:
    def __init__(self, word: str = None) -> None:
        self.word = word
        if not self.word:
            self.generate_word()

        self.guesses_remaining = 6
        self.completed_word = ['_'] * len(self.word)
        self.letters = list(self.word)
        self.guessed = set()

    def generate_word(self) -> None:
        response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
        words = response.content.splitlines()
        self.word = random.choice(words).decode("utf-8").lower()


if __name__ == '__main__':
    exercise_2_tests(HangMan)
