import pytest
from pathlib import Path


from t_04 import (
    prepare_ranges,
    is_fully_contained,
    is_partialy_contained,
    get_sum,
)


@pytest.mark.parametrize(
    "raw_input, expected_result",
    [
        ("2-3,4-5", [[2, 3], [4, 5]]),
        ("2-4,6-8", [[2, 4], [6, 8]]),
        ("5-7,7-9", [[5, 7], [7, 9]]),
        ("2-8,3-7", [[2, 8], [3, 7]]),
        ("6-6,4-6", [[6, 6], [4, 6]]),
        ("2-6,4-8", [[2, 6], [4, 8]]),
    ],
)
def test_prepare_ranges(raw_input, expected_result):
    assert prepare_ranges(raw_input) == expected_result


@pytest.mark.parametrize(
    "ranges, expected_result",
    [
        ([[2, 3], [4, 5]], False),
        ([[2, 4], [6, 8]], False),
        ([[5, 7], [7, 9]], False),
        ([[2, 8], [3, 7]], True),
        ([[3, 7], [2, 8]], True),
        ([[6, 6], [4, 6]], True),
        ([[4, 6], [6, 6]], True),
        ([[2, 6], [4, 8]], False),
        ([[2, 6], [4, 8]], False),
        ([[14, 59], [14, 59]], True),
    ],
)
def test_is_fully_contained(ranges, expected_result):
    assert is_fully_contained(ranges) == expected_result


@pytest.mark.parametrize(
    "ranges, expected_result",
    [
        ([[2, 3], [4, 5]], False),
        ([[2, 4], [6, 8]], False),
        ([[5, 7], [7, 9]], True),
        ([[2, 8], [3, 7]], True),
        ([[3, 7], [2, 8]], True),
        ([[6, 6], [4, 6]], True),
        ([[4, 6], [6, 6]], True),
        ([[2, 6], [4, 8]], True),
        ([[2, 6], [4, 8]], True),
        ([[14, 59], [14, 59]], True),
    ],
)
def test_is_partialy_contained(ranges, expected_result):
    assert is_partialy_contained(ranges) == expected_result


@pytest.mark.parametrize("input_file_path, expected_result", [("data_for_test.csv", 2)])
def test_get_nuber_of_fully_contained(input_file_path, expected_result):
    with Path(__file__).with_name(input_file_path).open("r") as input_file:
        assert get_sum(input_file, is_fully_contained) == expected_result


@pytest.mark.parametrize("input_file_path, expected_result", [("data_for_test.csv", 4)])
def test_get_nuber_of_partialy_contained(input_file_path, expected_result):
    with Path(__file__).with_name(input_file_path).open("r") as input_file:
        assert get_sum(input_file, is_partialy_contained) == expected_result
