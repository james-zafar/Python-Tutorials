import io
import math
import string
from collections.abc import Callable, Iterable
from unittest.mock import patch
from contextlib import redirect_stdout


def exercise_1_tests(klass: Callable) -> None:
    with patch('builtins.input', side_effect=['None', 'None']):
        game = klass()
        assert game.board == [['_' for _ in range(7)] for _ in range(6)], 'Error: The board does not match the expected dimensions, or contains incorrect values'
    print('All test cases passed!')
# def play_mock_game(klass: Callable, side_effect: Iterable[str], word: str) -> list[str]:
#     with patch('builtins.input', side_effect=side_effect):
#         with io.StringIO() as buf, redirect_stdout(buf):
#             game = klass(word)
#             assert len(game.completed_word) == len(word)
#             output = buf.getvalue()
#
#     return output.splitlines()