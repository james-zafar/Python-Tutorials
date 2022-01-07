import random
from typing import cast

import pandas as pd

from test_suite import testable


# Exercise 7 - Refactoring
# We now have a fully functioning game of Tic-Tac-Toe which has both a one and two
# player mode, and persists data about the players records between games. You may
# have noticed that some features implemented up to this point do not always
# work as expected, or you may have noticed some ways in which we could improve the
# quality of the code. In this exercise we will address some of these problems before
# implementing one final feature.

# Exercises:
# 1 - When the game starts, we ask the user to provide a file name of an existing database
#     if they have one. If the file name they enter is not valid the code will raise a
#     FileNotFoundError which we do not handle. We could add an exception handler to this
#     block of code to ensure we can continue even if we fail to load the file. In fact, this
#     is not necessary - we choose the file name of the database (tic_tac_toe.csv), so instead
#     of asking the user to provide the file name, we can look for this file automatically, and
#     if it doesn't exist, then create a new database. Update the code to perform this action.
#       - It would be a good idea to store the file name as a constant that is an attribute of the
#         TicTacToe class to make it easy to change later.
#       - You can construct a pathlib.Path object using Path('./path/to/file') and call path.is_file()
#         to check if the path exists
#       - Remember to change references to the file name in __init__, init_db and save_db!
# 2 - When playing against an automated opponent, the board outputs twice in a row without any
#     gap which may be confusing to the user. Can you improve the implementation to print a
#     horizontal line or 30 characters and a blank line between outputs only if the next turn is
#     the turn of the automated opponent? Feel free to implement this wherever you see fit.


class TicTacToe:
    def __init__(self, database_file: str = None) -> None:
        self.file_name = database_file

        self.board = [['_' for _ in range(3)] for _ in range(3)]
        self.database = None  # type: pd.DataFrame
        self.player_one = None
        self.player_two = None
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

        self.play_game()

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
    input_file = str(input('Enter path to database file (or press enter to create new): ')) or None
    TicTacToe(input_file)
