from typing import TextIO, NamedTuple
from pathlib import Path

input_data_path = Path(__file__).with_name("data.txt")

GridIndex = NamedTuple("GridIndex", [("row", int), ("column", int)])


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


def is_visible(index: GridIndex, grid: list[list[int]]) -> bool:
    value = grid[index.row][index.column]
    left = grid[index.row][0 : index.column]
    right = grid[index.row][index.column + 1 : len(grid[1])]
    up = [row[index.column] for row in grid[0 : index.row]]
    down = [row[index.column] for row in grid[index.row + 1 : len(grid)]]
    return any(
        all((i < value for i in direction)) for direction in (left, right, up, down)
    )


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(get_visible_trees_number(parse_file_to_grid(input_file)))
