from typing import cast

import pandas as pd

from ..test_suite import exercise_3_tests, testable

# Exercise 3 - Solution
# IMPORTANT: To run the solutions, you must run the following to run tic-tac-toe
# as a package:
# python -m tic-tac-toe.solutions.exercise_2
# from outside of the tic-tac-toe directory


class TicTacToe:
    def __init__(self, database_file: str = None) -> None:
        self.file_name = database_file

        self.board = [['_' for _ in range(3)] for _ in range(3)]
        self.database = None  # type: pd.DataFrame
        self.player_one = None  # type; str
        self.player_two = None  # type: str
        self.player_one_symbol = 'O'
        self.player_two_symbol = 'X'
        self.game_over = False

        self.init_game()

    def init_game(self) -> None:
        self.init_db()
        self.player_one = str(input('Enter the name of Player 1: '))
        if self.player_one not in self.database.Name.values:
            self.insert_into_database(self.player_one)

        self.player_two = str(input('Enter the name of Player 2, or press enter to play against the computer: '))
        if self.player_two and self.player_two not in self.database.Name.values:
            self.insert_into_database(self.player_two)

    def init_db(self) -> None:
        if self.file_name:
            self.database = pd.read_csv(self.file_name)
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
        target_file = self.file_name if self.file_name else './tic_tac_toe.csv'
        self.database.to_csv(target_file, index=False)

    def print_board(self) -> None:
        fmt = '\t'.join('{:1}' for _ in range(3))
        table = [fmt.format(*row) for row in self.board]
        print('\n'.join(table))

    def print_leaderboard(self) -> None:
        pass

    @testable
    def get_ai_move(self) -> tuple[int, int]:
        pass
    
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
        pass

    @testable
    def game_is_over(self, last_move: tuple[int, int], symbol: str) -> None:
        pass

    def play_game(self) -> None:
        pass


if __name__ == '__main__':
    exercise_3_tests(TicTacToe)
    input_file = str(input('Enter path to database file (or press enter to create new): ')) or None
    TicTacToe(input_file)
