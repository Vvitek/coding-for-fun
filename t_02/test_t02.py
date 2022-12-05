import pytest
from .t_02 import (
    GameResult,
    Option,
    calculate_score,
    get_game_result,
    get_score_from_text_line,
)


@pytest.mark.parametrize(
    "my_choice, opponent_choice, expected_result",
    [
        (Option.PAPER, Option.ROCK, GameResult.WIN),
        (Option.ROCK, Option.SCISSORS, GameResult.WIN),
        (Option.SCISSORS, Option.PAPER, GameResult.WIN),
        (Option.PAPER, Option.PAPER, GameResult.DRAW),
        (Option.ROCK, Option.ROCK, GameResult.DRAW),
        (Option.SCISSORS, Option.SCISSORS, GameResult.DRAW),
        (Option.SCISSORS, Option.ROCK, GameResult.LOST),
        (Option.ROCK, Option.PAPER, GameResult.LOST),
        (Option.PAPER, Option.SCISSORS, GameResult.LOST),
    ],
)
def test_get_game_score(my_choice, opponent_choice, expected_result):
    assert get_game_result(my_choice, opponent_choice) == expected_result


@pytest.mark.parametrize(
    "result, my_choice, expected_score",
    [
        (GameResult.WIN, Option.ROCK, 7),
        (GameResult.WIN, Option.PAPER, 8),
        (GameResult.WIN, Option.SCISSORS, 9),
        (GameResult.DRAW, Option.ROCK, 4),
        (GameResult.DRAW, Option.PAPER, 5),
        (GameResult.DRAW, Option.SCISSORS, 6),
        (GameResult.LOST, Option.ROCK, 1),
        (GameResult.LOST, Option.PAPER, 2),
        (GameResult.LOST, Option.SCISSORS, 3),
    ],
)
def test_calculate_score(result, my_choice, expected_score):
    assert calculate_score(result, my_choice) == expected_score


@pytest.mark.parametrize(
    "text_line, expected_result", [("A Y", 8), ("B X", 1), ("C Z", 6)]
)
def test_get_score_from_text_line(text_line, expected_result):
    assert get_score_from_text_line(text_line) == expected_result
