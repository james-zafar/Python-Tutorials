from test_suite import exercise_2_tests

# Exercise 2
# It would be nice if the user did not have to manually provide a word
# every time a game begins, and can instead choose to have a word randomly
# generated.
# We will choose a random word from a list of 10,000 words if the user chooses
# not to provide one from this source:
# "https://www.mit.edu/~ecprice/wordlist.10000"

# Exercises:
# 1 - Change the argument 'word' to __init__ to be optional, giving it an appropriate
#   default value
# 2 - If the word provided is None, call the generate_word function to set self.word
#   to a randomly chosen value
# 3 - Implement generate_word to select a random word from the word provided by
#   "https://www.mit.edu/~ecprice/wordlist.10000". To do this you will need to:
#   - Use 'requests' to execute a GET request on the URL
#   - The response will be a list of utf-8 encoded strings of length 10,000
#   - To unpack the response you can use response.content.splitlines()
#   - Use a library of your choosing to select a random word to use
#   - As the words are encoded, you will need to call <word>.decode("utf-8")
#       on the word that has been selected
#   - Make the word all lowercase for consistency
# 4 - Run your solution and verify that all test cases pass


class HangMan:
    def __init__(self, word: str) -> None:
        self.word = word

        self.guesses_remaining = 6
        self.completed_word = ['_'] * len(self.word)
        self.letters = list(self.word)
        self.guessed = set()

    def generate_word(self) -> None:
        ...


if __name__ == '__main__':
    exercise_2_tests(HangMan)
