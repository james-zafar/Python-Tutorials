import random

import requests

from hangman.test_suite import exercise_3_tests

# We are not ready to start implementing the game. We will do this in 2 stages:
# Firstly, we we gather user input and deal with incorrect guesses, the in the
# next exercise we will update the game based on correct guesses.

# Exercises:
# 1 - Begin by printed the word being guessed with the letter hidden as a
#   string (self.completed_words). The output should not have the square brackets,
#   and/or the commas present when printing a list
# 2 - While the user has guesses remaining, enter a loop to keep asking for guesses
# 3 - Gather user input as a lower case string
# 4 - Check if the letter has already been guessed; is it in self.guessed? If so,
#   output the below string and skip the rest of this loop iteration, and if not add
#   it to guessed.
#   'Error: The letter <GUESS> has already been guessed'
# 5 - Check whether or not the input letter is a correct guess (is the letter part of the
#   final word?), if not write the below error message to the console:
#   That guess is incorrect. You have {guesses_remaining} guesses remaining
# 6 - call the play_game function from the __init__ function
# 7 - Check that your solution is correct by running the code and verifying that all test
#   cases pass

# NB: It is important the log messages match the templates as these will be validated in the tests


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

    def play_game(self) -> None:
        ...


if __name__ == '__main__':
    exercise_3_tests(HangMan)
