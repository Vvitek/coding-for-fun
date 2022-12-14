from pathlib import Path

input_data_path = Path(__file__).with_name("data.txt")


def get_marker_position(input: str, singnal_length: int) -> int:
    four_signals = [i for i in input[: singnal_length - 1]] + [None]
    for i in range(singnal_length - 1, len(input), 1):
        four_signals[i % singnal_length] = input[i]
        if len(four_signals) == len(set(four_signals)):
            return i + 1


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(get_marker_position(input_file.read(), 14))
