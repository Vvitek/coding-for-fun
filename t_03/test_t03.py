import pytest
from pathlib import Path

from t_03 import (
    get_same_element_in_both_compartments,
    get_priority,
    get_priority_sum,
    get_common_item,
    split_into_3_lines,
    get_common_badge_priorities,
)


@pytest.mark.parametrize(
    "elements, expected_result",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ],
)
def test_get_same_element_in_both_compartments(elements, expected_result):
    assert get_same_element_in_both_compartments(elements) == expected_result


@pytest.mark.parametrize(
    "element, expected_result",
    [("p", 16), ("L", 38), ("P", 42), ("v", 22), ("t", 20), ("s", 19)],
)
def test_get_priority(element, expected_result):
    assert get_priority(element) == expected_result


@pytest.mark.parametrize(
    "elements, expected_result",
    [
        (
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ],
            157,
        )
    ],
)
def test_get_priority_sum(elements, expected_result):
    assert get_priority_sum(elements) == expected_result


@pytest.mark.parametrize(
    "rucksacks, expected_result",
    [
        (
            (
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ),
            "r",
        ),
        (
            (
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ),
            "Z",
        ),
    ],
)
def test_get_common_item(rucksacks, expected_result):
    assert get_common_item(rucksacks) == expected_result


@pytest.mark.parametrize(
    "split_line_file_path, expected_result",
    [
        (
            "split_lines_data.csv",
            (
                (
                    "vJrwpWtwJgWrhcsFMMfFFhFp",
                    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                    "PmmdzqPrVvPwwTWBwg",
                ),
                (
                    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                    "ttgJtRGJQctTZtZT",
                    "CrZsJsPPZsGzwwsLwLmpwMDw",
                ),
            ),
        )
    ],
)
def test_split_into_3_lines(split_line_file_path, expected_result):
    with Path(__file__).with_name(split_line_file_path).open("r") as input_file:
        line_generator = split_into_3_lines(input_file)
        assert next(line_generator) == expected_result[0]
        assert next(line_generator) == expected_result[1]


@pytest.mark.parametrize(
    "split_line_file_path, expected_result", [("split_lines_data.csv", [18, 52])]
)
def test_get_common_badge_priorities(split_line_file_path, expected_result):
    with Path(__file__).with_name(split_line_file_path).open("r") as input_file:
        common_badge_priority_generator = get_common_badge_priorities(input_file)
        assert next(common_badge_priority_generator) == expected_result[0]
        assert next(common_badge_priority_generator) == expected_result[1]
