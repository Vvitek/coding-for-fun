from pathlib import Path
from enum import IntEnum

input_data_path = Path(__file__).with_name("data.txt")


class GameResult(IntEnum):
    WIN = 2
    DRAW = 1
    LOST = 0


class Option(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


mapping_dict = {
    "A": Option.ROCK,
    "B": Option.PAPER,
    "C": Option.SCISSORS,
    "X": Option.ROCK,
    "Y": Option.PAPER,
    "Z": Option.SCISSORS,
}


def get_game_result(my_choice: Option, opponent_choice: Option) -> GameResult:
    return GameResult((my_choice - opponent_choice + 1) % 3)


def calculate_score(result: GameResult, my_choice: Option) -> int:
    return result * 3 + my_choice


def get_score_from_text_line(line: str) -> int:
    opponent_choice, my_choice = [
        mapping_dict[item] for item in line.rstrip().split(" ")
    ]
    return calculate_score(
        get_game_result(my_choice=my_choice, opponent_choice=opponent_choice),
        my_choice=my_choice,
    )


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(sum((get_score_from_text_line(line) for line in input_file)))
