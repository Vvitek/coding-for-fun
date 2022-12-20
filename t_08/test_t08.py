import pytest

from t_08 import (
    get_visible_trees_number,
    is_visible,
    GridIndex,
    get_scenic_score,
    get_overall_scenic_score,
)


test_data = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]


@pytest.mark.parametrize(
    "index, expected_result",
    [
        (GridIndex(row=1, column=1), True),
        (GridIndex(row=1, column=2), True),
        (GridIndex(row=1, column=3), False),
        (GridIndex(row=2, column=1), True),
        (GridIndex(row=2, column=2), False),
        (GridIndex(row=2, column=3), True),
        (GridIndex(row=3, column=1), False),
        (GridIndex(row=3, column=2), True),
        (GridIndex(row=3, column=3), False),
    ],
)
def test_is_visible(index, expected_result):
    assert is_visible(index, test_data) == expected_result


@pytest.mark.parametrize(
    "index, expected_result",
    [
        (GridIndex(row=1, column=2), 4),
        (GridIndex(row=3, column=2), 8),
    ],
)
def test_get_overall_scenic_score(index, expected_result):
    assert get_overall_scenic_score(index, test_data) == expected_result


@pytest.mark.parametrize(
    "value, direction, expected_result",
    [
        (5, [3], 1),
        (5, [5, 2], 1),
        (5, [1, 2], 2),
        (5, [3, 5, 3], 2),
        (5, [3, 3], 2),
        (5, [3], 1),
        (5, [4, 9], 2),
    ],
)
def test_get_scenic_score(value, direction, expected_result):
    assert get_scenic_score(value, direction) == expected_result


def test_get_visible_trees_number():
    expected_result = 21
    assert get_visible_trees_number(test_data) == expected_result
