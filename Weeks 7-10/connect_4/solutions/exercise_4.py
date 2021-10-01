import math
from typing import Final
from contextlib import suppress

# IMPORTANT: To run the solutions, you must run the following to run connect_4
# as a package:
# python -m connect_4.solutions.exercise_4
# from outside of the connect_4 directory


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
        self.play_game()

    def player_has_won(self, row: int, col: int, symbol: str) -> None:
        # Horizontal Right Check
        with suppress(IndexError):
            if (self.board[row][col + 1] == symbol and self.board[row][col + 2] == symbol
                    and self.board[row][col + 3] == symbol):
                self.game_over = True
        # Horizontal Left Check
        with suppress(IndexError):
            if (self.board[row][col - 1] == symbol and self.board[row][col - 2] == symbol
                    and self.board[row][col - 3] == symbol):
                self.game_over = True
        # Vertical Check
        with suppress(IndexError):
            if (self.board[row + 1][col] == symbol and self.board[row + 2][col] == symbol
                    and self.board[row + 3][col] == symbol):
                self.game_over = True
        # Left Diagonal Check
        with suppress(IndexError):
            if (self.board[row + 1][col - 1] == symbol and self.board[row + 2][col - 2] == symbol
                    and self.board[row + 3][col - 3] == symbol):
                self.game_over = True
        # Right Diagonal Check
        with suppress(IndexError):
            if (self.board[row + 1][col + 1] == symbol and self.board[row + 2][col + 2] == symbol
                    and self.board[row + 3][col + 3] == symbol):
                self.game_over = True

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
    ConnectFour()
