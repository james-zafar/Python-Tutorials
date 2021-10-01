from typing import Final
from contextlib import suppress


# Exercise 2
# Feel free to continue using your solution from the previous exercise. If you did
# not manage to solve the previous exercise, a solution has been provided for you to
# allow you to continue with the project.
# In this exercise we will implement the play_game function.
# The function must do the following:
#   - Print the board (the print_board function has been provided for you)
#   - Fetch the name and symbol of the player whose turn it is from the names variable
#   - Ask the user for input a column number
#   - Update the board - for now you may call self.update_board() for this step which we
#       will implement in a later exercise
#   - Repeat the above steps until a player has won the game. A player has won when
#       self.game_over is True
#   - When a player has won, print the board once more, then fetch the name of the winner
#       and print the following message to the console:
#       'Congratulations <<WINNERS NAME>> wins!


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


if __name__ == '__main__':
    ConnectFour()
