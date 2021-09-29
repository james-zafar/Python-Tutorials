import random

import requests

from hangman.test_suite import exercise_4_tests

# In this exercise, we will complete the implementation of hangman.
# The final thing to implement is the case where the user has correctly guessed a letter.
# We will update the game state in a function called update_game. The implementation should
# follow these steps:
# 1 - First write a message to the console informing them their guess is correct using the below
#     message:
#       The letter <<INSERT GUESS>> is correct!
# 2 - Call the update_game function
# 3 - in update_game, replace the relevant _ in 'completed_word' with the letter the user has
#     correctly guessed, and print to the console the updated word
# 4 - In play_game after updating the game state, check to see if the user has correctly guessed
#     the complete word. If they have, output the following message to the console:
#       'Congratulation, you won with <<Insert remaining guesses>> guesses left!
# 5 - else if the user is out of guesses, break from the loop and output the following messages to
#     the console:
#       print('You are out of guesses! Better luck next time.')
#       print(f'The correct answer was <<INSERT COMPLETED WORD>>')
# 6 - Verify your solution is correct by running the file and checking all of the automated tests pass
# 7 - Once all tests are passed change line 70 from:
#       exercise_4_tests(HangMan), to:
#       HangMan()

# Extension: Can you enhance the implementation ask the user to provide a word to use in the game, and if
#   the choose not to provide one, auto-generate a word from the dictionary implemented in an earlier
#   exercise.

# NB: It is important the log messages match the templates as these will be validated in the tests


class HangMan:
    def __init__(self, word: str = '') -> None:
        self.word = word.lower()
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

    def update_game(self) -> None:
        ...

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
    exercise_4_tests(HangMan)
