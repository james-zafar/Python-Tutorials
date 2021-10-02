import random
from pathlib import Path
from typing import cast

import pandas as pd

# Final solution
# This code is similar to the solution for Exercise 9 with a few improvements to Board:
#   - Board has a new empty_cells property to return the coordinates of any empty grid
#       cells which is used by get_ai_move


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
    def empty_cells(self) -> list[tuple[int, int]]:
        empty_cells = [[(x, y) for x, piece in enumerate(row) if piece == '_'] for y, row in enumerate(self._board)]
        empty_cells_1d = [pos for sub_list in empty_cells for pos in sub_list]
        return empty_cells_1d

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
        if not self.empty_cells:
            return True
        return False

    def __str__(self) -> str:
        fmt = '\t'.join('{:1}' for _ in range(3))
        table = [fmt.format(*row) for row in self._board]
        return '\n'.join(table)


class Leaderboard:
    def __init__(self):
        self.DATABASE_FILE = 'tic_tac_toe.csv'
        self._leaderboard = None  # type: pd.DataFrame

    def init_db(self) -> None:
        path = Path(self.DATABASE_FILE)
        if path.is_file():
            self._leaderboard = pd.read_csv(path)
        else:
            self._leaderboard = pd.DataFrame(columns=['Name', 'Wins', 'Losses'])

    def name_exists(self, name: str) -> bool:
        return name in self._leaderboard.Name.values

    def insert(self, name: str) -> None:
        row = [name, 0, 0]
        self._leaderboard.loc[-1] = row
        self._leaderboard.index = self._leaderboard.index + 1
        self._leaderboard = self._leaderboard.sort_index()

    def update(self, name: str, column: str) -> None:
        if column != 'Wins' and column != 'Losses':
            raise AttributeError(f'LeaderBoard has no column named \'{column}\'')
        if name is not None:
            self._leaderboard.loc[self._leaderboard.Name == name, column] += 1

    def close(self) -> None:
        self._leaderboard.to_csv(self.DATABASE_FILE, index=False)

    def print_leaderboard(self) -> None:
        print('Updated Leaderboard')
        sorted_db = self._leaderboard.sort_values(by=['Wins'], ascending=False).reset_index(drop=True)
        print(sorted_db)


class TicTacToe:
    def __init__(self) -> None:
        self.DATABASE_FILE = 'tic_tac_toe.csv'

        self.board = Board()
        self.leaderboard = Leaderboard()  # type: Leaderboard
        self.player_one = None  # type: Player
        self.player_two = None  # type: Player
        self.game_over = False

        self.init_game()

    def init_game(self) -> None:
        self.leaderboard.init_db()
        player_one = str(input('Enter the name of Player 1: '))
        self.player_one = Player(player_one, 'O')
        if not self.leaderboard.name_exists(player_one):
            self.leaderboard.insert(player_one)

        player_two = str(input('Enter the name of Player 2, or press enter to play against the computer: '))
        self.player_two = Player(player_two, 'X')
        if player_two and not self.leaderboard.name_exists(player_two):
            self.leaderboard.insert(player_two)

        self.play_game()

    def get_ai_move(self) -> tuple[int, int]:
        # rand_coords = random.choice(self.board.empty_cells)
        return random.choice(self.board.empty_cells)

    def is_valid_move(self, coordinates: tuple[int, int]) -> bool:
        if coordinates[0] < 0 or coordinates[0] > 3 or coordinates[1] < 0 or coordinates[1] > 3:
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
            print(f'Error: \'{move}\' does not match the expected format "x, y".')
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
        if not self.board.empty_cells:
            print('The game ended in a draw!')
        else:
            winner_name = current_player[(turns - 1) % 2].name
            print(f'The winner is {winner_name}!')
            self.leaderboard.update(winner_name, 'Wins')
            self.leaderboard.update(current_player[(turns - 2) % 2].name, 'Losses')

        self.leaderboard.print_leaderboard()
        self.leaderboard.close()


if __name__ == '__main__':
    TicTacToe()
