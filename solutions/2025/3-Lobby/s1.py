import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.join(current_dir, "../../../templates/python")
sys.path.append(utils_path)
import utils

# input_file = "input_example"
input_file = "input"

input_path = os.path.join(current_dir, input_file)

with open(input_path, "r", encoding="utf8") as file:
    data = file.read().split("\n")

def solution_1(data):
    """
    In each row:
    1. find largest integer (ignore last number) (ties pick first index) -> A
    2. find largest integer to right of A -> B
    3. result += AB
    """
    result = 0
    for row in data:
        int_list = list(map(int, list(row)))
        a_val = max(int_list[:-1])
        a_index = int_list.index(a_val)
        b_val = max(int_list[a_index + 1:])
        result += int(f"{a_val}{b_val}")

    print(result)

def solution_2(data):
    """
    - first digit -> ignore last 11
    - second digit -> ignore last 10
    ...
    """
    result = 0
    for row in data:
        int_list = list(map(int, list(row)))

        battery_values = [] # store result digits
        prev_i = -1 # look to right of this index

        for right_i_max in range(-11, 1, 1):
            # remove used left part of list (prevent finding same values)
            int_list = int_list[prev_i+1:]

            # hacky prevent int_list[:0] empty list issue
            if right_i_max == 0:
                val = max(int_list)
            else:
                val = max(int_list[:right_i_max])
            prev_i = int_list.index(val)

            battery_values.append(val)

        result += int("".join(list(map(str, battery_values))))

    print(result)

if __name__ == "__main__":
    solution_1(data)
    solution_2(data)
