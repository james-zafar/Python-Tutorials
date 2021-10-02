from typing import cast

import pandas as pd

# Exercise 5
# In this exercise we will implement the play_game and print_leaderboard functions.
# This exercise will be less guided than the previous ones; a rough overview of what
# the functions need to do will be provided, and the implementation will be up to you.

# The play_game function should:
#   - Record whose turn it is and call get_move and update_board until a winner has been
#     found, or there are playable squares left.
#   - At the end of the game, the finished board should be printed, then if there was a
#     winner, output the winner, otherwise write a message to the console to inform the
#     players the game ended in a draw.
#   - If there was a winner, the database should be updated adding a win to the winning
#     player, and a loss to the losing player.
#   - The updated database should be saved to a file.
#   - The final output from play_game should be the updated leaderboard

# The print_leaderboard function should:
#   - Sort the database on wins, so that row 0 is the player with the highest number of
#     wins and print the sorted DataFrame


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

        self.play_game()

    def init_db(self) -> None:
        if self.file_name:
            self.database = pd.read_csv(self.file_name)
        else:
            self.database = pd.DataFrame(columns=['Name', 'Wins', 'Losses'])

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

    def get_ai_move(self) -> tuple[int, int]:
        pass

    def is_valid_move(self, coordinates: tuple[int, int]) -> bool:
        if coordinates[0] < 0 or coordinates[0] > 3 or coordinates[1] < 0 or coordinates[1] > 3:
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

        # Convert coordinator to list indices
        coordinates = (2 - coordinates[0], coordinates[1])
        return coordinates

    def update_board(self, coordinates: tuple[int, int], symbol: str) -> None:
        self.board[coordinates[0]][coordinates[1]] = symbol
        self.game_is_over(coordinates, symbol)

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
        pass


if __name__ == '__main__':
    input_file = str(input('Enter path to database file (or press enter to create new): ')) or None
    TicTacToe(input_file)
