from typing import cast

import pandas as pd

# Welcome to the TicTacToe project!
# In this project we will build a text-based implementation of Tic-Tac-Toe. We will
# use Pandas to create a database to persist player statistics between games, and
# will create an automated opponent to allow people to play against the computer.
# The basic building blocks needed for this project have been provided for you. We
# will implement the game in the TicTacToe class. The __init__ and print_board
# functions have been provided for you, and you should not need to edit these. The
# other functions provided are currently empty - we will implement these throughout
# this project, feel free to add functions of your own where you see fit.

# Exercise
# In this exercise we will implement the init_game and init_db functions.
# Implement init_game to do the following:
#   - First call the init_db function.
#   - Ask the user to enter a name for player one and assign the value to the class
#     attribute player_one.
#   - Check if the name provided exists in the database, if not call insert_into_database
#     with the players name - we will implement this later.
#   - Ask the user to enter a name for the second player. This input should be optional,
#     and if no input is provided, the computer will player against the AI. If a name is
#     provided, assign it to that player_two class attribute.
#   - Check if the name provided exists in the database, if not call insert_into_database
#     with the players name - we will implement this later.
# Implement init_db to do the following:
#   - If the file_name class attribute is not None, then use Pandas to read the CSV file
#     (you can assume the file is a valid CSV). Assign the result to the database attribute.
#   - If the file_name attribute is None, then create a new Pandas DataFrame with the following
#     three columns and assign it to the database attribute:
#       - Name
#       - Wins
#       - Losses


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
        pass

    def init_db(self) -> None:
        pass

    def insert_into_database(self, name: str) -> None:
        pass

    def update_db(self, name: str, won: bool) -> None:
        pass

    def save_db(self) -> None:
        pass

    def print_board(self) -> None:
        fmt = '\t'.join('{:1}' for _ in range(3))
        table = [fmt.format(*row) for row in self.board]
        print('\n'.join(table))

    def print_leaderboard(self) -> None:
        pass

    def get_ai_move(self) -> tuple[int, int]:
        pass

    def is_valid_move(self, coordinates: tuple[int, int]) -> bool:
        pass

    def get_move(self, player_name: str) -> tuple[int, int]:
        pass

    def update_board(self, coordinates: tuple[int, int], symbol: str) -> None:
        pass

    def game_is_over(self, last_move: tuple[int, int], symbol: str) -> None:
        pass

    def play_game(self) -> None:
        pass


if __name__ == '__main__':
    input_file = str(input('Enter path to database file (or press enter to create new): ')) or None
    TicTacToe(input_file)
