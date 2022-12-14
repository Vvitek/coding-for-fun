from pathlib import Path

import t_04.t_04 as t_04


input_data_path = Path(__file__).parent.joinpath("t_04", "data.txt")

if __name__ == "__main__":
    with input_data_path.open("r") as input_file:
        print(t_04.get_sum(input_file, t_04.is_partialy_contained))
