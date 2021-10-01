import math
from typing import Final
from contextlib import suppress

from connect_4.test_suite import exercise_1_tests

# Exercise 3
# Feel free to continue using your solution from the previous exercise. If you did
# not manage to solve the previous exercise, a solution has been provided for you to
# allow you to continue with the project.
# In this exercise we will implement the get_move and update_board functions.
# get_move should do the following:
#   1 - Provide the current player with the following prompt to get their input:
#       <<PLAYER_NAME>>, enter a column (1 - 7):
#   2 - Check if the user input is a number, if not then output the following error
#       message and re-prompt them for input:
#       print('Error: You must enter a number')
#   3 - If the input is a valid number, check that it is a number between 1 and 7, if
#       not output the following error message and re-prompt them for input
#       print('Error: You must choose a column between 1 and 7')
#   4 - Repeat steps 2 and 3 until valid input is provided
#   5 - Return the input number - 1 (this will become important later)
# Implement update_board to do the following:
#   1 - Loop through the rows in the board, starting at the bottom of the board. Tip:
#       Think about how two dimensional arrays are structured and how the board appears
#       to the user to work out how to do this
#   2 - If the column in the current row is empty (i.e. is equal to '_') then change the
#       value of the board at the current row/column to be the symbol passed to the function
#   3 - Once an empty position has been found and the board updated, call the player_has_won
#       function. We will implement this in the next exercise, then break from the loop.


class ConnectFour:
    def __init__(self) -> None:
        self.ROWS: Final[int] = 6
        self.COLUMNS: Final[int] = 7
        self.board = [['_' for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

        self.player_1 = None  # type: str
        self.player_2 = None  # type: str
        self.player_1_symbol = 'X'
        self.player_2_symbol = 'O'
        self.game_over = False

        self.init_game()

    def init_game(self):
        self.player_1 = str(input('Enter the name of player 1: '))
        self.player_2 = str(input('Enter the name of player 2: '))

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
        names = [(self.player_1, self.player_1_symbol), (self.player_2, self.player_2_symbol)]
        turns = 0
        while not self.game_over:
            self.print_board()
            current_player, symbol = names[math.floor(turns % 2)]
            user_choice = self.get_move(current_player)
            self.update_board(user_choice, symbol)
            turns += 1

        self.print_board()
        winner = names[math.floor((turns - 1) % 2)][0]
        print(f'Congratulations {winner} wins!')


if __name__ == '__main__':
    exercise_1_tests(ConnectFour)
