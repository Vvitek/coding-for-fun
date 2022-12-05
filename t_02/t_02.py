from pathlib import Path
from enum import IntEnum

input_data_path = Path(__file__).with_name("data.txt")


class GameResult(IntEnum):
    WIN = 6
    DRAW = 3
    LOST = 0


class Option(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_game_result(my_choice: int, opponent_choice: int) -> int:
    return 1


def calculate_score(result: int, my_choice: int) -> int:
    return 1
