import pytest
from t_03 import get_same_element_in_both_compartments, get_priority, get_priority_sum


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
