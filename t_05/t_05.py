from pathlib import Path
from dataclasses import dataclass
import re

input_data_path = Path(__file__).with_name("data.txt")


def get_stacks_from_diagram(diagram_as_lines: list[str]) -> list[list[str]]:
    return [
        [line[i] for line in reversed(diagram_as_lines) if line[i].isalpha()]
        for i in range(1, len(diagram_as_lines[0]), 4)
    ]


@dataclass
class Instruction:
    amount: int
    source_stack: int
    target_stack: int

    def __init__(self, amount, source_stack, target_stack) -> None:
        self.amount = int(amount)
        self.source_stack = int(source_stack) - 1
        self.target_stack = int(target_stack) - 1


def parse_instructions(instructions_string: str) -> list[list[int]]:
    return [
        Instruction(*line)
        for line in re.findall(
            "move ([0-9]+) from ([0-9]+) to ([0-9]+)", instructions_string
        )
    ]


def move_creates(
    current_state: list[list[int]], instructions: list[Instruction]
) -> list[list[int]]:
    for instruction in instructions:
        for i in range(instruction.amount):
            current_state[instruction.target_stack].append(
                current_state[instruction.source_stack].pop()
            )
    return current_state


def get_result(current_state: list[list[int]]) -> str:
    return "".join((stack[-1] for stack in current_state))


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        diagram, instructions = input_file.read().split("\n\n")
        initial_state = get_stacks_from_diagram(diagram.split("\n"))
        parsed_instructions = parse_instructions(instructions)
        print(get_result(move_creates(initial_state, parsed_instructions)))
