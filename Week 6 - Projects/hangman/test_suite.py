import io
import math
import string
from collections.abc import Callable, Iterable
from unittest.mock import patch
from contextlib import redirect_stdout


def exercise_1_tests(klass: Callable) -> None:
    game = klass('example')
    assert len(game.completed_word) == 7
    assert game.completed_word == ['_', '_', '_', '_', '_', '_', '_']
    assert game.letters == ['e', 'x', 'a', 'm', 'p', 'l', 'e']

    game2 = klass('complete')
    assert len(game2.completed_word) == 8
    assert game2.completed_word == ['_', '_', '_', '_', '_', '_', '_', '_']
    assert game2.letters == ['c', 'o', 'm', 'p', 'l', 'e', 't', 'e']
    print('Tests passed, you may now move on to the next exercise')


def exercise_2_tests(klass: Callable) -> None:
    game = klass('word')
    assert len(game.completed_word) == 4
    assert game.completed_word == ['_', '_', '_', '_']
    assert game.letters == ['w', 'o', 'r', 'd']

    game2 = klass()
    assert game2.word is not None
    assert len(game2.completed_word) == len(game2.word)
    assert game2.letters == list(game2.word)
    print('Tests passed, you may now move on to the next exercise')


def play_mock_game(klass: Callable, side_effect: Iterable[str], word: str) -> list[str]:
    with patch('builtins.input', side_effect=side_effect):
        with io.StringIO() as buf, redirect_stdout(buf):
            game = klass(word)
            assert len(game.completed_word) == len(word)
            output = buf.getvalue()

    return output.splitlines()


def exercise_3_tests(klass: Callable) -> None:
    print(f'Playing game with inputs \'{list(string.ascii_lowercase)}\' with target word \'Test\'')
    output_lines = play_mock_game(klass, list(string.ascii_lowercase), 'Test')
    assert len(output_lines) == 7, f'Error: Expected to find 7 output lines, but instead found {len(output_lines)}'
    assert output_lines[0] == '____', f'Error: \'{output_lines[0]}\' does not match the expected output of \'____\''

    expected_output = 'That guess is incorrect. You have {} guesses remaining'
    guesses = 5
    for idx in range(1, len(output_lines)):
        expected = expected_output.format(guesses)
        guesses -= 1
        assert output_lines[idx] == expected, f'Error: \'{output_lines[idx]}\' does not match the expected output of \'{expected}\''

    # Test 2: Check output when a letter has already been guessed
    print(f'Playing game with inputs \'{list("ttstmnbvcxz")}\' with target word \'Temporary\'')
    output_lines = play_mock_game(klass, list('ttstmnbvcxz'), 'Temporary')
    guesses = 5
    assert output_lines[0] == '_________', f'Error: \'{output_lines[0]}\' does not match the expected output of \'_________\''
    for idx in range(1, len(output_lines)):
        if idx in [1, 3]:
            expected = 'Error: The letter t has already been guessed'
            assert output_lines[idx] == expected, f'Error: \'{output_lines[idx]}\' does not match the expected output of \'{expected}\''
            continue
        expected = expected_output.format(guesses)
        guesses -= 1
        assert output_lines[idx] == expected, f'Error: \'{output_lines[idx]}\' does not match the expected output of \'{expected}\''

    print('Tests passed, you may now move on to the next exercise')


def exercise_4_tests(klass: Callable) -> None:
    # Test 1: Success case, game completes successfully
    test_complete_game_success_case(klass)
    test_complete_game_failure_case(klass)


def test_complete_game_success_case(klass: Callable) -> None:
    print(f'Playing game with inputs \'{list("word")}\' with target word \'word\'')
    output_lines = play_mock_game(klass, list('word'), 'word')
    assert len(output_lines) == 10, f'Expected to find 10 output lines, but instead found {len(output_lines)}'
    expected_word_output = ['____', 'w___', 'wo__', 'wor_', 'word']
    expected_message_output = [
        'The letter \'w\' is correct!',
        'The letter \'o\' is correct!',
        'The letter \'r\' is correct!',
        'The letter \'d\' is correct!',
        'Congratulation, you won with 6 guesses left!',
    ]
    for idx, line in enumerate(output_lines):
        if idx % 2 == 0:
            expected_line = expected_word_output[int(idx / 2)]
            assert line == expected_line, f'Expected output for line {idx} to be \'{expected_line}\', but instead found {line}'
        else:
            expected_line = expected_message_output[math.floor(idx / 2)]
            assert line == expected_line, f'Expected output for line {idx} to be \'{expected_line}\', but instead found {line}'


def test_complete_game_failure_case(klass: Callable) -> None:
    print(f'Playing game with inputs \'{list("wnrklzmwpqs")}\' with target word \'word\'')
    output_lines = play_mock_game(klass, list('wnrklzmwpqs'), 'word')
    assert len(output_lines) == 14, f'Expected to find 14 output lines, but instead found {len(output_lines)}'
    expected_output = ['____', "The letter 'w' is correct!", 'w___', 'That guess is incorrect. You have 5 guesses remaining',
                       "The letter 'r' is correct!", 'w_r_', 'That guess is incorrect. You have 4 guesses remaining',
                       'That guess is incorrect. You have 3 guesses remaining', 'That guess is incorrect. You have 2 guesses remaining',
                       'That guess is incorrect. You have 1 guesses remaining', 'Error: The letter w has already been guessed',
                       'That guess is incorrect. You have 0 guesses remaining', 'You are out of guesses! Better luck next time.',
                       'The correct answer was word']
    for idx, line in enumerate(output_lines):
        assert line == expected_output[idx], f'Error: Expected line {idx} to be {expected_output[idx]}, but instead found {line}'

