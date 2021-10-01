from hangman.test_suite import exercise_1_tests

# IMPORTANT: To run the solutions, you must run the following to run hangman
# as a package:
# python -m hangman.solutions.exercise_1
# from outside of the hangman directory


class HangMan:
    def __init__(self, word: str) -> None:
        self.word = word

        self.guesses_remaining = 6
        self.completed_word = ['_'] * len(self.word)
        self.letters = list(self.word)
        self.guessed = set()


if __name__ == '__main__':
    exercise_1_tests(HangMan)
