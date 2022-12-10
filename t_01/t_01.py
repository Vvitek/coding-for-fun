from pathlib import Path

input_data_path = Path(__file__).with_name("data.txt")


def get_sum_calories(inventory: str) -> int:
    return sum((int(calories_amount) for calories_amount in inventory.split()))


def get_max_calories(input_data: str) -> int:
    return max(
        (get_sum_calories(inventory) for inventory in input_data.split(sep="\n\n"))
    )


def get_n_max_calories(input_data: str, n_most_calories: int) -> tuple[int]:
    return sorted(
        (get_sum_calories(inventory) for inventory in input_data.split(sep="\n\n")),
        reverse=True,
    )[:n_most_calories]


def sum_n_max_calories(input_data: str, n_most_calories: int) -> int:
    return sum(get_n_max_calories(input_data, n_most_calories))


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(sum_n_max_calories(input_file.read(), 3))
