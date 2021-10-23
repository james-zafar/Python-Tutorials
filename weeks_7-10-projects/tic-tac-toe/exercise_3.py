from typing import cast

import pandas as pd

from test_suite import exercise_3_tests, testable

# Exercise 3

# In this exercise we will implement the get_move and is_valid_move functions.

# Implement the get_move function as follows:
#   - If the player_name argument is empty, call get_ai_move and return the resulting
#     move - we will implement this later
#   - Else, ask the user to input a x, y pair, giving them an appropriate prompt to
#     indicate how they should format their input, for example:
#     {player_name}: Enter the square you would like to play in in the format "x, y",
#     where "0, 0" is the bottom left corner
#   - Check the input is a valid pair of integers and store them as a tuple of integers.
#   - Call is_valid_move to check the move is valid. If the function returns False, write
#     an appropriate error to the console - we will implement is_valid_move later
#   - Amend the coordinates provided as appropriate to ensure if the user inputs (0, 0)
#     that the bottom left square of the grid will be updated
#   - Repeat the above steps if any errors are encountered until the input is valid
# Implement the is_valid_move as follows:
#   - Check if either the x or y coordinates are not within the 3x3 grid, and if they are,
#     write a sensible error message to the console and return False
#   - Check the the requested grid cell is not already occupied by another symbol, and if
#   - it is, write a sensible error message to the console and return False
#   - Otherwise, the move is valid and you should return True


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
    exercise_3_tests(TicTacToe)
    input_file = str(input('Enter path to database file (or press enter to create new): ')) or None
    TicTacToe(input_file)
