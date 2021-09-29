import random

import requests

from hangman.test_suite import exercise_4_tests

# IMPORTANT: To run the solutions, you must run the following to run hangman
# as a package:
# python -m hangman.solutions.exercise_4
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

        self.play_game()

    def generate_word(self) -> None:
        response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
        words = response.content.splitlines()
        self.word = random.choice(words).decode("utf-8").lower()

    def update_game(self, letter: str) -> None:
        indices = [idx for idx, char in enumerate(self.letters) if char == letter]
        for idx in indices:
            self.completed_word[idx] = letter
        print(''.join(self.completed_word))

    def play_game(self) -> None:
        print(''.join(self.completed_word))
        while self.guesses_remaining > 0 and '_' in self.completed_word:
            guess = str(input('Enter a letter to guess: ')).lower()
            if guess in self.guessed:
                print(f'Error: The letter {guess} has already been guessed')
                continue
            self.guessed.add(guess)
            if guess not in self.letters:
                self.guesses_remaining -= 1
                print(f'That guess is incorrect. You have {self.guesses_remaining} guesses remaining')
            else:
                print(f'The letter \'{guess}\' is correct!')
                self.update_game(guess)

        if self.guesses_remaining == 0:
            print('You are out of guesses! Better luck next time.')
            print(f'The correct answer was {"".join(self.letters)}')
        else:
            print(f'Congratulation, you won with {self.guesses_remaining} guesses left!')


if __name__ == '__main__':
    exercise_4_tests(HangMan)
    # word = str(input('Enter a word, or press enter to skip this stage: '))
    # HangMan(word)
