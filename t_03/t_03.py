import string
from pathlib import Path
from typing import Generator, TextIO

input_data_path = Path(__file__).with_name("data.txt")


def get_same_element_in_both_compartments(elements: str) -> str:
    second_compartment = set(elements[len(elements) // 2 :])
    for i in elements:
        if i in second_compartment:
            return i


def get_priority(element: str) -> int:
    return string.ascii_letters.index(element) + 1


def get_priority_sum(rucksacks: list[str]) -> int:
    return sum(
        [
            get_priority(get_same_element_in_both_compartments(rucksack))
            for rucksack in rucksacks
        ]
    )


def get_common_item(rucksacks: tuple[str]) -> str:
    return next(
        j for j in (i for i in rucksacks[0] if i in rucksacks[1]) if j in rucksacks[2]
    )


def split_into_3_lines(
    input_file: TextIO,
) -> Generator[tuple[tuple[str]], None, None]:
    return (
        (line1.rstrip(), line2.rstrip(), line3.rstrip())
        for line1, line2, line3 in zip(input_file, input_file, input_file)
    )


def get_common_badge_priorities(input_file: TextIO) -> Generator[int, None, None]:
    return (
        get_priority(get_common_item(line)) for line in split_into_3_lines(input_file)
    )


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(sum(get_common_badge_priorities(input_file)))
