import math
from typing import Final
from contextlib import suppress

from connect_4.test_suite import exercise_1_tests

# Exercise 4
# Feel free to continue using your solution from the previous exercise. If you did
# not manage to solve the previous exercise, a solution has been provided for you to
# allow you to continue with the project.
# In this exercise we will implement the player_has_won function.
# player_has_won runs after every board update and should check if the current player
#   has won. The function takes three parameters; the row, column and symbol. The row
#   and column refer to the location of the last board update, and the symbol relates
#   to the current player.
#   The function body currently contains the following code:
#       with suppress(IndexError):
#           ...
#   The with statement clarifies code that previously would use try...finally or
#   try...except blocks to ensure that clean-up code is executed. suppress is a context
#   manager provided as part of the standard library, and IndexError is specify the error
#   we want to suppress. You can write code inside this with block to suppress an IndexError,
#   should one arise. Feel free to ask questions during the lessons if you don't understand or
#   have any other questions.

#   Try to think of a way to check if a player has won without iterating over the entire board,
#   as a hint, think about how you can use the arguments passed to the function to check a small
#   subset of the complete board.


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
        user_choice = input(f'{player_name}, enter a column (1 - 7): ')
        if not user_choice.isdigit():
            print('Error: You must enter a number')
            return self.get_move(player_name)
        if int(user_choice) < 1 or int(user_choice) > 7:
            print('Error: You must choose a column between 1 and 7')
            return self.get_move(player_name)

        return int(user_choice) - 1

    def update_board(self, column: int, symbol: str) -> None:
        for row in range(self.ROWS - 1, 0, -1):
            if self.board[row][column] == '_':
                self.board[row][column] = symbol
                self.player_has_won(row, column, symbol)
                break

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
