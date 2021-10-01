import random

import requests

from hangman.test_suite import exercise_5_tests

# Exercise 5
# We now have a fully functional hangman game! We can now look at ways to enhance and
# improve the initial implementation. One potential feature we could enhance is the
# handling of user input. At the moment we assume the user will enter a valid character
# but this may not be the case. In this exercise, we will enhance this feature to validate
# the user input before continuing with the game.
# Exercises
# 1 - Change the play_game function to fetch user input from the get_user_input function
# 2 - In get_user_input, check that the string is a single character a-z, not including
#   numbers and if not, output the following error message and ask the user to provide
#   input again
#   Error: '<<INSERT INPUT>>' is not a valid character
# 3 - Change play_game to not check if the letter the user input has already been guessed
#   and instead check this in the get_user_input function
# 4 - Validate that your solution is correct by running the code and checking that all
#   test cases have passed

# Extension: Can you think of any other ways to enhance the implementation of hangman?


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

    def get_user_input(self) -> str:
        ...

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
    exercise_5_tests(HangMan)
    word = str(input('Enter a word, or press enter to skip this stage: '))
    HangMan(word)
