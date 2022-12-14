import pytest

from t_06 import get_marker_position


@pytest.mark.parametrize(
    "input_string, signal_length_expected_result_dict",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", ((4, 7), (14, 19))),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", ((4, 5), (14, 23))),
        ("nppdvjthqldpwncqszvftbrmjlhg", ((4, 6), (14, 23))),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", ((4, 10), (14, 29))),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", ((4, 11), (14, 26))),
    ],
)
def test_get_marker_position(input_string, signal_length_expected_result_dict):
    for singnal_length, expected_result in signal_length_expected_result_dict:
        assert get_marker_position(input_string, singnal_length) == expected_result
