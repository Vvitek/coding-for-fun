import pytest
from t_03 import get_same_element_in_both_compartments


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
