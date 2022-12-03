from pathlib import Path

input_data_path = Path(__file__).with_name("data.txt")


def get_sum_calories(inventory: str) -> int:
    return sum([int(calories_amount) for calories_amount in inventory.split()])


def get_max_calories(input_data: str) -> int:
    return max(
        [get_sum_calories(inventory) for inventory in input_data.split(sep="\n\n")]
    )


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(get_max_calories(input_file.read()))
