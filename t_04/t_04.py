from pathlib import Path

input_data_path = Path(__file__).with_name("data.txt")


def prepare_ranges(line):
    return [[int(j) for j in i.split("-")] for i in line.strip().split(",")]


def is_fully_contained(ranges):
    for i in range(2):
        if (
            ranges[i][0] >= ranges[(i + 1) % 2][0]
            and ranges[i][1] <= ranges[(i + 1) % 2][1]
        ):
            return True
    return False


def is_partialy_contained(ranges):
    for i in range(2):
        if (
            ranges[i][0] <= ranges[(i + 1) % 2][0] <= ranges[i][1]
            or ranges[i][0] <= ranges[(i + 1) % 2][1] <= ranges[i][1]
        ):
            return True
    return False


def get_sum(input_file, method_to_run):
    return sum((method_to_run(prepare_ranges(line)) for line in input_file))


def get_nuber_of_fully_contained(input_file):
    return sum((is_fully_contained(prepare_ranges(line)) for line in input_file))


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(get_sum(input_file, is_partialy_contained))
