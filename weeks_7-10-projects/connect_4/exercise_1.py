import math
from typing import Final
from contextlib import suppress

from test_suite import exercise_1_tests

# Welcome to the Connect 4 project.
# We will build a text based implementation of connect 4 in the next <<N>> exercises.
# The basic building blocks for the game have been provided in the class below, you
# will complete the implementations of these functions in the upcoming exercises.

# Exercise 1 - Create an empty connect four board and assign it to the board variable
#   in the init function. An empty board should be of shape (self.ROWS, self.COLUMNS).
#   Each element should be an underscore (_)

# Exercise 2 - Implement the init game function. This function should ask the user to
#   input names for player 1 and 2 and assign them to the player_1 and player_2 class
#   attributes.


class ConnectFour:
    def __init__(self) -> None:
        self.ROWS: Final[int] = 6
        self.COLUMNS: Final[int] = 7
        self.board = None ## TODO: Fill this value

        self.player_1 = None  # type: str
        self.player_2 = None  # type: str
        self.player_1_symbol = 'X'
        self.player_2_symbol = 'O'
        self.game_over = False

        self.init_game()

    def init_game(self):
        pass

    def player_has_won(self, row: int, col: int, symbol: str) -> None:
        # Horizontal Right Check
        with suppress(IndexError):
            ...

    def get_move(self, player_name: str) -> int:
        pass

    def update_board(self, column: int, symbol: str) -> None:
        pass

    def print_board(self):
        fmt = '\t'.join('{{:{}}}'.format(row) for row in [1] * 7)
        table = [fmt.format(*row) for row in self.board]
        print('\n'.join(table))

    def play_game(self):
        pass


if __name__ == '__main__':
    exercise_1_tests(ConnectFour)