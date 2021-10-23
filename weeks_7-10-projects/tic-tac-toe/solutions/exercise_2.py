from typing import cast

import pandas as pd

from ..test_suite import exercise_2_tests, testable

# Exercise 2 - Solution
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

    @testable:
        pass

    @testable
    def is_valid_move(self, coordinates: tuple[int, int]) -> bool:
        pass

    def get_move(self, player_name: str) -> tuple[int, int]:
        pass

    def update_board(self, coordinates: tuple[int, int], symbol: str) -> None:
        pass

    @testable
    def game_is_over(self, last_move: tuple[int, int], symbol: str) -> None:
        pass

    def play_game(self) -> None:
        pass


if __name__ == '__main__':
    exercise_2_tests(TicTacToe)
    input_file = str(input('Enter path to database file (or press enter to create new): ')) or None
    TicTacToe(input_file)
