from test_suite import exercise_1_tests

# Exercise 1
# In this exercise we will set up the variables needed to begin a game
# of hangman.
# Complete the variables in the __init__ function that have TODO comments
# above them and check to make sure that all of the test cases pass


class HangMan:
    def __init__(self, word: str) -> None:
        self.word = word

        self.guesses_remaining = 6
        # TODO: set complete_word to be a list of '_' characters that matches the length
        # of the word
        self.completed_word = None
        # TODO: Set letters to be a list of each letter in the word being guesses
        self.letters = None
        self.guessed = set()


if __name__ == '__main__':
    exercise_1_tests(HangMan)
