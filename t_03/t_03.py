import string
from pathlib import Path

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


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(get_priority_sum(input_file.readlines()))
