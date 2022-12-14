import pytest
from t_05 import (
    Instruction,
    get_stacks_from_diagram,
    parse_instructions,
    move_creates,
    get_result,
    move_multi_creates,
)


def test_get_stacks_from_diagram():
    input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
    assert get_stacks_from_diagram(input.split("\n")) == [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
    ]


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        (
            """move 1 from 2 to 1
            move 3 from 1 to 3
            move 2 from 2 to 1
            move 1 from 1 to 2""",
            [Instruction(*i) for i in [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]],
        ),
    ],
)
def test_parse_instructions(input_string: str, expected_result: list[list[str]]):
    assert parse_instructions(input_string) == expected_result


@pytest.mark.parametrize(
    "current_state, instructions, expected_result",
    [
        (
            [
                ["Z", "N"],
                ["M", "C", "D"],
                ["P"],
            ],
            [Instruction(1, 2, 1)],
            [["Z", "N", "D"], ["M", "C"], ["P"]],
        ),
        (
            [["Z", "N", "D"], ["M", "C"], ["P"]],
            [Instruction(3, 1, 3)],
            [[], ["M", "C"], ["P", "D", "N", "Z"]],
        ),
        (
            [[], ["M", "C"], ["P", "D", "N", "Z"]],
            [Instruction(2, 2, 1)],
            [["C", "M"], [], ["P", "D", "N", "Z"]],
        ),
        (
            [["C", "M"], [], ["P", "D", "N", "Z"]],
            [Instruction(1, 1, 2)],
            [["C"], ["M"], ["P", "D", "N", "Z"]],
        ),
        (
            [
                ["Z", "N"],
                ["M", "C", "D"],
                ["P"],
            ],
            [
                Instruction(a, b, c)
                for a, b, c in [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
            ],
            [["C"], ["M"], ["P", "D", "N", "Z"]],
        ),
    ],
)
def test_move_creates(current_state, instructions, expected_result):
    assert move_creates(current_state, instructions) == expected_result


@pytest.mark.parametrize(
    "current_state, instructions, expected_result",
    [
        (
            [
                ["Z", "N"],
                ["M", "C", "D"],
                ["P"],
            ],
            [Instruction(1, 2, 1)],
            [["Z", "N", "D"], ["M", "C"], ["P"]],
        ),
        (
            [["Z", "N", "D"], ["M", "C"], ["P"]],
            [Instruction(3, 1, 3)],
            [[], ["M", "C"], ["P", "Z", "N", "D"]],
        ),
        (
            [[], ["M", "C"], ["P", "Z", "N", "D"]],
            [Instruction(2, 2, 1)],
            [["M", "C"], [], ["P", "Z", "N", "D"]],
        ),
        (
            [["M", "C"], [], ["P", "Z", "N", "D"]],
            [Instruction(1, 1, 2)],
            [["M"], ["C"], ["P", "Z", "N", "D"]],
        ),
        (
            [
                ["Z", "N"],
                ["M", "C", "D"],
                ["P"],
            ],
            [
                Instruction(a, b, c)
                for a, b, c in [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
            ],
            [["M"], ["C"], ["P", "Z", "N", "D"]],
        ),
    ],
)
def test_move_multi_creates(current_state, instructions, expected_result):
    assert move_multi_creates(current_state, instructions) == expected_result


@pytest.mark.parametrize(
    "final_state, expected_result",
    [
        ([["M"], ["C"], ["P", "Z", "N", "D"]], "MCD"),
        ([["C"], ["M"], ["P", "D", "N", "Z"]], "CMZ"),
    ],
)
def test_get_result(final_state, expected_result):
    assert get_result(final_state) == expected_result
