from pathlib import Path

input_data_path = Path(__file__).with_name("data.txt")


def get_marker_position(input):
    four_signals = [i for i in input[:3]] + [None]
    for i in range(3, len(input), 1):
        four_signals[i % 4] = input[i]
        if len(four_signals) == len(set(four_signals)):
            return i + 1


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(get_marker_position(input_file.read()))
