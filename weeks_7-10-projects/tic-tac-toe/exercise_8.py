import random
from pathlib import Path
from typing import cast
import pandas as pd

from test_suite import testable


# Exercise 8 - Refactoring II
# In this exercise we will do some more refactoring to split the code into more
# meaningful classes.
# There are three distinct requirements for a game of TicTacToe.
#  - Players
#  - A board
#  - The game itself
# Each of these act independently of each other, and as such could be implemented
# as independent classes.
# The Player class has been provided for you, and you should not need to edit this.
# The Board class has been partially provided. __str__ should replace print_board,
# and the board has been initialised for you in the __init__. You will implement the
# other functions during this exercise.

# Exercises:
#   1 - Change TicTacToe to populate self.player_one and self.player_two with instances
#       of the Player class when they are initialised instead of storing the name and
#       symbol in separate variables.
#   2 - Update play_game as appropriate to get the name/symbols from the Player classes
#       and remove player_one_symbol and player_two_symbol from the __init__.
#   3 - Change the board attribute in the __init__ of TicTacToe to instead use an instance
#       of the Board class.
#   4 - Remove print_board from TicTacToe and replace calls with it to print(str(self.board))
#   5 - Use the existing code from update_board and game_is_over to help implement the
#       update_cell and game_over function in the Board class.
#       NB: update_cell in Board should not automatically call game_over.
#   6 - Remove update_board and game_is_over from the TicTacToe class and use the new functions
#       from the Board class.
#   7 - Implement the cell_is_empty function in Board and change is_valid_move to use
#       this new function.
#   8 - Update get_ai_move to use self.board.grid to fetch the grid when searching for empty cells
#   8 - Test your solution and make sure the game still works!


class Player:
    def __init__(self, name: str, symbol: str):
        self._name = name
        self._symbol = symbol

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbol(self) -> str:
        return self._symbol


class Board:
    def __init__(self):
        self._board = [['_' for _ in range(3)] for _ in range(3)]

    @property
    def grid(self) -> list[list[str]]:
        return self._board

    def cell_is_empty(self, coordinates: tuple[int, int]) -> bool:
        pass

    def update_cell(self, coordinates: tuple[int, int], symbol: str) -> 'Board':
        pass

    def game_over(self, last_move: tuple[int, int], symbol: str) -> bool:
        pass

    def __str__(self) -> str:
        fmt = '\t'.join('{:1}' for _ in range(3))
        table = [fmt.format(*row) for row in self._board]
        return '\n'.join(table)


class TicTacToe:
    def __init__(self) -> None:
        self.DATABASE_FILE = 'tic_tac_toe.csv'

        self.board = [['_' for _ in range(3)] for _ in range(3)]
        self.database = None  # type: pd.DataFrame
        self.player_one = None  # type: Player
        self.player_two = None  # type: Player
        self.player_one_symbol = 'O'
        self.player_two_symbol = 'X'
        self.game_over = False

        self.init_game()
        self.play_game()

    def init_game(self) -> None:
        self.init_db()
        self.player_one = str(input('Enter the name of Player 1: '))
        if self.player_one not in self.database.Name.values:
            self.insert_into_database(self.player_one)

        self.player_two = str(input('Enter the name of Player 2, or press enter to play against the computer: '))
        if self.player_two and self.player_two not in self.database.Name.values:
            self.insert_into_database(self.player_two)

    def init_db(self) -> None:
        path = Path(self.DATABASE_FILE)
        if path.is_file():
            self.database = pd.read_csv(path)
        else:
            self.database = pd.DataFrame(columns=['Name', 'Wins', 'Losses'])

    @testable
    def insert_into_database(self, name: str) -> None:
        row = [name, 0, 0]
        self.database.loc[-1] = row
        self.database.index = self.database.index + 1
        self.database = self.database.sort_index()

    def update_db(self, name: str, won: bool) -> None:
        if won:
            self.database.loc[self.database.Name == name, 'Wins'] += 1
        else:
            self.database.loc[self.database.Name == name, 'Losses'] += 1

    def save_db(self) -> None:
        self.database.to_csv(self.DATABASE_FILE, index=False)

    def print_board(self) -> None:
        fmt = '\t'.join('{:1}' for _ in range(3))
        table = [fmt.format(*row) for row in self.board]
        print('\n'.join(table))

    def print_leaderboard(self) -> None:
        print('Updated Leaderboard')
        sorted_db = self.database.sort_values(by=['Wins'], ascending=False).reset_index(drop=True)
        print(sorted_db)

    @testable
    def get_ai_move(self) -> tuple[int, int]:
        empty_cells = [[(x, y) for x, piece in enumerate(row) if piece == '_'] for y, row in enumerate(self.board)]
        # Turn list into 1-d list
        empty_cells_1d = [pos for sub_list in empty_cells for pos in sub_list]
        return random.choice(empty_cells_1d)

    @testable
    def is_valid_move(self, coordinates: tuple[int, int]) -> bool:
        if coordinates[0] < 0 or coordinates[0] > 2 or coordinates[1] < 0 or coordinates[1] > 2:
            print('Error: The x and y coordinates must be 0 <= value < 3')
            return False
        if self.board[coordinates[0]][coordinates[1]] != '_':
            print(f'Error: The cell {coordinates[0], coordinates[1]} is already occupied')
            return False
        return True

    def get_move(self, player_name: str) -> tuple[int, int]:
        if not player_name:
            print('_' * 30, '\n')
            return self.get_ai_move()
        move = str(input(f'{player_name}: Enter the square you would like to play in in the format "x, y", '
                         f'where "0, 0" is the top left corner: '))
        try:
            coordinates = *map(int, move.replace(' ', '').split(',')),
        except ValueError:
            print(f'Error: {move} does not match the expected format "x, y".')
            return self.get_move(player_name)

        coordinates = cast(tuple[int, int], coordinates)

        if not self.is_valid_move(coordinates):
            return self.get_move(player_name)

        return coordinates

    def update_board(self, coordinates: tuple[int, int], symbol: str) -> None:
        self.board[coordinates[0]][coordinates[1]] = symbol
        self.game_is_over(coordinates, symbol)

    @testable
    def game_is_over(self, last_move: tuple[int, int], symbol: str) -> None:
        row, col = last_move[0], last_move[1]
        target_symbol = {symbol}
        # Check horizontal
        if set(self.board[row]) == target_symbol:
            self.game_over = True
            return
        # Check vertical
        if {row[col] for row in self.board} == target_symbol:
            self.game_over = True
            return
        # Check right diagonal
        if {self.board[2][0], self.board[1][1], self.board[0][2]} == target_symbol:
            self.game_over = True
            return
        # Check left diagonal
        if {self.board[0][0], self.board[1][1], self.board[2][2]} == target_symbol:
            self.game_over = True

    def play_game(self) -> None:
        print('Welcome to Tic-Tac-Toe!')
        turns = 0
        current_player = [(self.player_one, self.player_one_symbol), (self.player_two, self.player_two_symbol)]
        while not self.game_over and turns < 9:
            self.print_board()
            player, symbol = current_player[turns % 2]
            move = self.get_move(player)
            self.update_board(move, symbol)
            turns += 1

        self.print_board()
        if turns >= 8:
            print('The game ended in a draw!')
        else:
            winner_name = current_player[(turns - 1) % 2][0]
            print(f'The winner is {winner_name}!')
            self.update_db(winner_name, True)
            self.update_db(current_player[(turns - 2) % 2][0], False)

        self.save_db()
        self.print_leaderboard()


if __name__ == '__main__':
    TicTacToe()
