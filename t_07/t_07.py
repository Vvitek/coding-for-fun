from pathlib import Path
from typing import TextIO

input_data_path = Path(__file__).with_name("data.txt")


TOTAL_FILE_SYSTEM_SPACE = 70000000
FREE_SPACE_REQUIRED_FOR_UPDATE = 30000000


def parse_commands(input_file: TextIO) -> dict[str, list[int]]:
    file_system = {}
    cwd_list = []
    for line in input_file:
        match line.split():
            case ["$", "cd", ".."]:
                cwd_list.pop()
            case ["$", "cd", cwd]:
                cwd_list.append(cwd)
                if "/".join(cwd_list) not in file_system:
                    file_system["/".join(cwd_list)] = []
            case ["$", "ls"]:
                print(f"list directory {cwd_list}")
            case ["dir", directory]:
                print(f"next directory {cwd_list}")
            case [size, name] if size.isdigit():
                file_system["/".join(cwd_list)].append(int(size))
            case _:
                raise ValueError(f"Unknown command {line}")
    return file_system


def get_dir_sizes(file_system: dict[str, list[int]]) -> dict[str, int]:
    return {name: sum(elements) for name, elements in file_system.items()}


def get_dir_sizes_with_subdirectories(
    total_sizes: dict[str, int]
) -> dict[str, dict[str, int]]:
    return {
        dir_name: {d: size for d, size in total_sizes.items() if d.startswith(dir_name)}
        for dir_name in total_sizes
    }


def get_total_dir_sizes_with_subdirectories(
    file_system_tree: dict[str, dict[str, int]]
) -> dict[str, int]:
    return {
        name: sum((i for i in dir.values())) for name, dir in file_system_tree.items()
    }


if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        file_system = parse_commands(input_file)
        total_sizes = get_dir_sizes(file_system)
        dir_sizes_with_subdirectorie = get_dir_sizes_with_subdirectories(total_sizes)
        total_dir_sizes_with_subdirectories = get_total_dir_sizes_with_subdirectories(
            dir_sizes_with_subdirectorie
        )
        print("ANSWER FOR PART1:", end=" ")
        print(
            sum(
                (
                    directory
                    for directory in total_dir_sizes_with_subdirectories.values()
                    if directory < 100000
                )
            )
        )
        missing_space = (
            FREE_SPACE_REQUIRED_FOR_UPDATE
            + total_dir_sizes_with_subdirectories["/"]
            - TOTAL_FILE_SYSTEM_SPACE
        )
        print("ANSWER FOR PART2:", end=" ")
        print(
            min(
                (
                    size
                    for size in total_dir_sizes_with_subdirectories.values()
                    if size >= missing_space
                )
            )
        )
