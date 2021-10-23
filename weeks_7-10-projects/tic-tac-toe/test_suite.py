import collections
import io
import random
import re
from collections.abc import Callable
from contextlib import redirect_stdout
from functools import wraps
from typing import TypeVar
from unittest.mock import patch

import pandas as pd

T = TypeVar('T')


def testable(func: Callable) -> Callable:
    @wraps(func)
    def fn(self, *args, **kwargs):
        if hasattr(fn, '__call_count__'):
            fn.__call_count__ += 1
        else:
            fn.__call_count__ = 1
        if not hasattr(fn, 'called_with'):
            fn.called_with = []
        fn.called_with.append((fn.__call_count__, args, kwargs))
        return func(self, *args, **kwargs)

    return fn


def assertFuncCalled(func: Callable, call_count: int = 1) -> None:
    if not hasattr(func, '__wrapped__'):
        raise AttributeError('A function must be decorated with \'check_func_was_called\' to monitor execution')
    if not hasattr(func, '__call_count__'):
        raise AttributeError(f'Error: The function \'{func.__qualname__}\' is not decorated correctly')

    assert func.__call_count__ == call_count, f'Error: Expected \'{func.__qualname__}\' to be called {call_count} ' \
                                              f'times, but was instead called {func.__call_count__} times'


def assertCalledWith(func: Callable, call_no: int, *args, **kwargs) -> None:
    if not hasattr(func, '__wrapped__'):
        raise AttributeError('A function must be decorated with \'check_func_was_called\' to validate arguments')
    if not hasattr(func, 'called_with'):
        raise AttributeError(f'Error: The function \'{func.__qualname__}\' is not decorated correctly')
    func_args = list(filter(lambda arg: arg[0] == call_no, getattr(func, 'called_with')))[0]
    # Check args are the same
    assert func_args[1] == args, f'Error: Unexpected positional arguments. Expected {args}, but got {func_args[1]}'
    # Check kwargs are the same
    assert func_args[2] == kwargs, f'Error: Unexpected Keyword arguments. Expected {kwargs}, but got {func_args[2]}'


def test_print_leaderboard(game: T) -> None:
    with io.StringIO() as buf, redirect_stdout(buf):
        game.print_board()
        output = buf.getvalue().splitlines()
    assert len(output) == 3, 'Error: The print_board() function should not be modified'
    expected = ['_\t_\t_', '_\t_\t_', '_\t_\t_']
    assert output == expected, 'Error: The print_board() function should not be modified'


def exercise_1_tests(klass: Callable) -> T:
    with patch('builtins.input', side_effect=['Name_1', 'Name_2']):
        game = klass()
        print('Test 1: Check print_board has not been modified')
        test_print_leaderboard(game)
        print('Test 2: Check \'insert_into_database\' is called twice when two player names are entered...')
        assertFuncCalled(game.insert_into_database, 2)
        print('Test 3: Check arguments to \'insert_into_database\' are correct...')
        assertCalledWith(game.insert_into_database, 1, 'Name_1')
        assertCalledWith(game.insert_into_database, 2, 'Name_2')
        print('Test 4: Check implementation of \'init_db\'')
        database = game.database
        assert isinstance(database,pd.DataFrame), f'Error: self.database should be of type \'pd.DataFrame\', not {type(database)}'
        expected_cols = ['Name', 'Wins', 'Losses']
        cols = database.columns.to_list()
        assert collections.Counter(cols) == collections.Counter(expected_cols), f'Error: Database should contain columns ' \
                                                                                f'{expected_cols}, but instead contains {cols}'

        return game


def exercise_2_tests(klass: Callable) -> T:
    game = exercise_1_tests(klass)
    print('Test 5: Check new players have been added to the database...')
    db = game.database
    # Could replace this with a more efficient query, but it's not particularly important for small dfs
    assert ((db['Name'] == 'Name_1') & (db['Wins'] == 0) & (db['Losses'] == 0)).any(), 'Error: \'Name_1\' has not been ' \
                                                                                       'added to the database successfully'
    assert ((db['Name'] == 'Name_2') & (db['Wins'] == 0) & (db['Losses'] == 0)).any(), 'Error: \'Name_2\' has not been ' \
                                                                                       'added to the database successfully'
    # create mock database
    mock_database = pd.DataFrame([['Test', 0, 0]], columns=['Name', 'Wins', 'Losses'])
    game.database = mock_database

    print('Test 6: Check that losses are updated correctly in update_db...')
    game.update_db('Test', False)
    assert ((game.database['Name'] == 'Test') & (game.database['Wins'] == 0)
            & (game.database['Losses'] == 1)).any(), 'Error: update_db failed to update losses correctly.'

    print('Test 7: Check that wins are updated correctly in update_db...')
    game.update_db('Test', True)
    assert ((game.database['Name'] == 'Test') & (game.database['Wins'] == 1)
            & (game.database['Losses'] == 1)).any(), 'Error: update_db failed to update losses correctly.'
    # Reset database
    game.database = db

    print('Test 8: Check save_db works correctly...')
    real_file_name = game.file_name
    mock_output_file = io.StringIO()
    game.file_name = mock_output_file
    game.save_db()
    output_lines = mock_output_file.getvalue().splitlines()
    expected = ['Name,Wins,Losses', 'Name_2,0,0', 'Name_1,0,0']
    assert output_lines == expected, 'Error: save_db did not correctly save the database to the CSV file specified in self.file_name'
    game.file_name = real_file_name

    return game


def exercise_3_tests(klass: Callable) -> T:
    game = exercise_2_tests(klass)
    print('Test 9: Check get_move works correctly...')
    with patch('builtins.input', side_effect=['2, a', '10, 10', '2,2']):
        with io.StringIO() as buf, redirect_stdout(buf):
            return_val = game.get_move(game.player_one)
            lines = buf.getvalue().splitlines()
    assert len(lines) == 2, 'Error: Expected get_move to print 2 error message when given an inputs of "10, 10" and "2, a"'
    regex = re.compile(r'.*Error.*')
    assert regex.match(lines[0]) is not None, 'Error: The error message should contain "Error"...'
    assert regex.match(lines[1]) is not None, 'Error: The error message should contain "Error"...'

    # Check the return value is correct
    assert isinstance(return_val, tuple), f'Error: get_move should return a tuple, not a {type(return_val).__name__}'
    assert len(return_val) == 2, f'Error: get_move should return a tuple of length 2, but got tuple of length {len(return_val)}'
    assert all(isinstance(ele, int) for ele in return_val), 'Error: get_move should return a tuple of integers.'

    assertFuncCalled(game.is_valid_move, 2)
    assertCalledWith(game.is_valid_move, 1, (10, 10))
    assertCalledWith(game.is_valid_move, 2, (2, 2))

    return game


def exercise_4_tests(klass: Callable) -> T:
    game = exercise_3_tests(klass)
    print('Test 10: Check update_board works correctly...')
    game.update_board((2, 2), 'X')
    assert game.board[2][2] == 'X', 'Error: update_board has not updated the board correctly.'
    assertFuncCalled(game.game_is_over)
    assertCalledWith(game.game_is_over, 1, (2, 2), 'X')
    assert not game.game_over, 'Error: self.game_over should be False'
    return game


def exercise_5_tests(klass: Callable) -> T:
    game = exercise_4_tests(klass)

    real_file_name = game.file_name
    game.file_name = io.StringIO()
    print('Test 11: Check that we can complete a full game...')
    try:
        with patch('builtins.input',
                   side_effect=['0, 0', '1,1', '0,2', '2,2', 'a,b', '3,3', '0,1', '1,0', '1,2', '2,0', '2,1']):
            with io.StringIO() as buf, redirect_stdout(buf):
                game.play_game()
                lines = buf.getvalue().splitlines()
    except StopIteration:
        raise AssertionError('Error: The game did not end when a player had won.')

    expected_board = ['_\t_\t_\n_\t_\t_\n_\t_\tX',
                      'O\t_\t_\n_\t_\t_\n_\t_\tX',
                      'O\t_\t_\n_\tX\t_\n_\t_\tX',
                      'O\t_\tO\n_\tX\t_\n_\t_\tX',
                      'O\tX\tO\n_\tX\t_\n_\t_\tX',
                      'O\tX\tO\nO\tX\t_\n_\t_\tX',
                      'O\tX\tO\nO\tX\tX\n_\t_\tX',
                      'O\tX\tO\nO\tX\tX\nO\t_\tX']
    expected_errors = ['Error: The cell (2, 2) is already occupied',
                       'Error: a,b does not match the expected format "x, y".',
                       'Error: The x and y coordinates must be 0 <= value < 3', ]
    idx = 0
    error_count = 0
    expected_idx = 0
    while idx < len(lines):
        line = lines[idx]
        if '\t' in line:
            actual = '\n'.join(lines[idx:idx + 3])
            expected = expected_board[expected_idx]
            assert expected == actual, f'Error: Board should be \n{expected}\n after {expected_idx} moves, but is instead \n{actual}\n'
            expected_idx += 1
            idx += 3
        elif 'error' in line.lower():
            error_count += 1
            idx += 1
        else:
            idx += 1
    # We don't mandate the content for error message, so it is difficult to validate the correct error is being printed
    print('Test 12: Check the game correctly prints error messages for bad input...')
    assert error_count == len(expected_errors), f'Error: Expected to encounter 3 error messages, ' \
                                                f'but instead encountered {error_count}'
    game.file_name = real_file_name
    return game


def exercise_6_tests(klass: Callable) -> None:
    _ = exercise_5_tests(klass)
    print('Test 13: Check a game can run to completion when playing against the automated opponent...')
    random.seed(50)
    with patch('builtins.input', side_effect=['player1', '']):
        game = klass()
    game_file = game.file_name
    mock_file = io.StringIO()
    game.file_name = mock_file
    try:
        with patch('builtins.input', side_effect=['0, 0', '0,1', '0,2']):
            with io.StringIO() as buf, redirect_stdout(buf):
                game.play_game()
                lines = buf.getvalue().splitlines()
    except StopIteration:
        raise AssertionError('Error: The game did not complete as expected. Check your implementation of get_ai_move...')
    lines = [line for line in lines if '\t' in line or 'winner' in line]
    expected_lines = [
        '_\t_\t_', '_\t_\t_', '_\t_\t_',
        'O\t_\t_', '_\t_\t_', '_\t_\t_',
        'O\t_\t_', '_\t_\t_', '_\t_\tX',
        'O\tO\t_', '_\t_\t_', '_\t_\tX',
        'O\tO\t_', '_\tX\t_', '_\t_\tX',
        'O\tO\tO', '_\tX\t_', '_\t_\tX',
        'The winner is player1!']
    if len(lines) < 18:
        raise AssertionError(
            'Error: Too little output was produced when running the game against an automated opponent.')
    for idx in range(0, len(lines), 3):
        if idx == 18:
            assert 'player1' in lines[idx], 'Error: The game did not output the winner correctly.'
            continue
        expected = '\n'.join(expected_lines[idx:idx + 3])
        actual = '\n'.join(lines[idx:idx + 3])
        assert expected == actual, f'Error: The board after {idx % 3} moves should be \n{expected}\n, ' \
                                   f'but is instead \n{actual}\n'

    print('Test 14: Check the leaderboard saves correctly')
    database_content = mock_file.getvalue()
    expected = 'Name,Wins,Losses\nplayer1,1,0\n'
    assert database_content == expected, f'Error: The content of the database file is incorrect. Expected to ' \
                                         f'find \n\'{expected}\'\n, but instead found \n\'{database_content}\''

    print('Test 15: Check functions were called correctly when playing against an automated opponent...')
    assertFuncCalled(game.get_ai_move, 2)

    game.file_name = game_file
    print('Success: All tests passed!')
