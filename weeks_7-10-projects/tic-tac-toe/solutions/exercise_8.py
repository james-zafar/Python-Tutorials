import random
from pathlib import Path
from typing import cast

import pandas as pd

from ..test_suite import testable

# Exercise 8 - Solution
# IMPORTANT: To run the solutions, you must run the following to run tic-tac-toe
# as a package:
# python -m tic-tac-toe.solutions.exercise_8
# from outside of the tic-tac-toe directory


class Player:
    def __init__(self, name: str, symbol: str):
        self._name = name or None
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
        return self._board[coordinates[0]][coordinates[1]] == '_'

    def update_cell(self, coordinates: tuple[int, int], symbol: str) -> None:
        self._board[coordinates[0]][coordinates[1]] = symbol

    def game_over(self, last_move: tuple[int, int], symbol: str) -> bool:
        row, col = last_move[0], last_move[1]
        target_symbol = {symbol}
        # Check horizontal
        if set(self._board[row]) == target_symbol:
            return True
        # Check vertical
        if {row[col] for row in self._board} == target_symbol:
            return True
        # Check right diagonal
        if {self._board[2][0], self._board[1][1], self._board[0][2]} == target_symbol:
            return True
        # Check left diagonal
        if {self._board[0][0], self._board[1][1], self._board[2][2]} == target_symbol:
            return True
        return False

    def __str__(self) -> str:
        fmt = '\t'.join('{:1}' for _ in range(3))
        table = [fmt.format(*row) for row in self._board]
        return '\n'.join(table)


class TicTacToe:
    def __init__(self) -> None:
        self.DATABASE_FILE = 'tic_tac_toe.csv'

        self.board = Board()
        self.database = None  # type: pd.DataFrame
        self.player_one = None  # type: Player
        self.player_two = None  # type: Player
        self.game_over = False

        self.init_game()
        self.play_game()

    def init_game(self) -> None:
        self.init_db()
        player_one = str(input('Enter the name of Player 1: '))
        self.player_one = Player(player_one, 'O')
        if player_one not in self.database.Name.values:
            self.insert_into_database(player_one)

        player_two = str(input('Enter the name of Player 2, or press enter to play against the computer: '))
        self.player_two = Player(player_two, 'X')
        if player_two and player_two not in self.database.Name.values:
            self.insert_into_database(player_two)

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

    def print_leaderboard(self) -> None:
        print('Updated Leaderboard')
        sorted_db = self.database.sort_values(by=['Wins'], ascending=False).reset_index(drop=True)
        print(sorted_db)

    @testable
    def get_ai_move(self) -> tuple[int, int]:
        empty_cells = [[(x, y) for x, piece in enumerate(row) if piece == '_'] for y, row in enumerate(self.board.grid)]
        # Turn list into 1-d list
        empty_cells_1d = [pos for sub_list in empty_cells for pos in sub_list]
        return random.choice(empty_cells_1d)

    @testable
    def is_valid_move(self, coordinates: tuple[int, int]) -> bool:
        if coordinates[0] < 0 or coordinates[0] > 2 or coordinates[1] < 0 or coordinates[1] > 2:
            print('Error: The x and y coordinates must be 0 <= value < 3')
            return False
        if not self.board.cell_is_empty(coordinates):
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

    def play_game(self) -> None:
        print('Welcome to Tic-Tac-Toe!')
        turns = 0
        current_player = [self.player_one, self.player_two]
        while not self.game_over and turns < 9:
            print(str(self.board))
            player = current_player[turns % 2]
            move = self.get_move(player.name)
            self.board.update_cell(move, player.symbol)
            self.game_over = self.board.game_over(move, player.symbol)
            turns += 1

        print(str(self.board))
        if turns >= 8:
            print('The game ended in a draw!')
        else:
            winner_name = current_player[(turns - 1) % 2].name
            print(f'The winner is {winner_name}!')
            self.update_db(winner_name, True)
            self.update_db(current_player[(turns - 2) % 2].name, False)

        self.save_db()
        self.print_leaderboard()


if __name__ == '__main__':
    TicTacToe()
