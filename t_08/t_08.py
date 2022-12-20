from typing import TextIO, NamedTuple
from pathlib import Path
import math

input_data_path = Path(__file__).with_name("data.txt")

GridIndex = NamedTuple("GridIndex", [("row", int), ("column", int)])
Directions = NamedTuple(
    "Directions",
    [("left", list[int]), ("right", list[int]), ("up", list[int]), ("down", list[int])],
)


def get_visible_trees_number(grid: list[list[int]]) -> int:
    return (
        sum(
            (
                sum(
                    is_visible(GridIndex(row=row_index, column=column_index), grid)
                    for row_index in range(1, len(grid[0]) - 1)
                )
                for column_index in range(1, len(grid) - 1)
            )
        )
        + 2 * (len(grid) + len(grid[0]))
        - 4
    )


def parse_file_to_grid(file: TextIO) -> list[list[int]]:
    return [[int(j) for j in line.strip()] for line in file]


def _get_directions(index: GridIndex, grid: list[list[int]]) -> Directions:
    return Directions(
        left=grid[index.row][0 : index.column],
        right=grid[index.row][index.column + 1 : len(grid[1])],
        up=[row[index.column] for row in grid[0 : index.row]],
        down=[row[index.column] for row in grid[index.row + 1 : len(grid)]],
    )


def is_visible(index: GridIndex, grid: list[list[int]]) -> bool:
    value = grid[index.row][index.column]
    return any(
        all((i < value for i in direction))
        for direction in _get_directions(index, grid)
    )


def get_scenic_score(value: int, list: list[int]) -> int:
    for index, element in enumerate(list):
        if element >= value:
            return index + 1
    return len(list)


def get_overall_scenic_score(index: GridIndex, grid: list[list[int]]) -> int:
    value = grid[index.row][index.column]
    left, right, up, down = _get_directions(index, grid)
    x = [get_scenic_score(value, i) for i in (right, down)] + [
        get_scenic_score(value, i[::-1]) for i in (left, up)
    ]
    return math.prod(x)


def get_max_overall_scenic_score(grid: list[list[int]]) -> int:
    return max(
        (
            max(
                (
                    get_overall_scenic_score(
                        GridIndex(row=row_index + 1, column=column_index + 1), grid
                    )
                    for column_index, _ in enumerate(row[1:-1])
                )
            )
            for row_index, row in enumerate(grid[1:-1])
        )
    )


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(get_max_overall_scenic_score(parse_file_to_grid(input_file)))
